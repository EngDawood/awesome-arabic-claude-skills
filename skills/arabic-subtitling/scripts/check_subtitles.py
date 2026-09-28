#!/usr/bin/env python3
"""
Arabic Subtitles Quality Control (QC) Checker and Fixer
Validates SRT and WebVTT subtitle files against industry standards (Netflix Timed Text Style Guide).
"""

import argparse
import math
import os
import re
import sys
from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass
class SubtitleEvent:
    index: int
    start_seconds: float
    end_seconds: float
    raw_lines: List[str]
    clean_lines: List[str]

    @property
    def duration(self) -> float:
        return max(0.0, self.end_seconds - self.start_seconds)

    @property
    def total_characters(self) -> int:
        return sum(len(line) for line in self.clean_lines)

    @property
    def cps(self) -> float:
        if self.duration <= 0:
            return float("inf")
        return self.total_characters / self.duration


@dataclass
class QCError:
    event_index: int
    timestamp_str: str
    category: str
    message: str
    is_warning: bool = False


def parse_timestamp(ts: str) -> float:
    """Parses timestamp in HH:MM:SS,mmm or HH:MM:SS.mmm or MM:SS.mmm format."""
    ts = ts.strip().replace(",", ".")
    parts = ts.split(":")
    if len(parts) == 3:
        h, m, s = parts
        return int(h) * 3600 + int(m) * 60 + float(s)
    elif len(parts) == 2:
        m, s = parts
        return int(m) * 60 + float(s)
    else:
        return float(ts)


def format_timestamp_srt(seconds: float) -> str:
    """Formats seconds into HH:MM:SS,mmm."""
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int(round((seconds - int(seconds)) * 1000))
    if ms >= 1000:
        s += 1
        ms -= 1000
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def format_timestamp_vtt(seconds: float) -> str:
    """Formats seconds into HH:MM:SS.mmm."""
    return format_timestamp_srt(seconds).replace(",", ".")


def strip_formatting(text: str) -> str:
    """Removes HTML/styling tags from text for accurate character counting."""
    return re.sub(r"<[^>]+>", "", text).strip()


def has_arabic(text: str) -> bool:
    """Checks if string contains Arabic characters."""
    return bool(re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]", text))


def parse_srt(content: str) -> List[SubtitleEvent]:
    events = []
    blocks = re.split(r"\n\s*\n", content.strip())
    
    for block in blocks:
        lines = [line.rstrip("\r") for line in block.strip().split("\n") if line.strip()]
        if not lines:
            continue
        
        # Line 0: optional index
        idx = 0
        time_line_idx = 0
        if lines[0].strip().isdigit() and len(lines) > 1:
            idx = int(lines[0].strip())
            time_line_idx = 1
        else:
            idx = len(events) + 1

        if time_line_idx >= len(lines):
            continue

        match = re.search(r"(\d+:\d+:\d+[\.,]\d+)\s*-->\s*(\d+:\d+:\d+[\.,]\d+)", lines[time_line_idx])
        if not match:
            continue

        start_sec = parse_timestamp(match.group(1))
        end_sec = parse_timestamp(match.group(2))
        raw_text_lines = lines[time_line_idx + 1 :]
        clean_text_lines = [strip_formatting(l) for l in raw_text_lines]

        events.append(
            SubtitleEvent(
                index=idx,
                start_seconds=start_sec,
                end_seconds=end_sec,
                raw_lines=raw_text_lines,
                clean_lines=clean_text_lines,
            )
        )
    return events


def parse_vtt(content: str) -> List[SubtitleEvent]:
    events = []
    # Drop WEBVTT header
    content = re.sub(r"^WEBVTT.*?\n", "", content.strip(), flags=re.IGNORECASE)
    blocks = re.split(r"\n\s*\n", content.strip())

    for idx_counter, block in enumerate(blocks, start=1):
        lines = [line.rstrip("\r") for line in block.strip().split("\n") if line.strip()]
        if not lines:
            continue

        time_line_idx = -1
        for i, line in enumerate(lines):
            if "-->" in line:
                time_line_idx = i
                break

        if time_line_idx == -1:
            continue

        match = re.search(r"(\d+:?\d+:\d+[\.,]\d+)\s*-->\s*(\d+:?\d+:\d+[\.,]\d+)", lines[time_line_idx])
        if not match:
            continue

        start_sec = parse_timestamp(match.group(1))
        end_sec = parse_timestamp(match.group(2))
        raw_text_lines = lines[time_line_idx + 1 :]
        clean_text_lines = [strip_formatting(l) for l in raw_text_lines]

        events.append(
            SubtitleEvent(
                index=idx_counter,
                start_seconds=start_sec,
                end_seconds=end_sec,
                raw_lines=raw_text_lines,
                clean_lines=clean_text_lines,
            )
        )
    return events


