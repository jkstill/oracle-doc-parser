---
id: 19c__V$SQL_BIND_DATA
name: V$SQL_BIND_DATA
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dynamic_performance]
source_file: V-SQL_BIND_DATA.html
---

# V$SQL_BIND_DATA

V$SQL_BIND_DATA describes information related to bind variables.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CURSOR_NUM | NUMBER |  |
| POSITION | NUMBER |  |
| DATATYPE | NUMBER |  |
| SHARED_MAX_LEN | NUMBER |  |
| PRIVATE_MAX_LEN | NUMBER |  |
| ARRAY_SIZE | NUMBER |  |
| PRECISION | NUMBER |  |
| SCALE | NUMBER |  |
| SHARED_FLAG | NUMBER |  |
| SHARED_FLAG2 | NUMBER |  |
| BUF_ADDRESS | RAW(4 | 8) |  |
| BUF_LENGTH | NUMBER |  |
| VAL_LENGTH | NUMBER |  |
| BUF_FLAG | NUMBER |  |
| INDICATOR | NUMBER |  |
| VALUE | VARCHAR2(4000) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content V$SQL_BIND_DATA describes, for each distinct bind variable in each cursor owned by the session querying this view: Actual bind data, if the bind variable is user defined The underlying literal, if the CURSOR_SHARING parameter is set to FORCE and the bind variable is system generated. (System-generated binds have a value of 256 in the SHARED_FLAG2 column.) See Also: " CURSOR_SHARING " See Also: " CURSOR_SHARING "