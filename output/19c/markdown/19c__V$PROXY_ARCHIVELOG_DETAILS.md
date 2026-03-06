---
id: 19c__V$PROXY_ARCHIVELOG_DETAILS
name: V$PROXY_ARCHIVELOG_DETAILS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-PROXY_ARCHIVELOG_DETAILS.html
---

# V$PROXY_ARCHIVELOG_DETAILS

V$PROXY_ARCHIVELOG_DETAILS contains information about all available archive log proxy copies.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SESSION_KEY | NUMBER |  |
| SESSION_RECID | NUMBER |  |
| SESSION_STAMP | NUMBER |  |
| COPY_KEY | NUMBER |  |
| THREAD# | NUMBER |  |
| SEQUENCE# | NUMBER |  |
| RESETLOGS_CHANGE# | NUMBER |  |
| RESETLOGS_TIME | DATE |  |
| HANDLE | VARCHAR2(513) |  |
| MEDIA | VARCHAR2(65) |  |
| MEDIA_POOL | NUMBER |  |
| TAG | VARCHAR2(32) |  |
| FIRST_CHANGE# | NUMBER |  |
| NEXT_CHANGE# | NUMBER |  |
| FIRST_TIME | DATE |  |
| NEXT_TIME | DATE |  |
| OUTPUT_BYTES | NUMBER |  |
| COMPLETION_TIME | DATE |  |
| OUTPUT_BYTES_DISPLAY | VARCHAR2(3) |  |
| KEEP | DATE |  |
| KEEP_UNTIL | VARCHAR2(11) |  |
| KEEP_OPTIONS | VARCHAR2(4000) |  |
| CON_ID | NUMBER |  |