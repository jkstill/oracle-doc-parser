---
id: 19c__V$DEAD_CLEANUP
name: V$DEAD_CLEANUP
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-DEAD_CLEANUP.html
---

# V$DEAD_CLEANUP

V$DEAD_CLEANUP shows the dead processes and killed sessions present in the instance and their cleanup status.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TYPE | VARCHAR2(64) |  |
| PADDR | RAW(8) |  |
| SADDR | RAW(8) |  |
| ROOT_ADDR | RAW(8) |  |
| CLEANUP_OWNER | VARCHAR2(64) |  |
| STATE | VARCHAR2(64) |  |
| DEAD_TIME | NUMBER |  |
| CLEANUP_ATTEMPTS | NUMBER |  |
| LAST_ATTEMPT | NUMBER |  |
| CLEANUP_PROCESS | RAW(8) |  |
| CLEANUP_TIME | NUMBER |  |
| NUM_BLOCKED | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: " V$CLEANUP_PROCESS " See Also: " V$CLEANUP_PROCESS "