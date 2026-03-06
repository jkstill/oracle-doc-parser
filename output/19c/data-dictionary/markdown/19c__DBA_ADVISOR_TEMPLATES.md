---
id: 19c__DBA_ADVISOR_TEMPLATES
name: DBA_ADVISOR_TEMPLATES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_ADVISOR_TEMPLATES.html
---

# DBA_ADVISOR_TEMPLATES

DBA_ADVISOR_TEMPLATES displays information about all templates in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the task |
| TASK_ID | NUMBER | Unique identifier of the task |
| TASK_NAME | VARCHAR2(128) | Name of the task |
| DESCRIPTION | VARCHAR2(256) | User-supplied description of the task |
| ADVISOR_NAME | VARCHAR2(128) | Advisor associated with the task |
| CREATED | DATE | Creation date of the task |
| LAST_MODIFIED | DATE | Date on which the task was last modified |
| SOURCE | VARCHAR2(128) | Optional task or template on which the template was based |
| READ_ONLY | VARCHAR2(5) | Indicates whether the task can be modified or deleted ( TRUE ) or not ( FALSE ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View USER_ADVISOR_TEMPLATES displays information about the templates owned by the current user. This view does not display the OWNER column. See Also: " USER_ADVISOR_TEMPLATES " See Also: " USER_ADVISOR_TEMPLATES "