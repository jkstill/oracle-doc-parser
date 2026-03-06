---
id: 19c__DBA_UNUSED_OBJPRIVS_PATH
name: DBA_UNUSED_OBJPRIVS_PATH
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [dba]
source_file: DBA_UNUSED_OBJPRIVS_PATH.html
---

# DBA_UNUSED_OBJPRIVS_PATH

DBA_UNUSED_OBJPRIVS_PATH lists the object privileges that are not used for the privilege analysis policies reported by the DBMS_PRIVILEGE_CAPTURE.GENERATE_RESULT procedure.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CAPTURE | VARCHAR2(128) | Name of the privilege analysis policy |
| USERNAME | VARCHAR2(128) | Name of the user whose privileges are reported |
| ROLENAME | VARCHAR2(128) | Name of the role whose unused privileges are reported (for ROLE type privilege analysis or ROLE AND CONTEXT privilege analysis) |
| OBJ_PRIV | VARCHAR2(40) | Unused object privilege |
| OBJECT_OWNER | VARCHAR2(128) | Object owner |
| OBJECT_NAME | VARCHAR2(128) | Name of the object that USERNAME has OBJ_PRIV on |
| OBJECT_TYPE | VARCHAR2(23) | Type of the object that USERNAME has OBJ_PRIV on |
| COLUMN_NAME | VARCHAR2(128) | Name of the column that USERNAME has OBJ_PRIV on |
| GRANT_OPTION | NUMBER | Indicates whether the privilege is granted with the GRANT option: 0 - Indicates that the privilege is granted without the GRANT option 1 - Indicates that the privilege is granted with the GRANT option |
| PATH | GRANT_PATH | Object privilege grant paths |
| RUN_NAME | VARCHAR2(128) | The name of the run during which the privilege was reported |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view provides access to analyzed privilege records in SYS tables. You must have the CAPTURE_ADMIN role to access this view. See Also: " DBA_USED_OBJPRIVS_PATH " " DBA_UNUSED_OBJPRIVS " Oracle Database Security Guide for more information about privilege analysis Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_PRIVILEGE_CAPTURE.GENERATE_RESULT procedure See Also: " DBA_USED_OBJPRIVS_PATH " " DBA_UNUSED_OBJPRIVS " Oracle Database Security Guide for more information about privilege analysis Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_PRIVILEGE_CAPTURE.GENERATE_RESULT procedure