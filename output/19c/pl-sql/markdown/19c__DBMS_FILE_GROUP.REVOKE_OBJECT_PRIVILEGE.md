---
id: 19c__DBMS_FILE_GROUP.REVOKE_OBJECT_PRIVILEGE
name: DBMS_FILE_GROUP.REVOKE_OBJECT_PRIVILEGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FILE_GROUP
tags: [dbms_file_group]
source_file: DBMS_FILE_GROUP.html
---

# DBMS_FILE_GROUP.REVOKE_OBJECT_PRIVILEGE

This procedure revokes object privileges on a file group from a user.

## Syntax

```sql
DBMS_FILE_GROUP.REVOKE_OBJECT_PRIVILEGE(
  object_name  IN  VARCHAR2,
  privilege    IN  BINARY_INTEGER,
  revokee      IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_name | VARCHAR2 | IN | The name of the file group on which the privilege is revoked, specified as [schema_name.]file_group_name . For example, if the schema is hq_dba and the file group name is sales_tbs , then specify hq_dba.sales_tbs . If the schema is not specified, then the current user is the default. |
| privilege | BINARY_INTEGER | IN | The constant that specifies the privilege. See " Constants " for valid privileges. |
| revokee | VARCHAR2) | IN | The name of the user or role from which the privilege is revoked. The user who owns the object cannot be specified. |

## Usage Notes

Syntax DBMS_FILE_GROUP.REVOKE_OBJECT_PRIVILEGE( object_name IN VARCHAR2, privilege IN BINARY_INTEGER, revokee IN VARCHAR2); Parameters Table 70-15 REVOKE_OBJECT_PRIVILEGE Procedure Parameters Parameter Description object_name The name of the file group on which the privilege is revoked, specified as [schema_name.]file_group_name . For example, if the schema is hq_dba and the file group name is sales_tbs , then specify hq_dba.sales_tbs . If the schema is not specified, then the current user is the default. privilege The constant that specifies the privilege. See " Constants " for valid privileges. revokee The name of the user or role from which the privilege is revoked. The user who owns the object cannot be specified.