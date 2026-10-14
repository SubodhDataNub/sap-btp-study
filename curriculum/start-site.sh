#!/bin/sh
# Starts the local study site (macOS / Linux). Press Ctrl+C to stop.
DIR="$(cd "$(dirname "$0")" && pwd)"
if command -v python3 >/dev/null 2>&1; then
  exec python3 "$DIR/site/serve.py" "$@"
else
  exec python "$DIR/site/serve.py" "$@"
fi
