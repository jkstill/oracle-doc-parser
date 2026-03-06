---
id: 19c__DBMS_RESCONFIG.DELETEREPOSITORYRESCONFIG
name: DBMS_RESCONFIG.DELETEREPOSITORYRESCONFIG
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESCONFIG
tags: [dbms_resconfig]
source_file: DBMS_RESCONFIG.html
---

# DBMS_RESCONFIG.DELETEREPOSITORYRESCONFIG

This procedure removes the configuration at the given position in the repository's configuration list. It shifts any subsequent elements to the left.

## Syntax

```sql
DBMS_RESCONFIG.DELETEREPOSITORYRESCONFIG(
   pos           IN   PLS_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pos | PLS_INTEGER) | IN | The index of the configuration to be removed. An exception is raised if the index is out of range ( pos < 0 or pos >= the size of the target resource's configuration list). |

## Usage Notes

Syntax DBMS_RESCONFIG.DELETEREPOSITORYRESCONFIG( pos IN PLS_INTEGER); Parameters Table 141-5 DELETEREPOSITORYRESCONFIG Function Parameters Parameter Description pos The index of the configuration to be removed. An exception is raised if the index is out of range ( pos < 0 or pos >= the size of the target resource's configuration list). Usage Notes Users must have XDBADMIN role to execute this. This statement is treated as if it is a DDL statement. This means the system will implicitly commit before and after this statement.