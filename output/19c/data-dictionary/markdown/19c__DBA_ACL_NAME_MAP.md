---
id: 19c__DBA_ACL_NAME_MAP
name: DBA_ACL_NAME_MAP
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_ACL_NAME_MAP.html
---

# DBA_ACL_NAME_MAP

DBA_ACL_NAME_MAP maps new names of the access control lists for PL/SQL network utility packages from old XDB names.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| XDB_NAME | VARCHAR2(4000) | The old XDB name of the access control list |
| ACL | VARCHAR2(128) | The new name of the access control list |
| ACL_OWNER | VARCHAR2(128) | The owner of the access control list |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content