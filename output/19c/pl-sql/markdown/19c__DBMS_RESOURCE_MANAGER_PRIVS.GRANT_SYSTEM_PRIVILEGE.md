---
id: 19c__DBMS_RESOURCE_MANAGER_PRIVS.GRANT_SYSTEM_PRIVILEGE
name: DBMS_RESOURCE_MANAGER_PRIVS.GRANT_SYSTEM_PRIVILEGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER_PRIVS
tags: [dbms_resource_manager_privs]
source_file: DBMS_RESOURCE_MANAGER_PRIVS.html
---

# DBMS_RESOURCE_MANAGER_PRIVS.GRANT_SYSTEM_PRIVILEGE

This procedure performs a grant of a system privilege to a user or role.

## Syntax

```sql
DBMS_RESOURCE_MANAGER_PRIVS.GRANT_SYSTEM_PRIVILEGE (
   grantee_name    IN VARCHAR2, 
   privilege_name  IN VARCHAR2 DEFAULT 'ADMINISTER_RESOURCE_MANAGER',             
   admin_option    IN BOOLEAN);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| grantee_name | VARCHAR2 | IN | Name of the user or role to whom privilege is to be granted. |
| privilege_name | VARCHAR2 | IN | Name of the privilege to be granted. |
| admin_option | BOOLEAN) | IN | TRUE if the grant is with admin_option , FALSE otherwise. |

## Usage Notes

Syntax DBMS_RESOURCE_MANAGER_PRIVS.GRANT_SYSTEM_PRIVILEGE ( grantee_name IN VARCHAR2, privilege_name IN VARCHAR2 DEFAULT 'ADMINISTER_RESOURCE_MANAGER', admin_option IN BOOLEAN); Parameters Table 143-3 GRANT_SYSTEM_PRIVILEGE Procedure Parameters Parameter Description grantee_name Name of the user or role to whom privilege is to be granted. privilege_name Name of the privilege to be granted. admin_option TRUE if the grant is with admin_option , FALSE otherwise. Usage Notes Currently, Oracle provides only one system privilege for the Resource Manager: ADMINISTER_RESOURCE_MANAGER . Database administrators have this system privilege with the ADMIN option. The grantee and the revokee can either be a user or a role. Users that have been granted the system privilege with the ADMIN option can also grant this privilege to others. Examples The following call grants this privilege to a user called scott without the ADMIN option: BEGIN DBMS_RESOURCE_MANAGER_PRIVS.GRANT_SYSTEM_PRIVILEGE ( grantee_name => 'scott', privilege_name => 'ADMINISTER_RESOURCE_MANAGER', admin_option => FALSE); END; /