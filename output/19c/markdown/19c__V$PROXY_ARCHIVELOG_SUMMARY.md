---
id: 19c__V$PROXY_ARCHIVELOG_SUMMARY
name: V$PROXY_ARCHIVELOG_SUMMARY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-PROXY_ARCHIVELOG_SUMMARY.html
---

# V$PROXY_ARCHIVELOG_SUMMARY

V$PROXY_ARCHIVELOG_SUMMARY provides summary information about the output proxy archive log file.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NUM_FILES_BACKED | NUMBER |  |
| NUM_DISTINCT_FILES_BACKED | NUMBER |  |
| MIN_FIRST_CHANGE# | NUMBER |  |
| MAX_NEXT_CHANGE# | NUMBER |  |
| MIN_FIRST_TIME | DATE |  |
| MAX_NEXT_TIME | DATE |  |
| OUTPUT_BYTES | NUMBER |  |
| OUTPUT_BYTES_DISPLAY | VARCHAR2(4000) |  |
| CON_ID | NUMBER |  |