---
id: 19c__DBA_STREAMS_RENAME_SCHEMA
name: DBA_STREAMS_RENAME_SCHEMA
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_STREAMS_RENAME_SCHEMA.html
---

# DBA_STREAMS_RENAME_SCHEMA

DBA_STREAMS_RENAME_SCHEMA displays information about declarative rule-based transformations that rename a schema in a row logical change record (LCR).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RULE_OWNER | VARCHAR2(128) | Owner of the rule |
| RULE_NAME | VARCHAR2(128) | Name of the rule |
| FROM_SCHEMA_NAME | VARCHAR2(128) | Schema to be renamed |
| TO_SCHEMA_NAME | VARCHAR2(128) | New schema name |
| PRECEDENCE | NUMBER | 5 (the execution order relative to other transformations on the same STEP_NUMBER ; the smaller number will be executed first) |
| STEP_NUMBER | NUMBER | Order in which this transformation should be executed |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content