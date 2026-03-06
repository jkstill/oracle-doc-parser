---
id: 19c__DBMS_RESOURCE_MANAGER_PRIVS.REVOKE_SYSTEM_PRIVILEGE
name: DBMS_RESOURCE_MANAGER_PRIVS.REVOKE_SYSTEM_PRIVILEGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER_PRIVS
tags: [dbms_resource_manager_privs]
source_file: DBMS_RESOURCE_MANAGER_PRIVS.html
---

# DBMS_RESOURCE_MANAGER_PRIVS.REVOKE_SYSTEM_PRIVILEGE

This procedure performs a revoke of a system privilege from a user or role.

## Syntax

```sql
DBMS_RESOURCE_MANAGER_PRIVS.REVOKE_SYSTEM_PRIVILEGE (
   revokee_name   IN VARCHAR2, 
   privilege_name IN VARCHAR2 DEFAULT 'ADMINISTER_RESOURCE_MANAGER');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| revokee_name | VARCHAR2 | IN | Name of the user or role from whom privilege is to be revoked. |
| privilege_name | VARCHAR2 | IN | Name of the privilege to be revoked. |

## Usage Notes

Syntax DBMS_RESOURCE_MANAGER_PRIVS.REVOKE_SYSTEM_PRIVILEGE ( revokee_name IN VARCHAR2, privilege_name IN VARCHAR2 DEFAULT 'ADMINISTER_RESOURCE_MANAGER'); Parameters Table 143-5 REVOKE_SYSTEM_PRIVILEGE Procedure Parameters Parameter Description revokee_name Name of the user or role from whom privilege is to be revoked. privilege_name Name of the privilege to be revoked. Examples The following call revokes the ADMINISTER_RESOURCE_MANAGER from user scott: BEGIN DBMS_RESOURCE_MANAGER_PRIVS.REVOKE_SYSTEM_PRIVILEGE ('scott'); END; /