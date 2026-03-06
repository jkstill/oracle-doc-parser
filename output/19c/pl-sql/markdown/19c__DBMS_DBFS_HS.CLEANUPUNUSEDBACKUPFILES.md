---
id: 19c__DBMS_DBFS_HS.CLEANUPUNUSEDBACKUPFILES
name: DBMS_DBFS_HS.CLEANUPUNUSEDBACKUPFILES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_HS
tags: [dbms_dbfs_hs]
source_file: DBMS_DBFS_HS.html
---

# DBMS_DBFS_HS.CLEANUPUNUSEDBACKUPFILES

This procedure removes files created on the external storage device that hold no currently used data in them.

## Syntax

```sql
DBMS_DBFS_HS.CLEANUPUNUSEDBACKUPFILES (
   store_name     IN     VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2) | IN | Name of store |

## Usage Notes

Syntax DBMS_DBFS_HS.CLEANUPUNUSEDBACKUPFILES ( store_name IN VARCHAR2); Parameters Table 54-6 CLEANUPUNUSEDBACKUPFILES Procedure Parameters Parameter Description store_name Name of store Usage Notes The action of removing files from external storage device can not be rolled back. This method can be executed periodically to clear space on the external storage device. Asynchronously deleting content from the external storage device is useful because it has minimal impact on the OLTP performance. The periodic scheduling can be accomplished using the DBMS_SCHEDULER package.