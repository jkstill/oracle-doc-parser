---
id: 19c__ALL_CODE_ROLE_PRIVS
name: ALL_CODE_ROLE_PRIVS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [all]
source_file: ALL_CODE_ROLE_PRIVS.html
---

# ALL_CODE_ROLE_PRIVS

ALL_CODE_ROLE_PRIVS describes all the roles that are associated with program units owned or accessible by the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Username of the owner of the object |
| OBJECT_NAME | VARCHAR2(128) | Name of the object |
| OBJECT_TYPE | VARCHAR2(9) | Type of the object |
| ROLE | VARCHAR2(128) | The role associated with the object |

## Usage Notes

Related Views DBA_CODE_ROLE_PRIVS describes all the roles that are associated with program units in the database. USER_CODE_ROLE_PRIVS describes all the roles that are associated with program units owned by current user. This view does not display the OWNER column. See Also: " DBA_CODE_ROLE_PRIVS " " USER_CODE_ROLE_PRIVS " Oracle Database Security Guide for more information about granting and revoking roles to and from program units See Also: " DBA_CODE_ROLE_PRIVS " " USER_CODE_ROLE_PRIVS " Oracle Database Security Guide for more information about granting and revoking roles to and from program units