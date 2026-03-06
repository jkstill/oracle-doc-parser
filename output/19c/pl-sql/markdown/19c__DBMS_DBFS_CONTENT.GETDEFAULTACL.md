---
id: 19c__DBMS_DBFS_CONTENT.GETDEFAULTACL
name: DBMS_DBFS_CONTENT.GETDEFAULTACL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.GETDEFAULTACL

This procedure returns the ACL parameter of the default context. This information can be inserted explicitly by way of argument into other method calls, allowing for a more fine-grained control.

## Syntax

```sql
DBMS_DBFS_CONTENT.GETDEFAULTACL (
   acl    OUT NOCOPY     VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| acl | NOCOPY | OUT | ACL for all new elements created (implicitly or explicitly) by the current operation |

## Usage Notes

Syntax DBMS_DBFS_CONTENT.GETDEFAULTACL ( acl OUT NOCOPY VARCHAR2); Parameters Table 52-31 GETDEFAULTACL Procedure Parameters Parameter Description acl ACL for all new elements created (implicitly or explicitly) by the current operation