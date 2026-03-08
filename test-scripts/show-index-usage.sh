#!/usr/bin/env bash

# example: DRYRUN=N LOCAL_ONLY=N test-scripts/show-index-usage.sh  2>&1 | tee logs/show-index-usage-02.log

DRYRUN=${DRYRUN:-N}
LOCAL_ONLY=${LOCAL_ONLY:-Y}


[[ -n "$ANTHROPIC_API_KEY" ]] || source ~/anthropic.env || {
	echo "Please set the ANTHROPIC_API_KEY environment variable or source it from a file."
	exit 1
}

[[ -n "$ANTHROPIC_API_KEY" ]] || { echo "Please set the ANTHROPIC_API_KEY environment variable." ; exit 3; }

echo "Using ANTHROPIC_API_KEY: ${ANTHROPIC_API_KEY:0:5}...${ANTHROPIC_API_KEY: -5:5}"

[[ -n "$GOOGLE_CLOUD_PROJECT" ]] || source ~/google.env || {
	echo "Please set the Google environment variables for Gemini use."
	exit 2
}

# see if google env vars are set in  a subshell
(
	[[ -n "$GOOGLE_CLOUD_PROJECT" ]] || { echo "Please set the Google environment variables for Gemini use." ; exit 4; }
)

set -euo pipefail

banner () {
	echo
	echo "=================================================="
	echo "== $@"
	echo "=================================================="
	echo
}

declare -A queries=(
	["find database views"]="which database views include information about indexes used in a sql execution plan"
	["write SQL for index usage in execution plans"]="write a sql statement to show what indexes have been used in sql execution plans. include the sql_id and hash_value."
)

declare -a models_ordered=(
	"qwen2.5:14b"
	"gemini-2.5-pro"
	"claude-opus-4-6"
)

declare -A models=( # model and backend name
	["qwen2.5:14b"]='ollama'
	["gemini-2.5-pro"]='gemini'
	["claude-opus-4-6"]='claude'
)

declare -A localLLM=(
	["ollama"]='Y'
	["gemini"]='N'
	["claude"]='N'
)

for model in "${models_ordered[@]}"; do
	backend="${models[$model]}"
	for query_name in "${!queries[@]}"; do
		query="${queries[$query_name]}"
		banner "$model -- $query_name"
		CMD="./oracle-rag ask --show-prompt --backend $backend --model '$model' --ollama-url http://lestrade:11434 '$query'"
		export CMD
		# when using gemini backend, CMD does to work without eval
		if [[ "$DRYRUN" == 'Y' ]]; then
			if [[ $LOCAL_ONLY == 'Y' ]]; then
				[[ ${localLLM[$backend]} == 'Y' ]] &&  echo "DRY RUN LOCAL ONLY: $CMD"
			else
				echo "DRY RUN: $CMD" 
			fi
		else
			if [[ $LOCAL_ONLY == 'Y' ]]; then
				[[ ${localLLM[$backend]} == 'Y' ]] &&  eval "$CMD"
			else
				#echo "RUN: $CMD" 
				eval "$CMD"
			fi
		fi
	done
done


