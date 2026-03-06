---
id: 19c__DBA_STREAMS_RENAME_TABLE
name: DBA_STREAMS_RENAME_TABLE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [dba]
source_file: DBA_STREAMS_RENAME_TABLE.html
---

# DBA_STREAMS_RENAME_TABLE

DBA_STREAMS_RENAME_TABLE displays information about declarative rule-based transformations that rename a table in a row logical change record (LCR).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RULE_OWNER | VARCHAR2(128) | Owner of the rule |
| RULE_NAME | VARCHAR2(128) | Name of the rule |
| FROM_SCHEMA_NAME | VARCHAR2(128) | Schema to be renamed |
| TO_SCHEMA_NAME | VARCHAR2(128) | New schema name |
| FROM_TABLE_NAME | VARCHAR2(128) | Table to be renamed |
| TO_TABLE_NAME | VARCHAR2(128) | New table name |
| PRECEDENCE | NUMBER | 4 (the execution order relative to other transformations on the same STEP_NUMBER ; the smaller number will be executed first) |
| STEP_NUMBER | NUMBER | Order in which this transformation should be executed |