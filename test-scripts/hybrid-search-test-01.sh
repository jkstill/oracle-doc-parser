#!/usr/bin/env bash

# update: the best results are with qwen2.5:14b
# this is based in it providing SQL that did not require editing
model="qwen2.5:14b"

# slow and SQL is less robuset then qwen2.5, but it is more concise and less verbose
#model="qwen3.5:9b"

# fast, but inaaccurate and verbose responses
#model="llama3.2:latest"

# slow, terse and kind of useless responses
#model="glm-4.7-flash:q4_K_M"

# Storage / segments
./bin/oracle-rag ask --ollama-url http://lestrade:11434 --model "$model" \
  "show all segments larger than 1GB with their tablespace"

# Locking
./bin/oracle-rag ask --ollama-url http://lestrade:11434 --model "$model" \
  "show which sessions are blocking other sessions"

# AWR / performance history
./bin/oracle-rag ask --ollama-url http://lestrade:11434 --model "$model" \
  "query historical wait event data from AWR"

# PL/SQL task
./bin/oracle-rag ask --ollama-url http://lestrade:11434 --model "$model" \
  --task plsql \
  "gather statistics for all tables in a schema"


