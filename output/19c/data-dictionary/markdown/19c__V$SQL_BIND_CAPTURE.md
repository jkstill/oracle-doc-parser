---
id: 19c__V$SQL_BIND_CAPTURE
name: V$SQL_BIND_CAPTURE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dynamic_performance]
source_file: V-SQL_BIND_CAPTURE.html
---

# V$SQL_BIND_CAPTURE

Reference to the cursor defining the bind variable

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ADDRESS | RAW(4 | 8) |  |
| HASH_VALUE | NUMBER |  |
| SQL_ID | VARCHAR2(13) |  |
| CHILD_ADDRESS | RAW(4 | 8) |  |
| CHILD_NUMBER | NUMBER |  |
| NAME | VARCHAR2(128) |  |
| POSITION | NUMBER |  |
| DUP_POSITION | NUMBER |  |
| DATATYPE | NUMBER |  |
| DATATYPE_STRING | VARCHAR2(15) |  |
| CHARACTER_SID | NUMBER |  |
| PRECISION | NUMBER |  |
| SCALE | NUMBER |  |
| MAX_LENGTH | NUMBER |  |
| WAS_CAPTURED | VARCHAR2(3) |  |
| LAST_CAPTURED | DATE |  |
| VALUE_STRING | VARCHAR2(4000) |  |
| VALUE_ANYDATA | ANYDATA |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Reference to the cursor defining the bind variable ( hash_value , address ) for the parent cursor and ( hash_value , child_address ) for the child cursor. Bind metadata Name, position, data type, character set ID, precision, scale, and maximum length of the bind variable. Bind data One of the bind values used for the bind variable during a past execution of its associated SQL statement. Bind values are not always captured for this view. Bind values are displayed by this view only when the type of the bind variable is simple (this excludes LONG, LOB, and ADT data types) and when the bind variable is used in the WHERE or HAVING clauses of the SQL statement. Bind capture is disabled when the STATISTICS_LEVEL initialization parameter is set to BASIC . This view can be joined with V$SQLAREA on ( HASH_VALUE , ADDRESS ) and with V$SQL on ( HASH_VALUE , CHILD_ADDRESS ). See Also: " STATISTICS_LEVEL " " V$SQLAREA " " V$SQL " See Also: " STATISTICS_LEVEL " " V$SQLAREA " " V$SQL "