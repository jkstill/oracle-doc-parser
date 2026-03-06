---
id: 19c__V$LATCH_CHILDREN
name: V$LATCH_CHILDREN
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-LATCH_CHILDREN.html
---

# V$LATCH_CHILDREN

V$LATCH_CHILDREN displays statistics about child latches.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ADDR | RAW(4 | 8) |  |
| LATCH# | NUMBER |  |
| CHILD# | NUMBER |  |
| LEVEL# | NUMBER |  |
| NAME | VARCHAR2(64) |  |
| HASH | NUMBER |  |
| GETS | NUMBER |  |
| MISSES | NUMBER |  |
| SLEEPS | NUMBER |  |
| IMMEDIATE_GETS | NUMBER |  |
| IMMEDIATE_MISSES | NUMBER |  |
| WAITERS_WOKEN | NUMBER |  |
| WAITS_HOLDING_LATCH | NUMBER |  |
| SPIN_GETS | NUMBER |  |
| SLEEP[1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11] | NUMBER |  |
| WAIT_TIME | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view includes all columns of V$LATCH plus the CHILD# column. Note that child latches have the same parent if their LATCH# columns match each other. See Also: " V$LATCH " See Also: " V$LATCH "