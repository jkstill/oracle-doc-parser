---
id: 19c__DBA_ADVISOR_DIR_TASK_INST
name: DBA_ADVISOR_DIR_TASK_INST
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_ADVISOR_DIR_TASK_INST.html
---

# DBA_ADVISOR_DIR_TASK_INST

DBA_ADVISOR_DIR_TASK_INST provides information about all task directive instances.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DIRECTIVE_ID | NUMBER | Unique id for directive. The directive management engine automatically generates ID numbers. |
| SEQ_ID | NUMBER | Unique id for the directive instance. The directive management engine automatically generates ID numbers. |
| INSTANCE_NAME | VARCHAR2(128) | A user-assigned name for the directive instance. |
| USERNAME | VARCHAR2(128) | Database user who owns the task instance. |
| TASK_ID | NUMBER | An advisor task identifier to which the directive instance is associated |
| TASK_NAME | VARCHAR2(128) | An advisor task to which the directive instance is associated. |
| DATA | CLOB | An XML document that gives meaningful default values for all parts of the directive. |

## Usage Notes

Related View USER_ADVISOR_DIR_TASK_INST provides information about all task directive instances owned by the current user. See Also: " USER_ADVISOR_DIR_TASK_INST " See Also: " USER_ADVISOR_DIR_TASK_INST "