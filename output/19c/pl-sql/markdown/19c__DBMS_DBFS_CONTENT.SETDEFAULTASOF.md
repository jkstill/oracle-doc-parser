---
id: 19c__DBMS_DBFS_CONTENT.SETDEFAULTASOF
name: DBMS_DBFS_CONTENT.SETDEFAULTASOF
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.SETDEFAULTASOF

This procedure sets the "as of" parameter of the default context. This information can be inserted explicitly by way of argument into other method calls, allowing for a more fine-grained control.

## Syntax

```sql
DBMS_DBFS_CONTENT.SETDEFAULTASOF (
  asof    IN     TIMESTAMP);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| asof | TIMESTAMP) | IN | The "as of" timestamp at which the underlying read-only operation (or its read-only sub-components) executes |

## Usage Notes

Syntax DBMS_DBFS_CONTENT.SETDEFAULTASOF ( asof IN TIMESTAMP); Parameters Table 52-67 SETDEFAULTASOF Procedure Parameters Parameter Description asof The "as of" timestamp at which the underlying read-only operation (or its read-only sub-components) executes Usage Notes NULL by default, this parameter be can be cleared by setting it to NULL . The parameters, once set, remain as a default for the duration of the session, and is inherited by all operations for which the default is not explicitly overridden.