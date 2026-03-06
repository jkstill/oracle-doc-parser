---
id: 19c__DBMS_FILE_GROUP.GRANT_OBJECT_PRIVILEGE
name: DBMS_FILE_GROUP.GRANT_OBJECT_PRIVILEGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FILE_GROUP
tags: [dbms_file_group]
source_file: DBMS_FILE_GROUP.html
---

# DBMS_FILE_GROUP.GRANT_OBJECT_PRIVILEGE

This procedure grants object privileges on a file group to a user.

## Syntax

```sql
DBMS_FILE_GROUP.GRANT_OBJECT_PRIVILEGE(
  object_name   IN  VARCHAR2,
  privilege     IN  BINARY_INTEGER,
  grantee       IN  VARCHAR2,
  grant_option  IN  BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_name | VARCHAR2 | IN | The name of the file group on which the privilege is granted, specified as [schema_name.]file_group_name . For example, if the schema is hq_dba and the file group name is sales_tbs , then specify hq_dba.sales_tbs . If the schema is not specified, then the current user is the default. |
| privilege | BINARY_INTEGER | IN | The constant that specifies the privilege. See " Constants " for valid privileges. |
| grantee | VARCHAR2 | IN | The name of the user or role for which the privilege is granted. The specified user cannot be the owner of the object. |
| grant_option | BOOLEAN | IN | If TRUE , then the specified user granted the specified privilege can grant this privilege to others. If FALSE , then the specified user granted the specified privilege cannot grant this privilege to others. |

## Usage Notes

Syntax DBMS_FILE_GROUP.GRANT_OBJECT_PRIVILEGE( object_name IN VARCHAR2, privilege IN BINARY_INTEGER, grantee IN VARCHAR2, grant_option IN BOOLEAN DEFAULT FALSE); Parameters Table 70-11 GRANT_OBJECT_PRIVILEGE Procedure Parameters Parameter Description object_name The name of the file group on which the privilege is granted, specified as [schema_name.]file_group_name . For example, if the schema is hq_dba and the file group name is sales_tbs , then specify hq_dba.sales_tbs . If the schema is not specified, then the current user is the default. privilege The constant that specifies the privilege. See " Constants " for valid privileges. grantee The name of the user or role for which the privilege is granted. The specified user cannot be the owner of the object. grant_option If TRUE , then the specified user granted the specified privilege can grant this privilege to others. If FALSE , then the specified user granted the specified privilege cannot grant this privilege to others. Usage Notes To run this procedure, a user must meet at least one of the following requirements: Be the owner of the object on which the privilege is granted Have the same privilege as the privilege being granted with the grant option