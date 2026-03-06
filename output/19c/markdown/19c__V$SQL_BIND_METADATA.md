---
id: 19c__V$SQL_BIND_METADATA
name: V$SQL_BIND_METADATA
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dynamic_performance]
source_file: V-SQL_BIND_METADATA.html
---

# V$SQL_BIND_METADATA

V$SQL_BIND_METADATA describes metadata related to bind variables.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ADDRESS | RAW(4 | 8) |  |
| POSITION | NUMBER |  |
| DATATYPE | NUMBER |  |
| MAX_LENGTH | NUMBER |  |
| ARRAY_LEN | NUMBER |  |
| BIND_NAME | VARCHAR2(128) |  |
| CON_ID | NUMBER |  |

## Usage Notes

V$SQL_BIND_METADATA describes, for each distinct bind variable in each cursor owned by the session querying this view: Bind metadata provided by the client, if the bind variable is user defined Metadata based on the underlying literal, if the CURSOR_SHARING parameter is set to FORCE and the bind variable is system-generated. See Also: " CURSOR_SHARING " See Also: " CURSOR_SHARING "