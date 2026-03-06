---
id: 19c__V$PROCESS_MEMORY
name: V$PROCESS_MEMORY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-PROCESS_MEMORY.html
---

# V$PROCESS_MEMORY

V$PROCESS_MEMORY displays dynamic PGA memory usage by named component categories for each process.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PID | NUMBER |  |
| SERIAL# | NUMBER |  |
| CATEGORY | VARCHAR2(15) |  |
| ALLOCATED | NUMBER |  |
| USED | NUMBER |  |
| MAX_ALLOCATED | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content