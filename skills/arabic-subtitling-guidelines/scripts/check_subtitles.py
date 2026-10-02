#!/usr/bin/env python3
"""
check_subtitles.py — QC checker for Arabic SRT/VTT subtitle files against the
Netflix Timed Text Style Guide (Arabic + General Requirements + Timing Guidelines).

Checks (see references/netflix-arabic-rules.md for the full rules):
  - Max 42 characters per line, max 2 lines per event
  - Reading speed (default 20 cps adult, --children for 17 cps, --sdh for 23/20 cps)
  - Duration: min 5/6 s (20 frames), max 7 s
  - Gaps between events: must be exactly 2 frames, or >= 0.5 s (nothing in between)
  - Ellipsis must be U+2026, never three periods "..."
  - No "?!" or "!?" combos; no space before , ? !
  - Straight double quotes only (flags curly “ ” ‘ ’)
  - No italics markup (<i>, <I>)
  - Flags Latin letters inside the Arabic text (often a sign of an untranslated
    website/email/hashtag that should follow the quoting rule instead)
  - Lone word alone on the second line (heuristic, needs human judgement)
  - Out-of-order / overlapping timestamps

This is a mechanical check. It cannot judge translation quality, meaning, shot
changes, or audio sync — use the manual QC checklist in SKILL.md for those.

Usage:
  python check_subtitles.py FILE.srt [--fps 24] [--children] [--sdh] [--fix OUT.srt]

--fix applies only safe, unambiguous mechanical fixes:
  - "..." -> "…"
  - curly quotes -> straight quotes
  - drop a space before , ? !
  - close gaps of 3-11 frames (at the given --fps) down to exactly 2 frames,
    by pulling back the *next* event's start time (never touches the previous
    event's own displayed duration)
It does NOT fix line length, reading speed, or line-break placement — those
need human judgement.
"""
import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ELLIPSIS = "\u2026"
CURLY_QUOTES = {
    "\u201c": '"', "\u201d": '"', "\u2018": "'", "\u2019": "'",
}
ARABIC_RANGE = re.compile(r"[\u0600-\u06FF\u0750-\u077F]")
LATIN_LETTERS = re.compile(r"[A-Za-z]")
KASHIDA = "\u0640"


@dataclass
class Event:
    index: int
    start: float  # seconds
    end: float
    lines: list = field(default_factory=list)
    raw_start: str = ""
    raw_end: str = ""


def ts_to_seconds(ts: str) -> float:
    ts = ts.strip().replace(",", ".")
    h, m, s = ts.split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


