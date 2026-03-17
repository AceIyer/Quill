#!/bin/sh

# Get the root directory of the git repo
REPO_ROOT=$(git rev-parse --show-toplevel)

# Check if this is the first commit (logic you already had)
COMMIT_COUNT=$(git rev-list --count HEAD)
if [ "$COMMIT_COUNT" -lt 1 ]; then
  exit 0
fi

# Trigger Quill
# We use 'python3' and point to the main.py in the repo root
echo "--- Quill is starting up ---"
python3 "$REPO_ROOT/main.py" run