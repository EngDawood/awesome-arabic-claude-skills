# Troubleshooting

## Connection

| Symptom | Cause | Fix |
|---------|-------|-----|
| `403 forbidden` on every call | `API_KEY` is unset on the Worker, or the key sent does not match | The `/mcp` route fails **closed** — an unset `API_KEY` disables it entirely rather than opening it. Set the secret with `npx wrangler secret put API_KEY`, then send the same value |
| Tools never appear | The server is configured but the key is missing from the environment | `VIDEO_CAPTION_API_KEY` must be set in the shell that starts Claude Code; `.mcp.json` expands it at launch, not per call |
| `404 not found` | Wrong path | The endpoint is `/mcp` exactly. `/api/jobs` is the REST twin, not the MCP one |

## submit_job errors

| Message | Cause |
|---------|-------|
| `sourceUrl is required` | Field missing or empty |
| `callbackUrl must be a string` | A non-string value. Omit the field instead |
| `callbackUrl must be https://` | An `http://` URL. TLS only |
| `callbackUrl must be a valid URL` | Unparseable string |
| `settings.<field>: "x" is not one of the options this bot offers` | Off-menu value — check `references/settings.md` |
| `settings.review "on" is not supported over the API yet — set it to "off"` | The script-review gate pauses on a Telegram card that does not exist over MCP |
| `settings.preview "on" is not supported over the API yet — set it to "off"` | Same, for the burned-frame gate |
| `the API is at capacity right now — try again shortly` (429) | Concurrency slots are full. **No job was created** — wait and resubmit |
| `the workflow binding is not configured` (500) | Deployment problem: `CAPTION_WORKFLOW` is not bound. Not a client-side fix |

A rejected submission costs nothing and produces no `jobId`.

## Job states

`job_status` returns one of:

| Status | Meaning | Do |
|--------|---------|----|
| `queued` | Accepted, not started | Wait |
| `running` | Working | Wait — a job is minutes |
| `paused`, `waiting`, `waitingForPause` | Internal workflow states | Wait; these resolve on their own |
| `complete` | Finished | Call `get_output` |
| `errored` | Failed — `error` says why | Report the reason; resubmitting repeats the cost |
| `terminated` | Cancelled or killed | Resubmit if the user still wants it |
| `unknown` | State could not be read | Retry once before assuming failure |

`no such job` (404) means the `jobId` does not exist — usually a typo, or a jobId from a run that
was never created because submission was rejected.

## Output problems

**`ready: false`** — the MP4 is not in R2. Either the job has not finished, the video was already
fetched and cleaned up, or it aged out. The `url` field is returned regardless and will 404; check
`ready` before using it.

**The signed link 404s** — it expired (24 hours), or R2's lifecycle rule dropped the object (two
days). Neither can be recovered: resubmit the job.

**The `downloadUrl` in a `completed` callback returns 403** — that URL is the unsigned
`/api/jobs/{id}/output` and needs an `x-api-key` header. For a link a person can open in a browser,
call `get_output` instead.

## Problems in the finished video

These do not error — the video comes back wrong. All are settings problems:

| Symptom | Cause | Fix |
|---------|-------|-----|
| Boxes or blank gaps inside words | The font has no glyph for those letters | Arabic-only fonts (`aljazeera`, `thmanyah`) break Urdu and Persian — use `noto`, `almarai` or `cairo` |
| Latin-looking garbage instead of Arabic | The Worker's `SUBTITLE_FONT` is not a real internal family name, so libass fell back silently | Server-side: check `GET /debug/fonts?secret=…` |
| Every cue stacked into two or three lines over the picture | A fixed `chars` value too wide for a vertical frame; libass wraps rather than clips | Use `chars: "auto"` |
| Captions hidden under the app's UI | `position: "bottom"` on vertical video | Use `lowerThird` or `aboveBottom` |
| Translation is literal or loses the thread | `translator: "m2m100"` gets no context prompting | Use `llama70b`, or `riva` for Arabic |

## Job ended with no video

A `stopped` callback (or a run that completes with nothing to download) usually means no speech was
found in the source. Check the video actually has spoken audio before resubmitting with different
settings — no settings change will fix silence.
