---
id: 19c__DBMS_DBFS_CONTENT.GETDEFAULTPRINCIPAL
name: DBMS_DBFS_CONTENT.GETDEFAULTPRINCIPAL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.GETDEFAULTPRINCIPAL

This procedure returns the "principal" parameter of the default context. This information contained can be inserted explicitly by way of argument into other method calls, allowing for a more fine-grained control.

## Syntax

```sql
DBMS_DBFS_CONTENT.GETDEFAULTPRINCIPAL (
   principal    OUT NOCOPY     VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| principal | NOCOPY | OUT | Agent (principal) invoking the current operation |

## Usage Notes

Syntax DBMS_DBFS_CONTENT.GETDEFAULTPRINCIPAL ( principal OUT NOCOPY VARCHAR2); Parameters Table 52-35 GETDEFAULTPRINCIPAL Procedure Parameters Parameter Description principal Agent (principal) invoking the current operation