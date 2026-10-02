# The `settings` object

Every field is optional. Send **only what should differ** from the deployed defaults — the server
merges the rest in. An unrecognised value is rejected at submission with
`settings.<field>: "x" is not one of the options this bot offers`.

The MCP `tools/list` response advertises these same values, generated from the server's own menus,
so it is the authority if this file and the live schema ever disagree.

## Quick reference

| Field | Values | Deployed default |
|-------|--------|------------------|
| `targetLang` | `ar` `en` `es` `fr` `hi` `ur` `fa` `tr` `ru` `pt` | `ar` |
| `sourceLang` | `auto` `en` `ar` `es` `fr` `hi` `ur` `fa` `tr` `ru` | `en` |
| `preset` | `clean` `hormozi` `cinematic` `youtube` `naskh` | `clean` |
| `font` | `aljazeera` `thmanyah` `noto` `almarai` `cairo` `dubai` `frutiger` `neosans` `arial` `times` | `aljazeera` |
| `size` | `xsmall` `small` `medium` `large` `xlarge` | `medium` |
| `color` | `preset` `white` `yellow` `green` `cyan` `black` | `preset` |
| `background` | `preset` `none` `box` `solid` `plain` `shadow` `thin` `heavy` `outlineShadow` `solidShadow` | `preset` |
| `position` | see below | `bottom` |
| `chars` | `auto` `28` `36` `42` `52` `64` | `42` |
| `stt` | `groq` `mistral` `workers-ai` | `groq` |
| `translator` | `llama70b` `scout` `m2m100` `riva` | `llama70b` |
| `review` | `off` only | `off` |
| `preview` | `off` only | `off` |
| `confirm` | `on` `off` — inert over MCP | `on` |

## Language and font

`sourceLang` is the spoken language. `auto` lets the transcriber detect it — safe, and the right
answer when the user has not said what the video is in.

**Font choice is a coverage decision before it is a style one.**

| Font | Covers | Bold |
|------|--------|------|
| `aljazeera` | Arabic only — breaks Urdu | yes |
| `thmanyah` | Arabic only — breaks Urdu and Persian | no |
| `noto` (Noto Naskh Arabic) | Arabic + both supplements — safe for `ar` `ur` `fa` | no |
| `almarai` | Same coverage as Noto, real bold | yes |
| `cairo` | Same coverage as Noto, real bold | yes |
| `dubai` | Arabic | no |
| `frutiger` | Arabic, commercially licensed | yes |
| `neosans` | Arabic, commercially licensed | no |
| `arial` | Latin, Greek, Cyrillic — breaks `ar` `ur` `fa` | yes |
| `times` | Latin, Greek, Cyrillic — breaks `ar` `ur` `fa` | yes |

For `targetLang: "ur"` or `"fa"`, use `noto`, `almarai` or `cairo`. A glyph the font does not carry
is drawn as a box or a blank gap in the finished video, silently — nothing errors.

`arial` and `times` are the Arial and Times New Roman looks (shipped as their open metric-compatible
twins, Arimo and Tinos), for Latin-script captions.

## Style

`preset` sets the overall look; `color` and `background` override parts of it — and each accepts
`preset` to leave the style's own choice alone, which is how 🎨 Hormozi keeps its yellow text.

- `clean` — white text, outlined
- `hormozi` — yellow on black, social-video style
- `cinematic` — heavy outline
- `youtube` — boxed
- `naskh` — classical, for Arabic

`size` percentages are relative to `medium`: `xsmall` 55%, `small` 70%, `medium` 100%, `large` 150%,
`xlarge` 200%.

`background`: `preset` keeps whatever the preset chose. The rest override it — `plain` and
`shadow` put the text straight on the footage with no outline at all (`shadow` adds a drop shadow
instead), `none` keeps an outline only, `thin` `heavy` `outlineShadow` are outline treatments, and
`box` `solid` `solidShadow` put a box behind the text — translucent, opaque, and opaque with a
drop shadow.

## Position

Nine-cell grid plus raised variants that lift captions clear of the player chrome social apps draw
over a video:

`bottom` `center` `top` · `bottomLeft` `bottomRight` · `middleLeft` `middleRight` · `topLeft`
`topRight` · `lowerThird` (18% up) · `upperThird` (18% down) · `lowerMiddle` (27% up) ·
`belowCentre` · `aboveBottom`

For vertical social video, `lowerThird` or `aboveBottom` usually reads better than `bottom`, which
can sit under the app's own UI.

## Line length

`chars` caps a caption line before it is split into another cue.

**`auto` is not a number.** It is resolved per video from the frame size and the font size the
captions are drawn at, and it only ever shortens — the ceiling is the 42-character broadcast norm.
Prefer it: a fixed `42` on a 9:16 video (which most uploads are) is too wide for the frame, and
libass *wraps* rather than clips, stacking every cue into two or three lines over the picture.
`auto` also enables a reading-rate cap that splits a line which would otherwise flash full-width for
half a second.

## Transcriber and translator

`stt` names which provider is tried **first**, not the only one — the rest follow as fallbacks, so an
outage rolls over instead of failing the job.

| `translator` | Model | Notes |
|--------------|-------|-------|
| `llama70b` | Llama 3.3 70B | Most accurate; the default |
| `scout` | Llama 4 Scout | Faster |
| `m2m100` | M2M100 1.2B | Literal, cheapest — no context prompting, so weakest on sentences |
| `riva` | NVIDIA Riva 4B | Arabic-tuned; needs the Worker's NVIDIA key |

## Fields that do nothing useful over MCP

- `review: "on"` — **rejected**. It pauses the run on a Telegram card to show the script first.
- `preview: "on"` — **rejected**. Same card, with a burned frame.
- `confirm` — accepted and ignored. It gates the Telegram settings card before a run starts; an MCP
  job has no card to show.
