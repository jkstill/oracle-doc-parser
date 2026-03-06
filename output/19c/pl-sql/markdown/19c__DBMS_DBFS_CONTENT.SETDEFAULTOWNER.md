---
id: 19c__DBMS_DBFS_CONTENT.SETDEFAULTOWNER
name: DBMS_DBFS_CONTENT.SETDEFAULTOWNER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.SETDEFAULTOWNER

This procedure sets the "owner" parameter of the default context. This information can be inserted explicitly by way of argument into other method calls, allowing for a more fine-grained control.

## Syntax

```sql
DBMS_DBFS_CONTENT.SETDEFAULTOWNER (
   principal    IN     VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| owner |  |  | Owner for new elements created (implicitly or explicitly) by the current operation |

## Usage Notes

Syntax DBMS_DBFS_CONTENT.SETDEFAULTOWNER ( principal IN VARCHAR2); Parameters Table 52-69 SETDEFAULTOWNER Procedure Parameters Parameter Description owner Owner for new elements created (implicitly or explicitly) by the current operation Usage Notes NULL by default, this parameter be can be cleared by setting it to NULL . The parameters, once set, remain as a default for the duration of the session, and is inherited by all operations for which the default is not explicitly overridden.