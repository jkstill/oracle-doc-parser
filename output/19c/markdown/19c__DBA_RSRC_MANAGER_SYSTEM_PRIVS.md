---
id: 19c__DBA_RSRC_MANAGER_SYSTEM_PRIVS
name: DBA_RSRC_MANAGER_SYSTEM_PRIVS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [dba]
source_file: DBA_RSRC_MANAGER_SYSTEM_PRIVS.html
---

# DBA_RSRC_MANAGER_SYSTEM_PRIVS

DBA_RSRC_MANAGER_SYSTEM_PRIVS displays information about all the users and roles that have been granted the ADMINISTER_RESOURCE_MANAGER system privilege, which is granted using the DBMS_RESOURCE_MANAGER_PRIVS package.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| GRANTEE | VARCHAR2(128) | User or role receiving the grant |
| PRIVILEGE | VARCHAR2(40) | Name of the system privilege |
| ADMIN_OPTION | VARCHAR2(3) | Indicates whether the grant was with the ADMIN option ( YES ) or not ( NO ) |

## Usage Notes

This privilege is not granted through the GRANT SQL statement. Related View USER_RSRC_MANAGER_SYSTEM_PRIVS displays information about the users who are granted system privileges for the DBMS_RESOURCE_MANAGER package. This view does not display the GRANTEE column. See Also: " USER_RSRC_MANAGER_SYSTEM_PRIVS " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_RESOURCE_MANAGER package See Also: " USER_RSRC_MANAGER_SYSTEM_PRIVS " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_RESOURCE_MANAGER package