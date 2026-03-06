---
id: 19c__DBMS_DBFS_CONTENT.UNMOUNTSTORE
name: DBMS_DBFS_CONTENT.UNMOUNTSTORE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.UNMOUNTSTORE

This procedure unmounts a registered store, either by name or by mount point.

## Syntax

```sql
DBMS_DBFS_CONTENT.UNMOUNTSTORE (
   store_name       IN      VARCHAR2   DEFAULT NULL,
   store_mount      IN      VARCHAR2   DEFAULT NULL,
   ignore_unknown   IN      BOOLEAN    DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of store |
| store_mount | VARCHAR2 | IN | Location at which the store instance is mounted |
| ignore_unknown | BOOLEAN | IN | If TRUE , attempts to unregister unknown stores will not raise an exception. |

## Usage Notes

Syntax DBMS_DBFS_CONTENT.UNMOUNTSTORE ( store_name IN VARCHAR2 DEFAULT NULL, store_mount IN VARCHAR2 DEFAULT NULL, ignore_unknown IN BOOLEAN DEFAULT FALSE); Parameters Table 52-78 UNMOUNTSTORE Procedure Parameters Parameter Description store_name Name of store store_mount Location at which the store instance is mounted ignore_unknown If TRUE , attempts to unregister unknown stores will not raise an exception. Usage Notes See Also: Oracle Database SecureFiles and Large Objects Developer's Guide for further information on unmounting a previously unmounted store See Also: Oracle Database SecureFiles and Large Objects Developer's Guide for further information on unmounting a previously unmounted store