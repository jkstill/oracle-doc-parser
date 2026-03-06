---
id: 19c__DBA_ADVISOR_DIR_INSTANCES
name: DBA_ADVISOR_DIR_INSTANCES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_ADVISOR_DIR_INSTANCES.html
---

# DBA_ADVISOR_DIR_INSTANCES

DBA_ADVISOR_DIR_INSTANCES provides information about all global instances for a directive.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DIRECTIVE_ID | NUMBER | Unique id for directive. The directive management engine automatically generates ID numbers. |
| INSTANCE_ID | NUMBER | Unique id for the directive instance. The directive management engine automatically generates ID numbers. |
| INSTANCE_NAME | VARCHAR2(128) | A user-assigned name for the directive instance. |
| DATA | CLOB | An XML document that gives meaningful default values for all parts of the directive. |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content