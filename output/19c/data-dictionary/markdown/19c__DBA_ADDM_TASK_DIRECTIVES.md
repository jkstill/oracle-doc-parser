---
id: 19c__DBA_ADDM_TASK_DIRECTIVES
name: DBA_ADDM_TASK_DIRECTIVES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_ADDM_TASK_DIRECTIVES.html
---

# DBA_ADDM_TASK_DIRECTIVES

DBA_ADDM_TASK_DIRECTIVES displays information about all ADDM task directives in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TASK_ID | NUMBER | An ADDM advisor task identifier to which the directive instance is associated |
| TASK_NAME | VARCHAR2(128) | An ADDM advisor task to which the directive instance is associated |
| USERNAME | VARCHAR2(128) | Database user who owns the ADDM task instance |
| SEQ_ID | NUMBER | Unique ID for the directive instance. The directive management engine automatically generates ID numbers. |
| INSTANCE_NAME | VARCHAR2(128) | A user-assigned name for the ADDM task directive instance |
| DIRECTIVE_NAME | VARCHAR2(128) | Any value that further classifies this directive within a domain. The domain and the name form a unique key for the directive. |
| DESCRIPTION | VARCHAR2(4000) | Description of the ADDM task directive, shown in the language used by the current session |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View USER_ADDM_TASK_DIRECTIVES displays information about ADDM task directives owned by the current user. See Also: " USER_ADDM_TASK_DIRECTIVES " See Also: " USER_ADDM_TASK_DIRECTIVES "