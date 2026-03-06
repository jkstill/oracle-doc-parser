---
id: 19c__DBMS_DBFS_CONTENT_SPI.DELETECONTENT
name: DBMS_DBFS_CONTENT_SPI.DELETECONTENT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT_SPI
tags: [dbms_dbfs_content_spi]
source_file: DBMS_DBFS_CONTENT_SPI.html
---

# DBMS_DBFS_CONTENT_SPI.DELETECONTENT

This procedure deletes the file specified by the given contentID.

## Syntax

```sql
DBMS_DBFS_CONTENT_SPI.DELETECONTENT (
   store_name     IN     VARCHAR2,
   contentID      IN     RAW,
   filter         IN     VARCHAR2,
   soft_delete    IN     INTEGER,
   ctx            IN     DBMS_DBFS_CONTENT_CONTEXT_T);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of store |
| contentID | RAW | IN | Unique identifier for the file to be deleted |
| filter | VARCHAR2 | IN | A filter, if any, to be applied |
| soft_delete | INTEGER | IN | If 0, execute a hard (permanent) delete. For any value other than 0, perform a soft delete see Oracle Database SecureFiles and Large Objects Developer's Guide , Deletion Operations). |
| ctx | DBMS_DBFS_CONTENT_CONTEXT_T) | IN | Context with which to delete the file (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type ) |

## Usage Notes

Syntax DBMS_DBFS_CONTENT_SPI.DELETECONTENT ( store_name IN VARCHAR2, contentID IN RAW, filter IN VARCHAR2, soft_delete IN INTEGER, ctx IN DBMS_DBFS_CONTENT_CONTEXT_T); Parameters Table 53-8 DELETECONTENT Procedure Parameters Parameter Description store_name Name of store contentID Unique identifier for the file to be deleted filter A filter, if any, to be applied soft_delete If 0, execute a hard (permanent) delete. For any value other than 0, perform a soft delete see Oracle Database SecureFiles and Large Objects Developer's Guide , Deletion Operations). ctx Context with which to delete the file (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type )