---
id: 19c__DBA_EDITIONED_TYPES
name: DBA_EDITIONED_TYPES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_EDITIONED_TYPES.html
---

# DBA_EDITIONED_TYPES

DBA_EDITIONED_TYPES lists all types that are editioned by default for every user in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SCHEMA | VARCHAR2(128) | Schema in which the object types is editionable |
| OBJECT_TYPE | VARCHAR2(23) | Object type that is editionable |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View USER_EDITIONED_TYPES lists the types that are editioned by default for the current user. This view does not display the SCHEMA column. See Also: " USER_EDITIONED_TYPES " See Also: " USER_EDITIONED_TYPES "