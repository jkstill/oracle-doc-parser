---
id: 19c__DBMS_FILE_GROUP.REVOKE_SYSTEM_PRIVILEGE
name: DBMS_FILE_GROUP.REVOKE_SYSTEM_PRIVILEGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FILE_GROUP
tags: [dbms_file_group]
source_file: DBMS_FILE_GROUP.html
---

# DBMS_FILE_GROUP.REVOKE_SYSTEM_PRIVILEGE

This procedure revokes system privileges for file group operations from a user.

## Syntax

```sql
DBMS_FILE_GROUP.REVOKE_SYSTEM_PRIVILEGE(
  privilege  IN  BINARY_INTEGER,
  revokee    IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| privilege | BINARY_INTEGER | IN | The constant that specifies the privilege. See " Constants " for valid privileges. |
| revokee | VARCHAR2) | IN | The name of the user or role from which the privilege is revoked. The user who runs the procedure cannot be specified. |

## Usage Notes

Syntax DBMS_FILE_GROUP.REVOKE_SYSTEM_PRIVILEGE( privilege IN BINARY_INTEGER, revokee IN VARCHAR2); Parameters Table 70-16 REVOKE_SYSTEM_PRIVILEGE Procedure Parameters Parameter Description privilege The constant that specifies the privilege. See " Constants " for valid privileges. revokee The name of the user or role from which the privilege is revoked. The user who runs the procedure cannot be specified.