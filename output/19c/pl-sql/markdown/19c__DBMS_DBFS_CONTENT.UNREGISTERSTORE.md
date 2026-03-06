---
id: 19c__DBMS_DBFS_CONTENT.UNREGISTERSTORE
name: DBMS_DBFS_CONTENT.UNREGISTERSTORE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.UNREGISTERSTORE

This procedure unregisters a previously registered store (invalidating all mount points associated with it).

## Syntax

```sql
DBMS_DBFS_CONTENT.UNREGISTERSTORE (
   store_name          IN      VARCHAR2,
   ignore_unknown      IN      BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of store |
| ignore_unknown | BOOLEAN | IN | If TRUE , attempts to unregister unknown stores will not raise an exception. |

## Usage Notes

Syntax DBMS_DBFS_CONTENT.UNREGISTERSTORE ( store_name IN VARCHAR2, ignore_unknown IN BOOLEAN DEFAULT FALSE); Parameters Table 52-79 UNREGISTERSTORE Procedure Parameters Parameter Description store_name Name of store ignore_unknown If TRUE , attempts to unregister unknown stores will not raise an exception. Usage Notes Once unregistered all access to the store (and its mount points) are not guaranteed to work If the ignore_unknown argument is TRUE , attempts to unregister unknown stores do not raise an exception.