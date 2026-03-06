---
id: 19c__USER_PRIVILEGE_MAP
name: USER_PRIVILEGE_MAP
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [user]
source_file: USER_PRIVILEGE_MAP.html
---

# USER_PRIVILEGE_MAP

USER_PRIVILEGE_MAP shows privilege (auditing option) type codes for object privileges that can be granted on a user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PRIVILEGE | NUMBER | A numeric privilege (auditing option) type code |
| NAME | VARCHAR2(40) | Name of the type of privilege (auditing option) |

## Usage Notes

This table can be used to map privilege type numbers to type names.