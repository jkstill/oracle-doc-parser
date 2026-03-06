---
id: 19c__V$SQLFN_METADATA
name: V$SQLFN_METADATA
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dynamic_performance]
source_file: V-SQLFN_METADATA.html
---

# V$SQLFN_METADATA

Internal function identification number

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FUNC_ID | NUMBER |  |
| NAME | VARCHAR2(128) |  |
| MINARGS | NUMBER |  |
| MAXARGS | NUMBER |  |
| DATATYPE | VARCHAR2(8) |  |
| VERSION | VARCHAR2(12) |  |
| ANALYTIC | VARCHAR2(3) |  |
| AGGREGATE | VARCHAR2(3) |  |
| OFFLOADABLE | VARCHAR2(3) |  |
| DISP_TYPE | VARCHAR2(13) |  |
| USAGE | VARCHAR2(128) |  |
| DESCR | VARCHAR2(4000) |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: " V$SQLFN_ARG_METADATA " See Also: " V$SQLFN_ARG_METADATA "