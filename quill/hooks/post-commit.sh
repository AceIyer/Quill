#!/bin/sh

# --- Quill Git Hook (Unix) ---

# Check if this is the first commit
COMMIT_COUNT=$(git rev-list --count HEAD)
if [ "$COMMIT_COUNT" -lt 1 ]; then
  exit 0
fi

# Run Quill via installed CLI
echo "--- Quill is starting up ---"
quill run