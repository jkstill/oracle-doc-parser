#!/usr/bin/env bash

( [[ -n "$ANTHROPIC_API_KEY" ]] || source ~/anthropic.env ) || {
	echo "Please set the ANTHROPIC_API_KEY environment variable or source it from a file."
	exit 1
}

( [[ -n "$GOOGLE_CLOUD_PROJECT" ]] || source ~/google.env ) || {
	echo "Please set the Google environment variables for Gemini use."
	exit 2
}

banner () {
	echo "=================================================="
	echo "== $@"
	echo "=================================================="
}

banner "qwen2.5:14b -- find database views"
set -x
./oracle-rag ask --show-prompt --ollama-url http://lestrade:11434  --model qwen2.5:14b 'which database views include information about indexes used in a sql execution plan'
set +x

banner "qwen2.5:14b -- write SQL for index usage in execution plans"
set -x
./oracle-rag ask --show-prompt --include 'V$SQL_PLAN_STATISTICS_ALL' --ollama-url http://lestrade:11434  --model qwen2.5:14b 'write a sql statement to show what indexes have been used in sql execution plans. include the sql_id and hash_value.'
set +x

banner "gemini-2.5-pro -- find database views"
set -x
./oracle-rag ask --show-prompt --backend gemini --model 'gemini-2.5-pro' --ollama-url http://lestrade:11434 'which database views include information about indexes used in a sql execution plan'
set +x

banner "gemini-2.5-pro -- write SQL for index usage in execution plans"
set -x
./oracle-rag ask --show-prompt --include 'V$SQL_PLAN_STATISTICS_ALL' --backend gemini --model 'gemini-2.5-pro' --ollama-url http://lestrade:11434 'write a sql statement to show what indexes have been used in sql execution plans. include the sql_id and hash_value.'
set +x

banner "claude-opus-4-6 -- find database views"
set -x
./oracle-rag ask --show-prompt --backend claude --model 'claude-opus-4-6' --ollama-url http://lestrade:11434 'which database views include information about indexes used in a sql execution plan'
set +x

banner "claude-opus-4-6 -- write SQL for index usage in execution plans"
set -x
./oracle-rag ask --show-prompt --include 'V$SQL_PLAN_STATISTICS_ALL' --backend claude --model 'claude-opus-4-6' --ollama-url http://lestrade:11434 'write a sql statement to show what indexes have been used in sql execution plans. include the sql_id and hash_value.'
set +x


