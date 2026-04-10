#!/usr/bin/env python3
"""
Growth by Design — Session Start Hook
Loads company brain context at the beginning of every Claude Code session.

Install: Copy to ~/.claude/hooks/session-start.py
Trigger: SessionStart event
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime


def main():
    brain_dir = Path.home() / "brain"

    if not brain_dir.exists():
        print("⚠️  No brain directory found. Run bootstrap.sh first.", file=sys.stderr)
        return

    context_parts = []
    context_parts.append(f"# Session Context — {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")

    # Load voice model summary
    voice_model = brain_dir / "voice-model.md"
    if voice_model.exists():
        content = voice_model.read_text()
        if len(content) > 200:
            context_parts.append("✅ Voice model loaded (~/brain/voice-model.md)")
        else:
            context_parts.append("⚠️  Voice model exists but looks empty — fill it in!")
    else:
        context_parts.append("❌ No voice model found — copy templates/voice-model.md to ~/brain/")

    # Load pipeline state
    pipeline = brain_dir / "pipeline.md"
    if pipeline.exists():
        content = pipeline.read_text()
        context_parts.append(f"✅ Pipeline state loaded ({len(content.splitlines())} lines)")
    else:
        context_parts.append("⚠️  No pipeline.md — create one with current deal state")

    # Load recent learnings (last 20 lines)
    learnings = brain_dir / "learnings.md"
    if learnings.exists():
        lines = learnings.read_text().splitlines()
        if len(lines) > 5:
            context_parts.append(f"✅ Learnings log has {len(lines)} entries")
            context_parts.append("\nRecent learnings:")
            for line in lines[-10:]:
                if line.strip():
                    context_parts.append(f"  {line}")

    # Check for meeting briefs
    meetings_dir = brain_dir / "meetings"
    if meetings_dir.exists():
        briefs = sorted(meetings_dir.glob("*.md"), reverse=True)[:3]
        if briefs:
            context_parts.append(f"\n📋 Recent meeting briefs: {len(briefs)}")
            for brief in briefs:
                context_parts.append(f"  - {brief.name}")

    # Output context
    output = "\n".join(context_parts)
    print(output)

    # Write to a temp file for Claude Code to pick up
    context_file = brain_dir / ".last-session-context.md"
    context_file.write_text(output)


if __name__ == "__main__":
    main()
