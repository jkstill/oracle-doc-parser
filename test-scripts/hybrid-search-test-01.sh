#!/usr/bin/env bash

# so far the best results are with llama3.2
# it provides good queries, good explanations, and good performance (response time)

model="qwen2.5:14b"
#model="qwen3.5:9b"
model="llama3.2:latest"

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


