---
id: 19c__V$LATCH
name: V$LATCH
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-LATCH.html
---

# V$LATCH

V$LATCH displays aggregate latch statistics for both parent and child latches, grouped by latch name.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ADDR | RAW(4 | 8) |  |
| LATCH# | NUMBER |  |
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

Individual parent and child latch statistics are broken down in the views V$LATCH_PARENT and V$LATCH_CHILDREN . See Also: " V$LATCH_CHILDREN " " V$LATCH_PARENT " See Also: " V$LATCH_CHILDREN " " V$LATCH_PARENT "