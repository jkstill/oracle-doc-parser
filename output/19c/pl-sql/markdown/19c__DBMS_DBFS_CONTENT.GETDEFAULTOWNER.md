---
id: 19c__DBMS_DBFS_CONTENT.GETDEFAULTOWNER
name: DBMS_DBFS_CONTENT.GETDEFAULTOWNER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.GETDEFAULTOWNER

This procedure returns the "owner" parameter of the default context. This information can be inserted explicitly by way of argument into other method calls, allowing for a more fine-grained control.

## Syntax

```sql
DBMS_DBFS_CONTENT.GETDEFAULTOWNER (
   principal    IN     VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| owner |  |  | Owner for new elements created (implicitly or explicitly) by the current operation |

## Usage Notes

Syntax DBMS_DBFS_CONTENT.GETDEFAULTOWNER ( principal IN VARCHAR2); Parameters Table 52-34 GETDEFAULTOWNER Procedure Parameters Parameter Description owner Owner for new elements created (implicitly or explicitly) by the current operation