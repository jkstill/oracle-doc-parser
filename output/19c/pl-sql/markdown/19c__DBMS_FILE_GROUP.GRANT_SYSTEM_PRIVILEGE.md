---
id: 19c__DBMS_FILE_GROUP.GRANT_SYSTEM_PRIVILEGE
name: DBMS_FILE_GROUP.GRANT_SYSTEM_PRIVILEGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FILE_GROUP
tags: [dbms_file_group]
source_file: DBMS_FILE_GROUP.html
---

# DBMS_FILE_GROUP.GRANT_SYSTEM_PRIVILEGE

This procedure grants system privileges for file group operations to a user.

## Syntax

```sql
DBMS_FILE_GROUP.GRANT_SYSTEM_PRIVILEGE(
  privilege     IN  BINARY_INTEGER,
  grantee       IN  VARCHAR2,
  grant_option  IN  BOOLEAN  DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| privilege | BINARY_INTEGER | IN | The constant that specifies the privilege. See " Constants " for valid privileges. |
| grantee | VARCHAR2 | IN | The name of the user or role for which the privilege is granted. The user who runs the procedure cannot be specified. |
| grant_option | BOOLEAN | IN | If TRUE , then the specified user granted the specified privilege can grant this privilege to others. If FALSE , then the specified user granted the specified privilege cannot grant this privilege to others. |

## Usage Notes

Syntax DBMS_FILE_GROUP.GRANT_SYSTEM_PRIVILEGE( privilege IN BINARY_INTEGER, grantee IN VARCHAR2, grant_option IN BOOLEAN DEFAULT FALSE); Parameters Table 70-12 GRANT_SYSTEM_PRIVILEGE Procedure Parameters Parameter Description privilege The constant that specifies the privilege. See " Constants " for valid privileges. grantee The name of the user or role for which the privilege is granted. The user who runs the procedure cannot be specified. grant_option If TRUE , then the specified user granted the specified privilege can grant this privilege to others. If FALSE , then the specified user granted the specified privilege cannot grant this privilege to others.