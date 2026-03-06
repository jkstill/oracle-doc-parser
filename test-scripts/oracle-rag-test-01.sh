#!/usr/bin/env bash

# With Ollama
oracle-rag search "how do I find which sessions are waiting and on what events" \
  | ollama run llama3 "Using only the Oracle documentation context provided, write a SQL query to answer this question."

# Or more directly — lookup the specific views you know you need, get full context
oracle-rag lookup V\$SESSION V\$SESSION_WAIT \
  | ollama run llama3 "Write a SQL query showing all active sessions with their current wait events and wait time."


