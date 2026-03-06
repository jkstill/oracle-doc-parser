---
id: 19c__DBMS_DBFS_CONTENT_SPI.DELETEFILE
name: DBMS_DBFS_CONTENT_SPI.DELETEFILE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT_SPI
tags: [dbms_dbfs_content_spi]
source_file: DBMS_DBFS_CONTENT_SPI.html
---

# DBMS_DBFS_CONTENT_SPI.DELETEFILE

This procedure deletes the specified file.

## Syntax

```sql
DBMS_DBFS_CONTENT_SPI.DELETEFILE (
   store_name     IN     VARCHAR2,
   path           IN     VARCHAR2,
   filter         IN     VARCHAR2,
   soft_delete    IN     BOOLEAN,
   ctx            IN     DBMS_DBFS_CONTENT_CONTEXT_T);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of store |
| path | VARCHAR2 | IN | Name of path to the file |
| filter | VARCHAR2 | IN | A filter, if any, to be applied |
| soft_delete | BOOLEAN | IN | If 0, execute a hard (permanent) delete. For any value other than 0, perform a soft delete see Oracle Database SecureFiles and Large Objects Developer's Guide , Deletion Operations). |
| ctx | DBMS_DBFS_CONTENT_CONTEXT_T) | IN | Context with which to delete the file (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type ) |

## Usage Notes

Syntax DBMS_DBFS_CONTENT_SPI.DELETEFILE ( store_name IN VARCHAR2, path IN VARCHAR2, filter IN VARCHAR2, soft_delete IN BOOLEAN, ctx IN DBMS_DBFS_CONTENT_CONTEXT_T); Parameters Table 53-10 DELETEFILE Procedure Parameters Parameter Description store_name Name of store path Name of path to the file filter A filter, if any, to be applied soft_delete If 0, execute a hard (permanent) delete. For any value other than 0, perform a soft delete see Oracle Database SecureFiles and Large Objects Developer's Guide , Deletion Operations). ctx Context with which to delete the file (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type )