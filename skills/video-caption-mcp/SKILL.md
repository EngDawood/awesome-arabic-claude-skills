---
name: video-caption-mcp
description: This skill should be used when the user asks to "caption this video", "burn subtitles into this TikTok", "translate this reel", "add Arabic captions to this video", "subtitle this YouTube short", "change the caption font", "fix this caption line", asks how to connect to or use the video-caption MCP server, or mentions its tools by name (submit_job, job_status, get_output, cancel_job, restyle_job, fix_script). Covers connecting to the /mcp endpoint, submitting a caption job, polling it, returning the finished download link, and restyling, correcting or stopping a job.
version: 0.1.0
---

# Using the video-caption MCP

The video-caption MCP server exposes one pipeline over six tools: fetch a video from a social
post, transcribe the speech, translate it, burn the translated captions into the picture, and
leave an MP4 behind a signed link. It runs on Cloudflare Workers and takes **minutes**, not
seconds.

Every `submit_job` call starts a new paid run. Treat it as spending money.

## Connecting

This plugin ships the server in its `.mcp.json`, so connecting is a matter of two environment
variables in the shell that launches Claude Code:

```bash
export VIDEO_CAPTION_API_KEY=<the Worker's API_KEY secret>
```

The URL defaults to `https://vc.engdawood.com/mcp`, the Worker's custom domain. The
`*.workers.dev` URL keeps working alongside it, so `VIDEO_CAPTION_MCP_URL` can point at
`https://video-caption.engdawood.workers.dev/mcp` to bypass the custom domain.

They are expanded once at launch, so a key set after Claude Code started will not be picked up —
restart the session.

Outside this plugin, add it by hand:

```bash
claude mcp add --transport http video-caption https://<host>/mcp --header "x-api-key: <API_KEY>"
```

Auth fails **closed**: if `API_KEY` is unset on the Worker, every call gets `403 forbidden` rather
than running unauthenticated. `?token=<API_KEY>` on the URL is accepted as a fallback for clients
that cannot send custom headers (ChatGPT); prefer the header, since a query token ends up in logs,
proxies and shell history.

Note that the download links `get_output` mints are built from the Worker's own `API_BASE_URL` var,
*not* from the URL used to reach `/mcp`. If a returned link points at a different host than the one
just called, that var is stale on the deployment — the job itself is fine.

## The tools

| Tool | Call it when | Returns |
|------|--------------|---------|
| `submit_job` | The user wants a video captioned | `{ jobId }` |
| `job_status` | Checking how that job is going | `{ jobId, status, progress?, error? }` |
| `get_output` | Status is `complete` | `{ jobId, ready, url, script?, postText? }` |
| `cancel_job` | The user wants a queued or running job stopped | `{ jobId, cancelled, status }` |
| `restyle_job` | A finished video should look different (font, colour, position, language…) | `{ jobId, mode }` |
| `fix_script` | Specific caption lines should be reworded or removed | `{ jobId, mode, updated, deleted, missed }` |

The first three run in that order. Never re-call `submit_job` to check on a job — that starts a
second run. Pass an `idempotencyKey` so a retried call cannot: the same key returns the job it
already started.

## submit_job

```json
{
  "sourceUrl": "https://www.tiktok.com/@user/video/123",
  "settings": { "targetLang": "ar", "font": "almarai" }
}
```

**`sourceUrl`** — a public *post* URL on TikTok, Instagram, YouTube, X, Facebook or Threads. A
direct `.mp4`/CDN file link is not accepted: the URL goes through the same resolver a Telegram link
does. If the user pastes a file link, ask for the post it came from.

**`callbackUrl`** — optional, `https://` only. Omit it unless the user gives one: `job_status`
reports the same progress to a polling client. When set, every progress and completion event is
also POSTed there as JSON. A failed POST is logged and swallowed, so a callback endpoint that does
not exist does not break the run. Never invent a URL on someone else's domain.

Callback bodies all carry `jobId`:

| Event | Body | Meaning |
|-------|------|---------|
| `progress` | `{ event, message }` | Stage narration |
| `completed` | `{ event, message, downloadUrl }` | Done. That URL is the *unsigned* `/api/jobs/{id}/output` and needs `x-api-key` — use `get_output` for a link a person can open |
| `failed` | `{ event, error }` | The run failed |
| `stopped` | `{ event, message }` | Ended with no video (e.g. no speech found) |