def check_subtitles(
    events: List[SubtitleEvent],
    fps: float = 24.0,
    max_cpr: int = 42,
    max_lines: int = 2,
    min_duration: float = 5.0 / 6.0,  # 0.833s (~20 frames at 24fps)
    max_duration: float = 7.0,
    max_cps: float = 20.0,
    min_gap_frames: int = 2,
) -> List[QCError]:
    errors = []
    frame_duration = 1.0 / fps
    min_gap_sec = min_gap_frames * frame_duration
    chain_gap_max_sec = 11.0 * frame_duration  # Between 3 and 11 frames

    for i, ev in enumerate(events):
        ts_str = f"{format_timestamp_srt(ev.start_seconds)} --> {format_timestamp_srt(ev.end_seconds)}"

        # 1. Line count check
        if len(ev.clean_lines) > max_lines:
            errors.append(
                QCError(
                    event_index=ev.index,
                    timestamp_str=ts_str,
                    category="Line Count",
                    message=f"Event has {len(ev.clean_lines)} lines (maximum allowed is {max_lines}).",
                )
            )

        # 2. Characters Per Row (CPR) check
        for line_num, line in enumerate(ev.clean_lines, start=1):
            char_count = len(line)
            if char_count > max_cpr:
                errors.append(
                    QCError(
                        event_index=ev.index,
                        timestamp_str=ts_str,
                        category="Line Length",
                        message=f"Line {line_num} exceeds max length: {char_count} chars (max: {max_cpr}) -> \"{line}\"",
                    )
                )

        # 3. Duration check
        if ev.duration < min_duration - 0.01:
            errors.append(
                QCError(
                    event_index=ev.index,
                    timestamp_str=ts_str,
                    category="Duration (Short)",
                    message=f"Duration {ev.duration:.2f}s is less than minimum {min_duration:.2f}s (approx. {int(min_duration*fps)} frames).",
                )
            )
        elif ev.duration > max_duration + 0.01:
            errors.append(
                QCError(
                    event_index=ev.index,
                    timestamp_str=ts_str,
                    category="Duration (Long)",
                    message=f"Duration {ev.duration:.2f}s exceeds maximum {max_duration:.2f}s.",
                )
            )

        # 4. Reading Speed (CPS) check
        if ev.cps > max_cps:
            errors.append(
                QCError(
                    event_index=ev.index,
                    timestamp_str=ts_str,
                    category="Reading Speed",
                    message=f"Reading speed {ev.cps:.1f} CPS exceeds limit of {max_cps:.1f} CPS ({ev.total_characters} chars in {ev.duration:.2f}s).",
                )
            )

        # 5. Gap checks between consecutive events
        if i > 0:
            prev_ev = events[i - 1]
            gap = ev.start_seconds - prev_ev.end_seconds
            if gap < -0.001:
                errors.append(
                    QCError(
                        event_index=ev.index,
                        timestamp_str=ts_str,
                        category="Overlap",
                        message=f"Overlaps with previous event #{prev_ev.index} by {abs(gap):.3f}s.",
                    )
                )
            elif gap < min_gap_sec - 0.001:
                gap_frames = gap * fps
                errors.append(
                    QCError(
                        event_index=ev.index,
                        timestamp_str=ts_str,
                        category="Gap Too Short",
                        message=f"Gap with event #{prev_ev.index} is {gap:.3f}s ({gap_frames:.1f} frames). Minimum is {min_gap_frames} frames ({min_gap_sec:.3f}s).",
                    )
                )
            elif min_gap_sec <= gap <= chain_gap_max_sec:
                gap_frames = gap * fps
                errors.append(
                    QCError(
                        event_index=ev.index,
                        timestamp_str=ts_str,
                        category="Gap Chaining",
                        is_warning=True,
                        message=f"Gap with event #{prev_ev.index} is {gap_frames:.1f} frames (between 3 and 11 frames). Should be chained to 2 frames or $\\ge$ 12 frames.",
                    )
                )

        # 6. Linguistic & Punctuation checks
        full_raw_text = " ".join(ev.raw_lines)
        full_clean_text = " ".join(ev.clean_lines)

        # Check for italics (Forbidden in Arabic)
        if re.search(r"<(?:i|em)>", full_raw_text, re.IGNORECASE):
            errors.append(
                QCError(
                    event_index=ev.index,
                    timestamp_str=ts_str,
                    category="Typography",
                    message="Italics tags <i>/<em> detected. Italics are strictly forbidden in Arabic subtitles.",
                )
            )

        # Check for ASCII 3 periods instead of Unicode ellipsis
        if "..." in full_clean_text:
            errors.append(
                QCError(
                    event_index=ev.index,
                    timestamp_str=ts_str,
                    category="Punctuation",
                    message="ASCII triple dots '...' found. Use dedicated Unicode ellipsis glyph '…' (U+2026).",
                )
            )

        # Check for space before punctuation in Arabic
        if re.search(r"\s+[،؟!:.]", full_clean_text):
            errors.append(
                QCError(
                    event_index=ev.index,
                    timestamp_str=ts_str,
                    category="Punctuation",
                    message="Illegal space before punctuation mark (،, ؟, !, : or .).",
                )
            )

        # Check for double punctuation like ؟! or !?
        if re.search(r"[؟!\.][؟!\.]", full_clean_text):
            # Exclude ellipsis
            cleaned = full_clean_text.replace("...", "").replace("…", "")
            if re.search(r"[؟!\.]{2,}", cleaned):
                errors.append(
                    QCError(
                        event_index=ev.index,
                        timestamp_str=ts_str,
                        category="Punctuation",
                        message="Double punctuation (e.g. '؟!', '!?') detected. Choose one dominant punctuation mark.",
                    )
                )

        # Check for Latin punctuation inside Arabic text
        if has_arabic(full_clean_text):
            if re.search(r"[\u0600-\u06FF]\s*,", full_clean_text):
                errors.append(
                    QCError(
                        event_index=ev.index,
                        timestamp_str=ts_str,
                        category="Punctuation",
                        message="Western comma ',' used in Arabic context. Replace with Arabic comma '،'.",
                    )
                )
            if re.search(r"[\u0600-\u06FF]\s*\?", full_clean_text):
                errors.append(
                    QCError(
                        event_index=ev.index,
                        timestamp_str=ts_str,
                        category="Punctuation",
                        message="Western question mark '?' used in Arabic context. Replace with Arabic question mark '؟'.",
                    )
                )

        # Check orphan word on line 2
        if len(ev.clean_lines) == 2:
            l1, l2 = ev.clean_lines[0].strip(), ev.clean_lines[1].strip()
            l2_words = l2.split()
            if len(l2_words) == 1 and len(l1.split()) > 3:
                errors.append(
                    QCError(
                        event_index=ev.index,
                        timestamp_str=ts_str,
                        category="Layout",
                        is_warning=True,
                        message=f"Orphan word on line 2: \"{l2}\". Re-balance lines to avoid a solitary word.",
                    )
                )

    return errors


