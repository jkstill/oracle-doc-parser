#!/usr/bin/env bash

:<<COMMENT

./oracle-rag search "session wait events" | curl -s http://lestrade:11434/api/generate \
  -H "Content-Type: application/json" \
  -d @- <<'EOF'
{
  "model": "qwen2.5:14b",
  "prompt": "$(cat -)",
  "stream": false
}
EOF
COMMENT

oracle-rag ask \
  --ollama http://lestrade:11434 \
  --model 'qwen2.5:14b' \
  "which sessions are waiting and on what events"


