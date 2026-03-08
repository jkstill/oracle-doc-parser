#!/usr/bin/env bash

# example: DRYRUN=N LOCAL_ONLY=N test-scripts/show-index-usage.sh  2>&1 | tee logs/show-index-usage-02.log

DRYRUN=${DRYRUN:-N}
LOCAL_ONLY=${LOCAL_ONLY:-Y}
SKIP_CLAUDE_API=${SKIP_CLAUDE_API:-Y} # skip by default as it is expensive and often rate limited

if [[ $SKIP_CLAUDE_API != 'Y' ]]; then

	[[ -n "$ANTHROPIC_API_KEY" ]] || source ~/anthropic.env || {
		echo "Please set the ANTHROPIC_API_KEY environment variable or source it from a file."
		exit 1
	}

	[[ -n "$ANTHROPIC_API_KEY" ]] || { echo "Please set the ANTHROPIC_API_KEY environment variable." ; exit 3; }

	echo "Using ANTHROPIC_API_KEY: ${ANTHROPIC_API_KEY:0:5}...${ANTHROPIC_API_KEY: -5:5}"

fi
	
if [[ $LOCAL_ONLY != 'Y' ]]; then

	[[ -n "$GOOGLE_CLOUD_PROJECT" ]] || source ~/google.env || {
		echo "Please set the Google environment variables for Gemini use."
		exit 2
	}

	# see if google env vars are set in  a subshell
	(
		[[ -n "$GOOGLE_CLOUD_PROJECT" ]] || { echo "Please set the Google environment variables for Gemini use." ; exit 4; }
	)

fi

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

declare -a llmsOrdered=(
	"ollama"
	"gemini"
	"claude"
	"claude-api"
)

declare -A llms=(
	[ollama]="qwen2.5:14b"
	[gemini]="gemini-2.5-pro"
	[claude]="claude-opus-4-6"
	[claude-api]="claude-opus-4-6" # expensive
)

declare -xA localLLM=(
	["ollama"]='Y'
	["gemini"]='N'
	["claude"]='N'
	["claude-api"]='N'
)

for backend in "${llmsOrdered[@]}"; do

	model="${llms[$backend]}"

	[[ $SKIP_CLAUDE_API == 'Y' ]] && [[ "$backend" == "claude-api" ]] && continue

	#echo "Backend: $backend"
	#echo "  Processing model: $model"
	#continue

	for query_name in "${!queries[@]}"; do
		query="${queries[$query_name]}"
		banner "$model -- $query_name"
		CMD="./oracle-rag ask --show-prompt --backend $backend --model '$model' --ollama-url http://lestrade:11434 '$query'"
		export CMD
		# when using gemini backend, CMD does to work without eval
		if [[ "$DRYRUN" == 'Y' ]]; then
			[[ $LOCAL_ONLY == 'Y' ]] && [[ ${localLLM[$backend]} == 'N' ]] && continue
			echo "DRY RUN: $CMD" 
		else
			[[ $LOCAL_ONLY == 'Y' ]] && [[ ${localLLM[$backend]} == 'N' ]] && continue
			echo "RUN CMD: $CMD"
			eval "$CMD"
		fi
	done
done