def fix_subtitles(events: List[SubtitleEvent]) -> List[SubtitleEvent]:
    """Applies automatic mechanical fixes to subtitles."""
    fixed_events = []

    for ev in events:
        new_raw_lines = []
        for line in ev.raw_lines:
            # Strip italics tags
            l = re.sub(r"</?(?:i|em)>", "", line, flags=re.IGNORECASE)
            
            # Replace triple dots with single Unicode ellipsis U+2026
            l = l.replace("...", "…")

            # Remove spaces before Arabic punctuation
            l = re.sub(r"\s+([،؟!:.\u2026])", r"\1", l)

            # Fix Western punctuation in Arabic text
            if has_arabic(l):
                l = re.sub(r"(?<=[\u0600-\u06FF]),", "،", l)
                l = re.sub(r"(?<=[\u0600-\u06FF])\?", "؟", l)
                l = re.sub(r"(?<=[\u0600-\u06FF]);", "؛", l)

            # Fix double punctuation ?! or !? -> single ? or !
            l = re.sub(r"[\?؟]!", "؟", l)
            l = re.sub(r"![\?؟]", "!", l)

            new_raw_lines.append(l.strip())

        new_clean_lines = [strip_formatting(l) for l in new_raw_lines]
        fixed_events.append(
            SubtitleEvent(
                index=ev.index,
                start_seconds=ev.start_seconds,
                end_seconds=ev.end_seconds,
                raw_lines=new_raw_lines,
                clean_lines=new_clean_lines,
            )
        )
    return fixed_events


