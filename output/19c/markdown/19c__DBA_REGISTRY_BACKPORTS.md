---
id: 19c__DBA_REGISTRY_BACKPORTS
name: DBA_REGISTRY_BACKPORTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_REGISTRY_BACKPORTS.html
---

# DBA_REGISTRY_BACKPORTS

DBA_REGISTRY_BACKPORTS displays backported bug fixes that were applied to the database. This view displays only bug fixes that changed the data dictionary of the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| BUGNO | NUMBER | Bug number |
| VERSION_FULL | VARCHAR2(30) | Component full version |
| COMP_ID | VARCHAR2(30) | Component identifier |
| NAMESPACE | VARCHAR2(30) | Component namespace |
| BACKPORT_TYPE | VARCHAR2(30) | Type of backported bug fix The value of this columns is always DICTIONARY , which indicates that the bug fix changed the data dictionary of the database. |
| BACKPORT_TIME | TIMESTAMP(6) | Date and time at which the backported bug fix was applied |

## Usage Notes

Note: This view is available starting with Oracle Database release 19c, version 19.1. Note: This view is available starting with Oracle Database release 19c, version 19.1.