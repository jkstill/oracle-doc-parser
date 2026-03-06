---
id: 19c__DBA_USED_SYSPRIVS
name: DBA_USED_SYSPRIVS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [dba]
source_file: DBA_USED_SYSPRIVS.html
---

# DBA_USED_SYSPRIVS

DBA_USED_SYSPRIVS lists the system privileges (without privilege grant paths) that are used for the privilege analysis policies reported by the DBMS_PRIVILEGE_CAPTURE.GENERATE_RESULT procedure.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CAPTURE | VARCHAR2(128) | Name of a privilege analysis policy |
| SEQUENCE | NUMBER | The sequence number of the privilege analysis run during which the privilege was used |
| OS_USER | VARCHAR2(128) | Operating system login username |
| USERHOST | VARCHAR2(128) | Client host machine name |
| MODULE | VARCHAR2(64) | Module name |
| USERNAME | VARCHAR2(128) | Name of the user whose privilege was reported |
| USED_ROLE | VARCHAR2(128) | Used role |
| SYS_PRIV | VARCHAR2(40) | Used system privilege |
| ADMIN_OPTION | NUMBER | Indicates whether the ADMIN option was used: 0 - Indicates that the ADMIN option was not used 1 - Indicates that the ADMIN option was used |
| RUN_NAME | VARCHAR2(128) | The name of the run during which the privilege was reported |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view provides access to analyzed privilege records in SYS tables. You must have the CAPTURE_ADMIN role to access this view. See Also: " DBA_USED_SYSPRIVS_PATH " for privilege grant path information for used system privileges Oracle Database Security Guide for more information about privilege analysis Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_PRIVILEGE_CAPTURE.GENERATE_RESULT procedure See Also: " DBA_USED_SYSPRIVS_PATH " for privilege grant path information for used system privileges Oracle Database Security Guide for more information about privilege analysis Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_PRIVILEGE_CAPTURE.GENERATE_RESULT procedure