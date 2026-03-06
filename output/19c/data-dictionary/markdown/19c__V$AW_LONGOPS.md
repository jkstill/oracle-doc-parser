---
id: 19c__V$AW_LONGOPS
name: V$AW_LONGOPS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-AW_LONGOPS.html
---

# V$AW_LONGOPS

V$AW_LONGOPS displays status information about active SQL cursors initiated in an analytic workspace.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SESSION_ID | NUMBER |  |
| CURSOR_NAME | VARCHAR2(64) |  |
| COMMAND | VARCHAR2(17) |  |
| STATUS | VARCHAR2(9) |  |
| ROWS_PROCESSED | NUMBER |  |
| SEQ_NUMBER | NUMBER |  |
| SQL_ID | VARCHAR2(13) |  |
| TARGET | VARCHAR2(64) |  |
| TARGET_DESC | VARCHAR2(64) |  |
| START_TIME | DATE |  |
| LAST_UPDATE_TIME | DATE |  |
| ELAPSED_SECONDS | NUMBER |  |
| SOFAR | NUMBER |  |
| TOTALWORK | NUMBER |  |
| UNITS | VARCHAR2(6) |  |
| MESSAGE | VARCHAR2(512) |  |
| USERNAME | VARCHAR2(32) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content