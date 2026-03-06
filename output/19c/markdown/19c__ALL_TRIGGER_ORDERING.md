---
id: 19c__ALL_TRIGGER_ORDERING
name: ALL_TRIGGER_ORDERING
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_TRIGGER_ORDERING.html
---

# ALL_TRIGGER_ORDERING

ALL_TRIGGER_ORDERING describes the triggers accessible to the current user that have FOLLOWS or PRECEDES ordering.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TRIGGER_OWNER | VARCHAR2(128) | Owner of the trigger |
| TRIGGER_NAME | VARCHAR2(128) | Name of the trigger |
| REFERENCED_TRIGGER_OWNER | VARCHAR2(128) | Owner of the referenced trigger |
| REFERENCED_TRIGGER_NAME | VARCHAR2(128) | Name of the referenced trigger |
| ORDERING_TYPE | VARCHAR2(8) | Type of the ordering between the trigger and the referenced trigger: FOLLOWS PRECEDES |

## Usage Notes

Related Views DBA_TRIGGER_ORDERING describes all triggers in the database that have FOLLOWS or PRECEDES ordering. USER_TRIGGER_ORDERING describes the triggers owned by the current user that have FOLLOWS or PRECEDES ordering. This view does not display the TRIGGER_OWNER column. See Also: " DBA_TRIGGER_ORDERING " " USER_TRIGGER_ORDERING " See Also: " DBA_TRIGGER_ORDERING " " USER_TRIGGER_ORDERING "