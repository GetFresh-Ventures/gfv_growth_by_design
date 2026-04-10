#!/usr/bin/env bash

# Growth by Design — Bootstrap Script
# Initializes the brain directory and symlinks hooks into Claude Code

set -e

echo "🚀 Initializing Growth by Design kit..."

# Target directories
BRAIN_DIR="$HOME/brain"
CLAUDE_HOOKS_DIR="$HOME/.claude/hooks"
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 1. Create brain structure
echo "📁 Creating ~/brain structure..."
mkdir -p "$BRAIN_DIR/meetings"
mkdir -p "$BRAIN_DIR/campaigns"
mkdir -p "$BRAIN_DIR/weekly"

# 2. Copy templates if files don't exist
echo "📄 Setting up templates..."
if [ ! -f "$BRAIN_DIR/voice-model.md" ]; then
    cp "$REPO_DIR/templates/voice-model.md" "$BRAIN_DIR/"
    echo "  → Created voice-model.md"
fi

if [ ! -f "$BRAIN_DIR/pipeline.md" ]; then
    cp "$REPO_DIR/templates/pipeline-report.md" "$BRAIN_DIR/pipeline.md"
    echo "  → Created pipeline.md"
fi

if [ ! -f "$BRAIN_DIR/learnings.md" ]; then
    echo "# Ongoing Learnings Log" > "$BRAIN_DIR/learnings.md"
    echo "This file captures tactical marketing/sales feedback over time." >> "$BRAIN_DIR/learnings.md"
    echo "  → Created learnings.md"
fi

# 3. Setup hooks
echo "🪝 Setting up Claude hooks..."
mkdir -p "$CLAUDE_HOOKS_DIR"

# Pre-send review hook
ln -sf "$REPO_DIR/hooks/pre-send-review.py" "$CLAUDE_HOOKS_DIR/pre-send-review.py"
chmod +x "$REPO_DIR/hooks/pre-send-review.py"

# Session start hook
ln -sf "$REPO_DIR/hooks/session-start.py" "$CLAUDE_HOOKS_DIR/session-start.py"
chmod +x "$REPO_DIR/hooks/session-start.py"

# Session stop hook
ln -sf "$REPO_DIR/hooks/session-stop.py" "$CLAUDE_HOOKS_DIR/session-stop.py"
chmod +x "$REPO_DIR/hooks/session-stop.py"

echo "✅ Hooks successfully symlinked."

# 4. Final Instructions
echo ""
echo "🎉 Growth by Design Bootstrap Complete!"
echo "----------------------------------------"
echo "Next Steps:"
echo "1. Open $HOME/brain/voice-model.md and fill out your specific writing patterns."
echo "2. Open Claude Code and try:"
echo "   'Use the deal-review skill to analyze my pipeline.'"
echo ""
