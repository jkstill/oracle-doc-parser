---
id: 19c__V$RMAN_STATUS
name: V$RMAN_STATUS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-RMAN_STATUS.html
---

# V$RMAN_STATUS

Session ID of the session which is running this RMAN operation

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SID | NUMBER |  |
| RECID | NUMBER |  |
| STAMP | NUMBER |  |
| PARENT_RECID | NUMBER |  |
| PARENT_STAMP | NUMBER |  |
| SESSION_RECID | NUMBER |  |
| SESSION_STAMP | NUMBER |  |
| ROW_LEVEL | NUMBER |  |
| ROW_TYPE | VARCHAR2(19) |  |
| COMMAND_ID | VARCHAR2(33) |  |
| OPERATION | VARCHAR2(33) |  |
| STATUS | VARCHAR2(23) |  |
| MBYTES_PROCESSED | NUMBER |  |
| START_TIME | DATE |  |
| END_TIME | DATE |  |
| INPUT_BYTES | NUMBER |  |
| OUTPUT_BYTES | NUMBER |  |
| OPTIMIZED | VARCHAR2(3) |  |
| OBJECT_TYPE | VARCHAR2(13) |  |
| OUTPUT_DEVICE_TYPE | VARCHAR2(17) |  |
| OSB_ALLOCATED | VARCHAR2(3) |  |
| CON_ID | NUMBER |  |