Every callback is signed: `x-signature: sha256=<hex>` is HMAC-SHA256 with the Worker's `API_KEY`
over `` `${x-signature-timestamp}.${rawBody}` ``. Verify it against the raw body before trusting a
callback, and reject a timestamp more than a few minutes old.

**`idempotencyKey`** — optional, up to 200 characters. Use a fresh random value per user request.
Resending the same key returns the first job's `jobId` whatever its state, so a *failed* job is
retried with a new key.

**`settings`** — name only the fields that should differ from the deployed defaults; everything else
is filled in server-side. See `references/settings.md` for every field and value.

## Polling

After submitting, wait and call `job_status`. A typical job is a few minutes — poll roughly every
30 seconds, not in a tight loop.

`status` is one of `queued`, `running`, `paused`, `waiting`, `waitingForPause`, `complete`,
`errored`, `terminated`, `unknown`. Only `complete` means a video exists. `errored` carries `error`
with the reason.

`progress` is the latest stage line — `⏳ Downloading from tiktok…`, `⏳ Transcribing… (2/5)`,
`⏳ Burning captions into the video…`, `✅ Done.` It is read from KV, so it can lag a few seconds
behind the run. A job that is `complete` with no video (no speech found, too long) says why here.

## Getting the video

`get_output` returns `{ jobId, ready, url, script, postText }`.

- `ready: false` means this job has not finished its video yet. **The `url` is returned anyway** —
  only hand it over once `ready` is true.
- The URL is HMAC-signed and valid for **24 hours**. It opens directly in a browser with no
  credential, so hand it to the user as a link.
- Never try to download and inline the MP4. It is tens of megabytes; the tool returns a link for
  exactly that reason.
- R2 expires the object after two days regardless of the signature.
- `script` is the captions as SRT: each cue's original line (🗣) above its translation (💬). It
  comes with every call, so show it when the user wants to read or check the captions. It is absent
  once the job's assets have expired.
- `postText` is a ready-to-paste description for publishing the video, keyed by language code
  (`POST_TEXT_LANGUAGES` on the Worker, `ar,en` by default). It is written once during the job,
  from the original transcript, by the model `settings.writer` names — so repeated calls return the
  same text. Absent when the video has too little speech or the writer failed; the video is
  delivered either way.

## Changing a finished video

`restyle_job` and `fix_script` re-burn a video the client already has. Each starts a paid run with a
**new `jobId`** — poll `job_status` with it, then call `get_output` with it. The new burn replaces the
previous download; `get_output` on either id returns the latest one.

- **`restyle_job({ jobId, settings })`** — name only the fields to change. The depth is picked for
  you: styling is one encode (`restyle`), a new `targetLang` or `translator` translates again
  (`retranslate`), and only `stt` or `sourceLang` reads the speech again (`retranscribe`). Naming
  nothing that differs is rejected.
- **`fix_script({ jobId, corrections })`** — each correction is
  `{ start: "00:00:12,400", text: "…" }` or `{ start, remove: true }`, with `start` copied from
  `get_output`'s script (matched within 0.6 s). The text is saved into the stored script, then the
  video is re-burned with its current look. Timestamps that match nothing come back in `missed`.
  Removing every line is rejected.
- **`cancel_job({ jobId })`** — stops a run still in progress. A first run's files are deleted with
  it; a restyle or fix run keeps the previously delivered video.

Both re-runs need a job that finished after this feature was deployed — it is what records the
settings the video was made with. Otherwise they return "that job has no delivered video to change".

## What gets a submission rejected

- **`review: "on"` or `preview: "on"`** — rejected outright. Both pause the run on a Telegram card
  that does not exist over MCP. Omit them, or set `"off"`.
- **`confirm`** — accepted but inert. It gates the Telegram start card only; over MCP the job starts
  immediately either way.
- **An off-menu value** — `settings.<field>: "x" is not one of the options this bot offers`.
- **Capacity** — `429`, "the API is at capacity right now — try again shortly". Wait and resubmit;
  no job was created.

## The one setting trap worth knowing up front

Font coverage is a language decision, not a style one. `aljazeera` and `thmanyah` are **Arabic-only**
and are missing letters Urdu needs (ٹ ڈ ڑ ں ے); `thmanyah` also misses Persian's گ ک ی ژ ہ. For
`targetLang: "ur"` or `"fa"`, pick `noto`, `almarai` or `cairo`. A missing glyph renders as a box or
a blank gap in the burned video — there is no error.

## Additional resources

- **`references/settings.md`** — every settings field, its values, and the deployed defaults.
- **`references/troubleshooting.md`** — error strings and status values mapped to causes and fixes.
