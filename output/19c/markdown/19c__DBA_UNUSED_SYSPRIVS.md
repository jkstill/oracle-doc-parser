---
id: 19c__DBA_UNUSED_SYSPRIVS
name: DBA_UNUSED_SYSPRIVS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [dba]
source_file: DBA_UNUSED_SYSPRIVS.html
---

# DBA_UNUSED_SYSPRIVS

DBA_UNUSED_SYSPRIVS lists the system privileges (without privilege grant paths) that are not used for the privilege analysis policies reported by the DBMS_PRIVILEGE_CAPTURE.GENERATE_RESULT procedure.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CAPTURE | VARCHAR2(128) | Name of a privilege analysis policy |
| USERNAME | VARCHAR2(128) | Name of the user whose privileges are reported |
| ROLENAME | VARCHAR2(128) | Name of the role whose unused privileges are reported (for ROLE type privilege analysis or ROLE AND CONTEXT privilege analysis) |
| SYS_PRIV | VARCHAR2(40) | Unused system privilege |
| ADMIN_OPTION | NUMBER | Indicates whether the privilege is granted with the ADMIN option: 0 - Indicates that the privilege is granted without the ADMIN option 1 - Indicates that the privilege is granted with the ADMIN option |
| RUN_NAME | VARCHAR2(128) | The name of the run during which the privilege was reported |

## Usage Notes

This view provides access to analyzed privilege records in SYS tables. You must have the CAPTURE_ADMIN role to access this view. See Also: " DBA_UNUSED_SYSPRIVS_PATH " for privilege grant path information for unused system privileges Oracle Database Security Guide for more information about privilege analysis Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_PRIVILEGE_CAPTURE.GENERATE_RESULT procedure See Also: " DBA_UNUSED_SYSPRIVS_PATH " for privilege grant path information for unused system privileges Oracle Database Security Guide for more information about privilege analysis Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_PRIVILEGE_CAPTURE.GENERATE_RESULT procedure