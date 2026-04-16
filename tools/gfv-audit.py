#!/usr/bin/env python3
import os
import sys
import json
from pathlib import Path

def get_claude_logs_dir():
    repo_dir = str(Path(__file__).parent.parent.absolute())
    escaped_cwd = repo_dir.replace("/", "-")
    return Path(os.environ.get("GFV_CEO_BRAIN", Path.home() / "ceo-brain")) / ".core" / "projects" / escaped_cwd

def main():
    logs_dir = get_claude_logs_dir()
    if not logs_dir.exists() or not logs_dir.is_dir():
        print(f"No log directory found at {logs_dir}")
        sys.exit(1)

    print("🔍 Scanning recent Claude Code JSONL transcripts for execution history...\n")

    logs = sorted(logs_dir.glob("*.jsonl"), key=os.path.getmtime, reverse=True)[:5]
    
    for logfile in logs:
        print(f"--- Session Log: {logfile.name} ---")
        try:
            with open(logfile, "r", encoding="utf-8") as f:
                for line in f:
                    if not line.strip():
                        continue
                    try:
                        record = json.loads(line)
                        if record.get("type") == "assistant" and record.get("message"):
                            msg = record["message"]
                            content = msg.get("content", [])
                            if isinstance(content, list):
                                for item in content:
                                    if item.get("type") == "tool_use" and item.get("name") == "Bash":
                                        ts = record.get("timestamp", "UNKNOWN TIME")
                                        command = item.get("input", {}).get("command", "")
                                        print(f"[{ts}] \n$ {command}\n")
                    except json.JSONDecodeError:
                        continue
        except Exception as e:
            pass
        print("")

if __name__ == "__main__":
    main()
