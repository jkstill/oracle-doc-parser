---
id: 19c__V$PROXY_ARCHIVEDLOG
name: V$PROXY_ARCHIVEDLOG
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-PROXY_ARCHIVEDLOG.html
---

# V$PROXY_ARCHIVEDLOG

V$PROXY_ARCHIVEDLOG contains descriptions of archived log backups that were taken using the proxy copy functionality.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RECID | NUMBER |  |
| STAMP | NUMBER |  |
| DEVICE_TYPE | VARCHAR2(17) |  |
| HANDLE | VARCHAR2(513) |  |
| COMMENTS | VARCHAR2(81) |  |
| MEDIA | VARCHAR2(65) |  |
| MEDIA_POOL | NUMBER |  |
| TAG | VARCHAR2(32) |  |
| STATUS | VARCHAR2(1) |  |
| DELETED | VARCHAR2(3) |  |
| THREAD# | NUMBER |  |
| SEQUENCE# | NUMBER |  |
| RESETLOGS_CHANGE# | NUMBER |  |
| RESETLOGS_TIME | DATE |  |
| FIRST_CHANGE# | NUMBER |  |
| FIRST_TIME | DATE |  |
| NEXT_CHANGE# | NUMBER |  |
| NEXT_TIME | DATE |  |
| BLOCKS | NUMBER |  |
| BLOCK_SIZE | NUMBER |  |
| START_TIME | DATE |  |
| COMPLETION_TIME | DATE |  |
| ELAPSED_SECONDS | NUMBER |  |
| RMAN_STATUS_RECID | NUMBER |  |
| RMAN_STATUS_STAMP | NUMBER |  |
| TERMINAL | VARCHAR2(3) |  |
| KEEP | VARCHAR2(3) |  |
| KEEP_UNTIL | DATE |  |
| KEEP_OPTIONS | VARCHAR2(11) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content In a proxy copy, the media manager takes over the operations of backing up and restoring data. Each row represents a backup of one control file.