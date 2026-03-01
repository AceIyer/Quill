#!/bin/sh

# Exit if first commit
COMMIT_COUNT=$(git rev-list --count HEAD)
if [ "$COMMIT_COUNT" -lt 2 ]; then
  exit 0
fi

CURRENT_COMMIT=$(git rev-parse HEAD)
PREVIOUS_COMMIT=$(git rev-parse HEAD~1)

CHANGED_FILES=$(git diff --name-only HEAD~1 HEAD)

echo "current_commit=$CURRENT_COMMIT"
echo "previous_commit=$PREVIOUS_COMMIT"
echo "changed_files:"
echo "$CHANGED_FILES"
