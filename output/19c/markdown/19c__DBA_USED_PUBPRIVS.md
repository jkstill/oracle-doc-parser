---
id: 19c__DBA_USED_PUBPRIVS
name: DBA_USED_PUBPRIVS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [dba]
source_file: DBA_USED_PUBPRIVS.html
---

# DBA_USED_PUBPRIVS

DBA_USED_PUBPRIVS lists the privileges that are used from the PUBLIC role for the privilege analysis policies reported by the DBMS_PRIVILEGE_CAPTURE.GENERATE_RESULT procedure.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CAPTURE | VARCHAR2(128) | Name of a privilege analysis policy |
| SEQUENCE | NUMBER | The sequence number of the privilege analysis run during which the privilege was reported |
| OS_USER | VARCHAR2(128) | Operating system login username |
| USERHOST | VARCHAR2(128) | Client host machine name |
| MODULE | VARCHAR2(64) | Module name |
| USERNAME | VARCHAR2(128) | Name of the user who used the privilege from the PUBLIC role |
| SYS_PRIV | VARCHAR2(40) | Used system privilege |
| OBJ_PRIV | VARCHAR2(40) | Used object privilege |
| OBJECT_OWNER | VARCHAR2(128) | Object owner |
| OBJECT_NAME | VARCHAR2(128) | Name of the object that OBJ_PRIV is used to access |
| OBJECT_TYPE | VARCHAR2(23) | Type of the object that OBJ_PRIV is used to access |
| OPTION$ | NUMBER | Indicates whether the GRANT option or the ADMIN option was used: 0 - Indicates that the GRANT option or ADMIN option was not used 1 - Indicates that the GRANT option or ADMIN option was used |
| RUN_NAME | VARCHAR2(128) | The name of the run during which the privilege was reported |

## Usage Notes

This view provides access to analyzed privilege records in SYS tables. You must have the CAPTURE_ADMIN role to access this view. See Also: Oracle Database Security Guide for more information about privilege analysis Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_PRIVILEGE_CAPTURE.GENERATE_RESULT procedure See Also: Oracle Database Security Guide for more information about privilege analysis Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_PRIVILEGE_CAPTURE.GENERATE_RESULT procedure