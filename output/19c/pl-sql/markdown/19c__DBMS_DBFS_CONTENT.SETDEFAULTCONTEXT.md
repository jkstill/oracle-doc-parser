---
id: 19c__DBMS_DBFS_CONTENT.SETDEFAULTCONTEXT
name: DBMS_DBFS_CONTENT.SETDEFAULTCONTEXT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.SETDEFAULTCONTEXT

This procedure sets the default context. The information contained in the context can be inserted explicitly by way of arguments to the various method calls, allowing for fine-grained control over individual operations.

## Syntax

```sql
DBMS_DBFS_CONTENT.SETDEFAULTCONTEXT (
   principal    IN     VARCHAR2,
   owner        IN     VARCHAR2,
   acl          IN     VARCHAR2,
   asof         IN     TIMESTAMP);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| principal | VARCHAR2 | IN | Agent (principal) invoking the current operation |
| owner | VARCHAR2 | IN | Owner for new elements created (implicitly or explicitly) by the current operation |
| acl | VARCHAR2 | IN | ACL for all new elements created (implicitly or explicitly) by the current operation |
| asof | TIMESTAMP) | IN | The "as of" timestamp at which the underlying read-only operation (or its read-only sub-components) executes |

## Usage Notes

Syntax DBMS_DBFS_CONTENT.SETDEFAULTCONTEXT ( principal IN VARCHAR2, owner IN VARCHAR2, acl IN VARCHAR2, asof IN TIMESTAMP); Parameters Table 52-68 SETDEFAULTCONTEXT Procedure Parameters Parameter Description principal Agent (principal) invoking the current operation owner Owner for new elements created (implicitly or explicitly) by the current operation acl ACL for all new elements created (implicitly or explicitly) by the current operation asof The "as of" timestamp at which the underlying read-only operation (or its read-only sub-components) executes Usage Notes All of the context parameters are NULL by default, and be can be cleared by setting them to NULL . The context parameters, once set, remain as defaults for the duration of the session, and are inherited by all operations for which the defaults are not explicitly overridden.