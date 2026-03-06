---
id: 19c__DBMS_DBFS_CONTENT_SPI.DELETEDIRECTORY
name: DBMS_DBFS_CONTENT_SPI.DELETEDIRECTORY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT_SPI
tags: [dbms_dbfs_content_spi]
source_file: DBMS_DBFS_CONTENT_SPI.html
---

# DBMS_DBFS_CONTENT_SPI.DELETEDIRECTORY

This procedure deletes a directory.

## Syntax

```sql
DBMS_DBFS_CONTENT_SPI.DELETEDIRECTORY (
   store_name     IN     VARCHAR2,
   path           IN     VARCHAR2,
   filter         IN     VARCHAR2,
   soft_delete    IN     INTEGER,
   recurse        IN     INTEGER,
   ctx            IN     DBMS_DBFS_CONTENT_CONTEXT_T);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of store |
| path | VARCHAR2 | IN | Name of path to the directory |
| filter | VARCHAR2 | IN | A filter, if any, to be applied |
| soft_delete | INTEGER | IN | If 0, execute a hard (permanent) delete. For any value other than 0, perform a soft delete see Oracle Database SecureFiles and Large Objects Developer's Guide , Deletion Operations). |
| recurse | INTEGER | IN | If 0, do not execute recursively. Otherwise, recursively delete the directories and files below the given directory. |
| ctx | DBMS_DBFS_CONTENT_CONTEXT_T) | IN | Context with which to delete the directory (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type ) |

## Usage Notes

Syntax If recurse is nonzero, it recursively deletes all elements of the directory. A filter, if supplied, determines which elements of the directory are deleted. DBMS_DBFS_CONTENT_SPI.DELETEDIRECTORY ( store_name IN VARCHAR2, path IN VARCHAR2, filter IN VARCHAR2, soft_delete IN INTEGER, recurse IN INTEGER, ctx IN DBMS_DBFS_CONTENT_CONTEXT_T); Parameters Table 53-9 DELETEDIRECTORY Procedure Parameters Parameter Description store_name Name of store path Name of path to the directory filter A filter, if any, to be applied soft_delete If 0, execute a hard (permanent) delete. For any value other than 0, perform a soft delete see Oracle Database SecureFiles and Large Objects Developer's Guide , Deletion Operations). recurse If 0, do not execute recursively. Otherwise, recursively delete the directories and files below the given directory. ctx Context with which to delete the directory (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type )