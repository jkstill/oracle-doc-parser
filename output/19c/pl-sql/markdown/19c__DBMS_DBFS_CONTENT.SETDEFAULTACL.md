---
id: 19c__DBMS_DBFS_CONTENT.SETDEFAULTACL
name: DBMS_DBFS_CONTENT.SETDEFAULTACL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.SETDEFAULTACL

This procedure sets the ACL parameter of the default context.

## Syntax

```sql
DBMS_DBFS_CONTENT.SETDEFAULTACL (
   acl    IN     VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| acl | VARCHAR2) | IN | ACL for all new elements created (implicitly or explicitly) by the current operation |

## Usage Notes

This information can be inserted explicitly by way of argument into other method calls, allowing for a more fine-grained control. Syntax DBMS_DBFS_CONTENT.SETDEFAULTACL ( acl IN VARCHAR2); Parameters Table 52-66 SETDEFAULTACL Procedure Parameters Parameter Description acl ACL for all new elements created (implicitly or explicitly) by the current operation Usage Notes NULL by default, this parameter be can be cleared by setting it to NULL . The parameters, once set, remain as a default for the duration of the session, and is inherited by all operations for which the default is not explicitly overridden.