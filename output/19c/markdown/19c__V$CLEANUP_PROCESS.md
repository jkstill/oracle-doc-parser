---
id: 19c__V$CLEANUP_PROCESS
name: V$CLEANUP_PROCESS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-CLEANUP_PROCESS.html
---

# V$CLEANUP_PROCESS

V$CLEANUP_PROCESS provides information on the PMON processes.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAME | VARCHAR2(5) |  |
| PADDR | RAW(8) |  |
| SADDR | RAW(8) |  |
| STATE | VARCHAR2(4) |  |
| DEAD_IN_CLEANUP | RAW(8) |  |
| CLEANUP_TIME | NUMBER |  |
| TIME_SINCE_LAST_CLEANUP | NUMBER |  |
| NUM_CLEANED | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: " V$DEAD_CLEANUP " See Also: " V$DEAD_CLEANUP "