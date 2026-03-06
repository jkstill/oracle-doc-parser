---
id: 19c__ALL_SECONDARY_OBJECTS
name: ALL_SECONDARY_OBJECTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_SECONDARY_OBJECTS.html
---

# ALL_SECONDARY_OBJECTS

ALL_SECONDARY_OBJECTS provides information about secondary objects associated with domain indexes accessible to the user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| INDEX_OWNER | VARCHAR2(128) | Owner of the domain index |
| INDEX_NAME | VARCHAR2(128) | Name of the domain index |
| SECONDARY_OBJECT_OWNER | VARCHAR2(128) | Owner of the secondary object created by the domain index |
| SECONDARY_OBJECT_NAME | VARCHAR2(128) | Name of the secondary object created by the domain index |
| SECONDARY_OBJDATA_TYPE | VARCHAR2(20) | Type of the secondary object created by the domain index |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view is only relevant for domain indexes. And currently, the secondary objects can only be tables. Related Views DBA_SECONDARY_OBJECTS provides information about all secondary objects that are associated with domain indexes in the database. USER_SECONDARY_OBJECTS provides information about secondary objects associated with domain indexes owned by the current user. See Also: " DBA_SECONDARY_OBJECTS " " USER_SECONDARY_OBJECTS "