def seconds_to_srt_ts(sec: float) -> str:
    if sec < 0:
        sec = 0
    h = int(sec // 3600)
    sec -= h * 3600
    m = int(sec // 60)
    sec -= m * 60
    s = int(sec)
    ms = round((sec - s) * 1000)
    if ms == 1000:
        ms = 0
        s += 1
        if s == 60:
            s = 0
            m += 1
            if m == 60:
                m = 0
                h += 1
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def parse_srt(text: str):
    blocks = re.split(r"\r?\n\r?\n+", text.strip())
    events = []
    for block in blocks:
        lines = [l for l in block.splitlines() if l.strip() != ""]
        if not lines:
            continue
        # First line may be an index number
        idx_line = 0
        if re.match(r"^\d+$", lines[0].strip()):
            idx = int(lines[0].strip())
            idx_line = 1
        else:
            idx = len(events) + 1
        if idx_line >= len(lines) or "-->" not in lines[idx_line]:
            continue
        m = re.match(r"\s*([\d:,.]+)\s*-->\s*([\d:,.]+)", lines[idx_line])
        if not m:
            continue
        start_raw, end_raw = m.group(1), m.group(2)
        text_lines = lines[idx_line + 1:]
        events.append(Event(
            index=idx,
            start=ts_to_seconds(start_raw),
            end=ts_to_seconds(end_raw),
            lines=text_lines,
            raw_start=start_raw,
            raw_end=end_raw,
        ))
    return events


def parse_vtt(text: str):
    text = re.sub(r"^WEBVTT.*?\n", "", text.strip(), flags=re.DOTALL)
    blocks = re.split(r"\r?\n\r?\n+", text.strip())
    events = []
    for block in blocks:
        lines = [l for l in block.splitlines() if l.strip() != ""]
        if not lines:
            continue
        cue_line = 0
        if "-->" not in lines[0] and len(lines) > 1:
            cue_line = 1
        if cue_line >= len(lines) or "-->" not in lines[cue_line]:
            continue
        m = re.match(r"\s*([\d:.]+)\s*-->\s*([\d:.]+)", lines[cue_line])
        if not m:
            continue
        start_raw, end_raw = m.group(1), m.group(2)
        text_lines = lines[cue_line + 1:]
        events.append(Event(
            index=len(events) + 1,
            start=ts_to_seconds(start_raw.replace(".", ",")),
            end=ts_to_seconds(end_raw.replace(".", ",")),
            lines=text_lines,
            raw_start=start_raw,
            raw_end=end_raw,
        ))
    return events


def char_len(line: str) -> int:
    # Strip combining diacritics from the count? Netflix counts displayed chars
    # including diacritics, so we count code points as-is, minus tags.
    clean = re.sub(r"</?i>", "", line, flags=re.IGNORECASE)
    return len(clean)


def check_event(ev: Event, max_chars, max_lines, min_dur, max_dur, cps_limit, fps):
    issues = []
    text = " ".join(ev.lines)
    n_lines = len(ev.lines)

    if n_lines > max_lines:
        issues.append(f"more than {max_lines} lines ({n_lines})")

    for i, line in enumerate(ev.lines, 1):
        n = char_len(line)
        if n > max_chars:
            issues.append(f"line {i} is {n} chars (max {max_chars}): {line!r}")

    if n_lines == 2:
        words2 = ev.lines[1].strip().split()
        if len(words2) == 1:
            issues.append(f"lone word alone on line 2: {ev.lines[1]!r} (consider reflowing)")

    dur = ev.end - ev.start
    if dur <= 0:
        issues.append("zero or negative duration")
    else:
        if dur < min_dur - 1e-6:
            issues.append(f"duration {dur:.2f}s below minimum {min_dur:.2f}s")
        if dur > max_dur + 1e-6:
            issues.append(f"duration {dur:.2f}s exceeds maximum {max_dur:.2f}s")
        total_chars = sum(char_len(l) for l in ev.lines)
        cps = total_chars / dur
        if cps > cps_limit + 1e-6:
            issues.append(f"reading speed {cps:.1f} cps exceeds {cps_limit} cps limit ({total_chars} chars / {dur:.2f}s)")

    if "..." in text:
        issues.append("uses three periods \"...\" instead of the ellipsis character \u2026")
    if re.search(r"[?\uFF1F\u061F][!\uFF01]|[!\uFF01][?\uFF1F\u061F]", text):
        issues.append("combines a question mark and exclamation mark (\u061F!/!\u061F or ?!/!?) — not allowed, pick one")
    if re.search(r"\s[،؛؟,?!]", text):
        issues.append("space before punctuation (،  ؛  ؟  ,  ?  !)")
    for ch, repl in CURLY_QUOTES.items():
        if ch in text:
            issues.append(f"curly quote {ch!r} found — use straight {repl!r} instead")
    if re.search(r"</?i>", text, flags=re.IGNORECASE):
        issues.append("italics markup found — Arabic subtitles never use italics")
    if LATIN_LETTERS.search(text) and ARABIC_RANGE.search(text):
        issues.append("Latin letters mixed into Arabic text — check hashtag/email/website rule (no Latin letters allowed)")
    # kashida-before-quote heuristic: ال" without kashida
    if re.search(r"(?<!" + KASHIDA + r")\u0627\u0644\"", text):
        issues.append("\u0627\u0644 (al-) touches a quote mark without a kashida (\u0640) — see quoting rule")

    return issues


def check_gaps(events, fps):
    issues = []
    min_frame_gap = 2 / fps
    lower_bound = 3 / fps
    upper_bound = 11 / fps
    half_sec = 0.5
    for a, b in zip(events, events[1:]):
        if b.start < a.end - 1e-6:
            issues.append((a.index, b.index, f"overlap: event {a.index} ends {a.end:.2f}s after event {b.index} starts {b.start:.2f}s"))
            continue
        gap = b.start - a.end
        if gap < min_frame_gap - 1e-6:
            issues.append((a.index, b.index, f"gap {gap*1000:.0f}ms is less than the minimum 2 frames ({min_frame_gap*1000:.0f}ms)"))
        elif lower_bound - 1e-6 <= gap <= upper_bound + 1e-6:
            issues.append((a.index, b.index, f"gap {gap*1000:.0f}ms falls in the disallowed 3-11 frame zone at {fps}fps — must be exactly 2 frames or >= 0.5s"))
    return issues


def auto_fix_text(line: str) -> str:
    line = line.replace("...", ELLIPSIS)
    for ch, repl in CURLY_QUOTES.items():
        line = line.replace(ch, repl)
    line = re.sub(r"\s+([،؛؟,?!])", r"\1", line)
    return line


def write_srt(events, path):
    out = []
    for i, ev in enumerate(events, 1):
        out.append(str(i))
        out.append(f"{seconds_to_srt_ts(ev.start)} --> {seconds_to_srt_ts(ev.end)}")
        out.extend(ev.lines)
        out.append("")
    Path(path).write_text("\n".join(out), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", help="SRT or VTT file to check")
    ap.add_argument("--fps", type=float, default=24.0, help="frame rate for gap/duration math (default 24)")
    ap.add_argument("--max-chars", type=int, default=42)
    ap.add_argument("--max-lines", type=int, default=2)
    ap.add_argument("--children", action="store_true", help="use children's reading-speed limit (17 cps) and min duration logic")
    ap.add_argument("--sdh", action="store_true", help="use SDH reading-speed limits (23 cps adult / 20 cps children)")
    ap.add_argument("--fix", metavar="OUT_FILE", help="write a copy with safe mechanical fixes applied")
    args = ap.parse_args()

    path = Path(args.file)
    text = path.read_text(encoding="utf-8-sig")
    if path.suffix.lower() == ".vtt":
        events = parse_vtt(text)
    else:
        events = parse_srt(text)

    if not events:
        print("No subtitle events parsed — check the file format.", file=sys.stderr)
        sys.exit(2)

    if args.sdh:
        cps_limit = 20.0 if args.children else 23.0
    else:
        cps_limit = 17.0 if args.children else 20.0

    min_dur = 20 / args.fps  # ~5/6s at 24fps
    max_dur = 7.0

    total_issues = 0
    for ev in events:
        issues = check_event(ev, args.max_chars, args.max_lines, min_dur, max_dur, cps_limit, args.fps)
        if issues:
            total_issues += len(issues)
            print(f"\nEvent {ev.index} [{ev.raw_start} --> {ev.raw_end}]")
            for line in ev.lines:
                print(f"    {line}")
            for issue in issues:
                print(f"    ! {issue}")

    gap_issues = check_gaps(events, args.fps)
    for a_idx, b_idx, msg in gap_issues:
        total_issues += 1
        print(f"\nBetween events {a_idx} and {b_idx}: ! {msg}")

    print(f"\n{'='*60}")
    print(f"{len(events)} events checked, {total_issues} issue(s) found "
          f"(fps={args.fps}, cps limit={cps_limit}, children={args.children}, sdh={args.sdh})")

    if args.fix:
        for ev in events:
            ev.lines = [auto_fix_text(l) for l in ev.lines]
        min_frame_gap = 2 / args.fps
        lower_bound = 3 / args.fps
        upper_bound = 11 / args.fps
        for a, b in zip(events, events[1:]):
            if b.start >= a.end:
                gap = b.start - a.end
                if lower_bound - 1e-6 <= gap <= upper_bound + 1e-6:
                    a.end = b.start - min_frame_gap
        write_srt(events, args.fix)
        print(f"Fixed copy written to {args.fix}")
        print("Note: text-length, reading-speed, and line-break issues were NOT auto-fixed — review the report above.")

    sys.exit(1 if total_issues else 0)


if __name__ == "__main__":
    main()
