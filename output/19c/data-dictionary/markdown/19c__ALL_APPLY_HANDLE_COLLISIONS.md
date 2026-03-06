---
id: 19c__ALL_APPLY_HANDLE_COLLISIONS
name: ALL_APPLY_HANDLE_COLLISIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_APPLY_HANDLE_COLLISIONS.html
---

# ALL_APPLY_HANDLE_COLLISIONS

ALL_APPLY_HANDLE_COLLISIONS provides details about apply handlers for collisions on objects visible to the user at the table level.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| APPLY_NAME | VARCHAR2(128) | Name of the apply process |
| OBJECT_OWNER | VARCHAR2(128) | Owner of the target object |
| OBJECT_NAME | VARCHAR2(128) | Name of the target object |
| SOURCE_OBJECT_OWNER | VARCHAR2(128) | Source database owner of the object |
| SOURCE_OBJECT_NAME | VARCHAR2(128) | Source database name of the object |
| ENABLED | VARCHAR2(1) | State of the collision handlers: Y for enabled, N for disabled |
| SET_BY | VARCHAR2(10) | Entity that set up the handler: USER GOLDENGATE |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View DBA_APPLY_HANDLE_COLLISIONS provides details about apply handlers for collisions at the table level. See Also: " DBA_APPLY_HANDLE_COLLISIONS " See Also: " DBA_APPLY_HANDLE_COLLISIONS "