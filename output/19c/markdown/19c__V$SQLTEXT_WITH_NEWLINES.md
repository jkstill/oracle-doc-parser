---
id: 19c__V$SQLTEXT_WITH_NEWLINES
name: V$SQLTEXT_WITH_NEWLINES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dynamic_performance]
source_file: V-SQLTEXT_WITH_NEWLINES.html
---

# V$SQLTEXT_WITH_NEWLINES

V$SQLTEXT_WITH_NEWLINES is identical to the V$SQLTEXT view except that, to improve legibility, V$SQLTEXT_WITH_NEWLINES does not replace newlines and tabs in the SQL statement with spaces.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ADDRESS | RAW(4 | 8) |  |
| HASH_VALUE | NUMBER |  |
| SQL_ID | VARCHAR2(13) |  |
| COMMAND_TYPE | NUMBER |  |
| PIECE | NUMBER |  |
| SQL_TEXT | VARCHAR2(64) |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: " V$SQLTEXT " See Also: " V$SQLTEXT "