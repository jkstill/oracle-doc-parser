---
id: 19c__V$IM_COLUMN_LEVEL
name: V$IM_COLUMN_LEVEL
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [dynamic_performance]
source_file: V-IM_COLUMN_LEVEL.html
---

# V$IM_COLUMN_LEVEL

V$IM_COLUMN_LEVEL presents the selective column compression levels that are defined using the inmemory_memcompress clause of the inmemory_column_clause of the CREATE TABLE statement.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| INST_ID | NUMBER |  |
| OWNER | VARCHAR2(31) |  |
| OBJ_NUM | NUMBER |  |
| TABLE_NAME | VARCHAR2(31) |  |
| SEGMENT_COLUMN_ID | NUMBER |  |
| COLUMN_NAME | VARCHAR2(31) |  |
| INMEMORY_COMPRESSION | VARCHAR2(26) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view returns no rows for a table which has no associated selective column compression levels. Note: The SYS_IME hidden virtual columns automatically added by the In-Memory Expression (IME) infrastructure will not be shown in this view. See Also: " INMEMORY_CLAUSE_DEFAULT " " V$IM_SEGMENTS " " V$IM_USER_SEGMENTS " Oracle Database In-Memory Guide for an introduction to the IM column store Oracle Database SQL Language Reference for more information about the inmemory_column_clause of the SQL CREATE TABLE statement Note: The SYS_IME hidden virtual columns automatically added by the In-Memory Expression (IME) infrastructure will not be shown in this view. See Also: " INMEMORY_CLAUSE_DEFAULT " " V$IM_SEGMENTS " " V$IM_USER_SEGMENTS " Oracle Database In-Memory Guide for an introduction to the IM column store Oracle Database SQL Language Reference for more information about the inmemory_column_clause of the SQL CREATE TABLE statement