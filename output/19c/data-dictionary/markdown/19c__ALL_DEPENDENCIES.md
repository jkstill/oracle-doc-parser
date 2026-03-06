---
id: 19c__ALL_DEPENDENCIES
name: ALL_DEPENDENCIES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_DEPENDENCIES.html
---

# ALL_DEPENDENCIES

Related Views

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the object |
| NAME | VARCHAR2(128) | Name of the object |
| TYPE | VARCHAR2(18) | Type of the object |
| REFERENCED_OWNER | VARCHAR2(128) | Owner of the referenced object (remote owner if remote object) |
| REFERENCED_NAME | VARCHAR2(128) | Name of the referenced object |
| REFERENCED_TYPE | VARCHAR2(18) | Type of the referenced object |
| REFERENCED_LINK_NAME | VARCHAR2(128) | Name of the link to the parent object (if remote) |
| DEPENDENCY_TYPE | VARCHAR2(4) | Indicates whether the dependency is a REF dependency ( REF ) or not ( HARD ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content DBA_DEPENDENCIES describes all dependencies between objects in the database. This view does not display the SCHEMAID column. USER_DEPENDENCIES describes dependencies between objects in the current user's schema. This view does not display the OWNER column. See Also: " DBA_DEPENDENCIES " " USER_DEPENDENCIES " See Also: " DBA_DEPENDENCIES " " USER_DEPENDENCIES "