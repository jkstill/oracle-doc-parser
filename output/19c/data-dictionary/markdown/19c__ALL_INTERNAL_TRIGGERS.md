---
id: 19c__ALL_INTERNAL_TRIGGERS
name: ALL_INTERNAL_TRIGGERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_INTERNAL_TRIGGERS.html
---

# ALL_INTERNAL_TRIGGERS

Related Views

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TABLE_NAME | VARCHAR2(128) | Name of the table on which the trigger is defined |
| INTERNAL_TRIGGER_TYPE | VARCHAR2(19) | Indicates the type of internal trigger on the table |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content DBA_INTERNAL_TRIGGERS describes internal triggers on all tables in the database. USER_INTERNAL_TRIGGERS describes all internal triggers on tables owned by the current user. This view does not display the OWNER_NAME column. See Also: " DBA_INTERNAL_TRIGGERS " " USER_INTERNAL_TRIGGERS " See Also: " DBA_INTERNAL_TRIGGERS " " USER_INTERNAL_TRIGGERS "