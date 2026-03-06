---
id: 19c__V$PROXY_COPY_DETAILS
name: V$PROXY_COPY_DETAILS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-PROXY_COPY_DETAILS.html
---

# V$PROXY_COPY_DETAILS

V$PROXY_COPY_DETAILS contains information about all available control file and datafile proxy copies.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SESSION_KEY | NUMBER |  |
| SESSION_RECID | NUMBER |  |
| SESSION_STAMP | NUMBER |  |
| COPY_KEY | NUMBER |  |
| FILE# | NUMBER |  |
| HANDLE | VARCHAR2(513) |  |
| MEDIA | VARCHAR2(65) |  |
| MEDIA_POOL | NUMBER |  |
| TAG | VARCHAR2(32) |  |
| CREATION_CHANGE# | NUMBER |  |
| CREATION_TIME | DATE |  |
| CHECKPOINT_CHANGE# | NUMBER |  |
| CHECKPOINT_TIME | DATE |  |
| OUTPUT_BYTES | NUMBER |  |
| COMPLETION_TIME | DATE |  |
| CONTROLFILE_TYPE | VARCHAR2(1) |  |
| KEEP | VARCHAR2(3) |  |
| KEEP_UNTIL | DATE |  |
| KEEP_OPTIONS | VARCHAR2(11) |  |
| OUTPUT_BYTES_DISPLAY | VARCHAR2(4000) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content