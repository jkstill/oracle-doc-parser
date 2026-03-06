#!/usr/bin/env bash

# Storage / segments
./oracle-rag ask --ollama-url http://lestrade:11434 --model qwen2.5:14b \
  "show all segments larger than 1GB with their tablespace"

# Locking
./oracle-rag ask --ollama-url http://lestrade:11434 --model qwen2.5:14b \
  "show which sessions are blocking other sessions"

# AWR / performance history
./oracle-rag ask --ollama-url http://lestrade:11434 --model qwen2.5:14b \
  "query historical wait event data from AWR"

# PL/SQL task
./oracle-rag ask --ollama-url http://lestrade:11434 --model qwen2.5:14b \
  --task plsql \
  "gather statistics for all tables in a schema"


