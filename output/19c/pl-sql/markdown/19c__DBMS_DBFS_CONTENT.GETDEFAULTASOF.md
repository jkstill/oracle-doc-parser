---
id: 19c__DBMS_DBFS_CONTENT.GETDEFAULTASOF
name: DBMS_DBFS_CONTENT.GETDEFAULTASOF
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.GETDEFAULTASOF

This procedure returns the "as of" parameter of the default context. This information can be inserted explicitly by way of argument into other method calls, allowing for a more fine-grained control.

## Syntax

```sql
DBMS_DBFS_CONTENT.GETDEFAULTASOF (
  asof    OUT NOCOPY     TIMESTAMP);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| asof | NOCOPY | OUT | The "as of" timestamp at which the underlying read-only operation (or its read-only sub-components) executes |

## Usage Notes

Syntax DBMS_DBFS_CONTENT.GETDEFAULTASOF ( asof OUT NOCOPY TIMESTAMP); Parameters Table 52-32 GETDEFAULTASOF Procedure Parameters Parameter Description asof The "as of" timestamp at which the underlying read-only operation (or its read-only sub-components) executes