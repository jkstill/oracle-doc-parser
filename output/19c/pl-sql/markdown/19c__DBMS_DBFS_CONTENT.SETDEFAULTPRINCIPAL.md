---
id: 19c__DBMS_DBFS_CONTENT.SETDEFAULTPRINCIPAL
name: DBMS_DBFS_CONTENT.SETDEFAULTPRINCIPAL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.SETDEFAULTPRINCIPAL

This procedure sets the "principal" parameter of the default context. This information contained can be inserted explicitly by way of argument into other method calls, allowing for a more fine-grained control.

## Syntax

```sql
DBMS_DBFS_CONTENT.SETDEFAULTPRINCIPAL (
   principal    IN     VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| principal | VARCHAR2) | IN | Agent (principal) invoking the current operation |

## Usage Notes

Syntax DBMS_DBFS_CONTENT.SETDEFAULTPRINCIPAL ( principal IN VARCHAR2); Parameters Table 52-70 SETDEFAULTPRINCIPAL Procedure Parameters Parameter Description principal Agent (principal) invoking the current operation Usage Notes NULL by default, this parameter be can be cleared by setting it to NULL . The parameters, once set, remain as a default for the duration of the session, and is inherited by all operations for which the default is not explicitly overridden.