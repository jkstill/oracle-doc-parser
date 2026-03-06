---
id: 19c__DBA_XSTREAM_STMTS
name: DBA_XSTREAM_STMTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_XSTREAM_STMTS.html
---

# DBA_XSTREAM_STMTS

DBA_XSTREAM_STMTS displays information about the statements in all XStream statement DML handlers in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| HANDLER_NAME | VARCHAR2(128) | Name of the statement handler |
| EXECUTION_SEQUENCE | NUMBER | Execution sequence of the statement |
| STATEMENT | CLOB | Text of the SQL statement |
| CREATION_TIME | TIMESTAMP(6) | Timestamp for statement creation |
| MODIFICATION_TIME | TIMESTAMP(6) | Timestamp for statement modification |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content