---
id: 19c__DBMS_DBFS_CONTENT.GETDEFAULTCONTEXT
name: DBMS_DBFS_CONTENT.GETDEFAULTCONTEXT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.GETDEFAULTCONTEXT

This procedure returns the default context. The information contained in the context can be inserted explicitly by way of arguments to the various method calls, allowing for fine-grained control over individual operations.

## Syntax

```sql
DBMS_DBFS_CONTENT.GETDEFAULTCONTEXT (
   principal    OUT NOCOPY     VARCHAR2,
   owner        OUT NOCOPY     VARCHAR2,
   acl          OUT NOCOPY     VARCHAR2,
   asof         OUT NOCOPY     TIMESTAMP);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| principal | NOCOPY | OUT | Agent (principal) invoking the current operation |
| owner | NOCOPY | OUT | Owner for new elements created (implicitly or explicitly) by the current operation |
| acl | NOCOPY | OUT | ACL for all new elements created (implicitly or explicitly) by the current operation |
| asof | NOCOPY | OUT | The "as of" timestamp at which the underlying read-only operation (or its read-only sub-components) executes |

## Usage Notes

Syntax DBMS_DBFS_CONTENT.GETDEFAULTCONTEXT ( principal OUT NOCOPY VARCHAR2, owner OUT NOCOPY VARCHAR2, acl OUT NOCOPY VARCHAR2, asof OUT NOCOPY TIMESTAMP); Parameters Table 52-33 GETDEFAULTCONTEXT Procedure Parameters Parameter Description principal Agent (principal) invoking the current operation owner Owner for new elements created (implicitly or explicitly) by the current operation acl ACL for all new elements created (implicitly or explicitly) by the current operation asof The "as of" timestamp at which the underlying read-only operation (or its read-only sub-components) executes