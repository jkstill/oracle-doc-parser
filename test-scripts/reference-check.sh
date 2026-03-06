#!/usr/bin/env bash

# Breakdown by object_type
python3 -c "
import json
from collections import Counter
counts = Counter()
with open('output/19c/oracle_docs.jsonl') as f:
    for line in f:
        obj = json.loads(line)
        counts[obj['object_type']] += 1
for k, v in counts.most_common():
    print(f'{v:5d}  {k}')
"

# Breakdown by category (for data dictionary views)
python3 -c "
import json
from collections import Counter
counts = Counter()
with open('output/19c/oracle_docs.jsonl') as f:
    for line in f:
        obj = json.loads(line)
        if obj['category']:
            counts[obj['category']] += 1
for k, v in counts.most_common():
    print(f'{v:5d}  {k}')
"

# Spot check: any chunks with zero columns extracted?
python3 -c "
import json
empty = []
with open('output/19c/oracle_docs.jsonl') as f:
    for line in f:
        obj = json.loads(line)
        if obj['object_type'] == 'data_dictionary_view' and not obj['columns']:
            empty.append(obj['name'])
print(f'{len(empty)} views with no columns extracted')
for name in empty[:20]:
    print(f'  {name}')
"

