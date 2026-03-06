---
id: 19c__V$OPEN_CURSOR
name: V$OPEN_CURSOR
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dynamic_performance]
source_file: V-OPEN_CURSOR.html
---

# V$OPEN_CURSOR

V$OPEN_CURSOR lists cursors that each user session currently has opened and parsed, or cached.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SADDR | RAW(4 | 8) |  |
| SID | NUMBER |  |
| USER_NAME | VARCHAR2(128) |  |
| ADDRESS | RAW(4 | 8) |  |
| HASH_VALUE | NUMBER |  |
| SQL_ID | VARCHAR2(13) |  |
| SQL_TEXT | VARCHAR2(60) |  |
| LAST_SQL_ACTIVE_TIME | DATE |  |
| SQL_EXEC_ID | NUMBER |  |
| CURSOR_TYPE | VARCHAR2(64) |  |
| CHILD_ADDRESS | RAW(4 | 8) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content