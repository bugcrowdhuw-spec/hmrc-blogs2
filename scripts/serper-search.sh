#!/bin/bash
# Serper.dev search wrapper
# Usage: ./serper-search.sh "your search query"

# Load API key from .env
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
if [ -f "$WORKSPACE_DIR/.env" ]; then
  source "$WORKSPACE_DIR/.env"
fi

if [ -z "$SERPER_API_KEY" ]; then
  echo "Error: SERPER_API_KEY not set" >&2
  exit 1
fi

if [ -z "$1" ]; then
  echo "Usage: $0 \"search query\"" >&2
  exit 1
fi

QUERY="$1"
NUM="${2:-5}"

curl -s -X POST "https://google.serper.dev/search" \
  -H "X-API-KEY: $SERPER_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"q\": \"$QUERY\", \"num\": $NUM}" | \
  jq -r '.organic[] | "**\(.title)**\n\(.link)\n\(.snippet)\n"'