def export_srt(events: List[SubtitleEvent], output_path: str):
    with open(output_path, "w", encoding="utf-8") as f:
        for idx, ev in enumerate(events, start=1):
            f.write(f"{idx}\n")
            f.write(f"{format_timestamp_srt(ev.start_seconds)} --> {format_timestamp_srt(ev.end_seconds)}\n")
            for line in ev.raw_lines:
                f.write(f"{line}\n")
            f.write("\n")


def export_vtt(events: List[SubtitleEvent], output_path: str):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("WEBVTT\n\n")
        for idx, ev in enumerate(events, start=1):
            f.write(f"{idx}\n")
            f.write(f"{format_timestamp_vtt(ev.start_seconds)} --> {format_timestamp_vtt(ev.end_seconds)}\n")
            for line in ev.raw_lines:
                f.write(f"{line}\n")
            f.write("\n")


def main():
    parser = argparse.ArgumentParser(
        description="Arabic Subtitles Quality Control (QC) Checker & Fixer (Netflix TTSG Compliance)"
    )
    parser.add_argument("file", help="Path to input subtitle file (.srt or .vtt)")
    parser.add_argument("--fps", type=float, default=24.0, help="Frame rate of video asset (default: 24.0)")
    parser.add_argument("--max-cpr", type=int, default=42, help="Max characters per line (default: 42)")
    parser.add_argument("--max-lines", type=int, default=2, help="Max lines per subtitle event (default: 2)")
    parser.add_argument("--max-cps", type=float, default=20.0, help="Max reading speed in chars/second (default: 20.0)")
    parser.add_argument(
        "--min-duration",
        type=float,
        default=5.0 / 6.0,
        help="Minimum duration in seconds (default: 5/6s = ~0.833s)",
    )
    parser.add_argument(
        "--max-duration", type=float, default=7.0, help="Maximum duration in seconds (default: 7.0s)"
    )
    parser.add_argument(
        "--fix", type=str, default=None, metavar="OUT_FILE", help="Auto-fix mechanical errors and save to new file"
    )
    parser.add_argument("--verbose", action="store_true", help="Print all details even if no errors")

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"Error: File '{args.file}' not found.", file=sys.stderr)
        sys.exit(1)

    with open(args.file, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    is_vtt = args.file.lower().endswith(".vtt") or content.strip().startswith("WEBVTT")
    if is_vtt:
        events = parse_vtt(content)
    else:
        events = parse_srt(content)

    if not events:
        print(f"Warning: No subtitle events could be parsed from '{args.file}'.", file=sys.stderr)
        sys.exit(1)

    print(f"Loaded {len(events)} subtitle events from '{args.file}' (Detected: {'WebVTT' if is_vtt else 'SRT'}).")
    print(f"QC Config: {args.fps} FPS | Max {args.max_cpr} CPR | Max {args.max_lines} Lines | Max {args.max_cps} CPS\n" + "-" * 70)

    errors = check_subtitles(
        events=events,
        fps=args.fps,
        max_cpr=args.max_cpr,
        max_lines=args.max_lines,
        min_duration=args.min_duration,
        max_duration=args.max_duration,
        max_cps=args.max_cps,
    )

    warnings = [e for e in errors if e.is_warning]
    critical_errors = [e for e in errors if not e.is_warning]

    if not errors:
        print("✅ SUCCESS: All subtitles passed QC with zero errors!")
    else:
        print(f"Found {len(critical_errors)} errors and {len(warnings)} warnings across {len(events)} events:\n")
        for err in errors:
            tag = "[WARNING]" if err.is_warning else "[ERROR]"
            print(f"{tag} #{err.event_index} ({err.timestamp_str}) [{err.category}]: {err.message}")

    print("\n" + "=" * 70)
    print(f"SUMMARY: {len(events)} Events | {len(critical_errors)} Errors | {len(warnings)} Warnings")

    if args.fix:
        fixed_events = fix_subtitles(events)
        if args.fix.lower().endswith(".vtt"):
            export_vtt(fixed_events, args.fix)
        else:
            export_srt(fixed_events, args.fix)
        print(f"✨ Auto-fixed mechanical issues and exported to: '{args.fix}'")

    sys.exit(1 if critical_errors else 0)


if __name__ == "__main__":
    main()
