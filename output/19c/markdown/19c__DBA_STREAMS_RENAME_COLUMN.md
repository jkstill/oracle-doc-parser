---
id: 19c__DBA_STREAMS_RENAME_COLUMN
name: DBA_STREAMS_RENAME_COLUMN
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [dba]
source_file: DBA_STREAMS_RENAME_COLUMN.html
---

# DBA_STREAMS_RENAME_COLUMN

DBA_STREAMS_RENAME_COLUMN displays information about declarative rule-based transformations that rename a column in a row logical change record (LCR).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RULE_OWNER | VARCHAR2(128) | Owner of the rule |
| RULE_NAME | VARCHAR2(128) | Name of the rule |
| SCHEMA_NAME | VARCHAR2(128) | Schema of the column to be renamed |
| TABLE_NAME | VARCHAR2(128) | Table of the column to be renamed |
| FROM_COLUMN_NAME | VARCHAR2(4000) | Column to rename |
| TO_COLUMN_NAME | VARCHAR2(4000) | New column name |
| VALUE_TYPE | VARCHAR2(3) | Indicates whether to modify the old ( OLD ), new ( NEW ), or both ( * ) values of the LCR |
| PRECEDENCE | NUMBER | 2 (the execution order relative to other transformations on the same STEP_NUMBER ; the smaller number will be executed first) |
| STEP_NUMBER | NUMBER | Order in which this transformation should be executed |