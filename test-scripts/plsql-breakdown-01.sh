#!/usr/bin/env bash

python3 -c "
import json
from collections import Counter
counts = Counter()
parents = Counter()
with open('output/19c/pl-sql/oracle_docs.jsonl') as f:
    for line in f:
        obj = json.loads(line)
        counts[obj['object_type']] += 1
        if obj['parent']:
            parents[obj['parent']] += 1

print('=== By object_type ===')
for k, v in counts.most_common():
    print(f'{v:5d}  {k}')

print()
print('=== Top 20 packages by subprogram count ===')
for k, v in parents.most_common(20):
    print(f'{v:5d}  {k}')
"

