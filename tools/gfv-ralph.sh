#!/usr/bin/env bash

# GFV Growth by Design - The Ralph Orchestration Loop
# Inspired by ralph-orchestrator. Allows unattended batch executions of an agent via CLI.

set -e

if [ -z "$1" ]; then
    echo "Usage: ./gfv-ralph.sh <prompt_string> [max_iterations]"
    echo "Example: ./gfv-ralph.sh 'Process the next 10 rows in pipeline.csv' 5"
    exit 1
fi

PROMPT="$1"
MAX_ITERATIONS=${2:-10}
ITERATION=1

echo "🚂 Starting Ralph Loop for '$PROMPT'"
echo "Max Iterations: $MAX_ITERATIONS"

while [ $ITERATION -le $MAX_ITERATIONS ]; do
    echo "---"
    echo "🔄 Iteration $ITERATION / $MAX_ITERATIONS"
    
    # Check if Claude Code is installed
    if command -v claude &> /dev/null; then
        claude -p "$PROMPT"
    else
        echo "❌ Error: Claude CLI not found. Ralph Loop requires the 'claude' command line tool."
        exit 1
    fi
    
    # We could check an exit condition via a file, e.g., if the agent touches 'DONE.flag'
    if [ -f "DONE.flag" ]; then
        echo "🏁 DONE.flag found! Agent signaled task completion."
        rm DONE.flag
        break
    fi

    ITERATION=$((ITERATION+1))
    
    echo "💤 Sleeping for 5s to avoid rate limits..."
    sleep 5
done

echo "🎉 Ralph Loop Complete."
