---
id: 19c__DBA_WI_PATTERNS
name: DBA_WI_PATTERNS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_WI_PATTERNS.html
---

# DBA_WI_PATTERNS

Each row in DBA_WI_PATTERNS represents a pattern that has been identified by Workload Intelligence as significant in the workload associated with the given job. Such a pattern consists of one or more templates.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| JOB_ID | NUMBER | The identifier of the job in the workload of which the current pattern has been found |
| PATTERN_ID | NUMBER | The identifier of the current pattern |
| LENGTH | NUMBER | The length of the pattern, that is, the number of items (templates) it consists of |
| NUMBER_OF_EXECUTIONS | NUMBER | The number of times the current pattern has been executed in the given workload |
| DB_TIME | NUMBER | The total time consumed in the database server by all the executions of the current pattern in the given workload |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content These templates that comprise the given pattern are described in the related view DBA_WI_PATTERN_ITEMS . See Also: " DBA_WI_PATTERN_ITEMS " See Also: " DBA_WI_PATTERN_ITEMS "