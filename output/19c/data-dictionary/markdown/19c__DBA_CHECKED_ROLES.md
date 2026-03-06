---
id: 19c__DBA_CHECKED_ROLES
name: DBA_CHECKED_ROLES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [dba]
source_file: DBA_CHECKED_ROLES.html
---

# DBA_CHECKED_ROLES

DBA_CHECKED_ROLES lists the roles (without role grant paths) that are used for the role analysis policies reported by the DBMS__CAPTURE.GENERATE_RESULT procedure.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CAPTURE | VARCHAR2(128) | Name of a role analysis policy |
| SEQUENCE | NUMBER | The sequence number of the role analysis run during which the role was reported |
| OS_USER | VARCHAR2(128) | Operating system login username |
| USERHOST | VARCHAR2(128) | Client host machine name |
| MODULE | VARCHAR2(64) | Module name |
| USERNAME | VARCHAR2(128) | Name of the user whose role was reported |
| CHECKED_ROLE | VARCHAR2(128) | Checked role |
| RUN_NAME | VARCHAR2(128) | The name of the run during which the role was reported |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view provides access to analyzed role records in SYS tables. You must have the CAPTURE_ADMIN role to access this view. See Also: " DBA_CHECKED_ROLES_PATH " See Also: " DBA_CHECKED_ROLES_PATH "