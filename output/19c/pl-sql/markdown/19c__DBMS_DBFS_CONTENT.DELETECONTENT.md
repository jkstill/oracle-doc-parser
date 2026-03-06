---
id: 19c__DBMS_DBFS_CONTENT.DELETECONTENT
name: DBMS_DBFS_CONTENT.DELETECONTENT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.DELETECONTENT

This procedure deletes the file specified by the given contentID.

## Syntax

```sql
DBMS_DBFS_CONTENT.DELETECONTENT (
   store_name     IN     VARCHAR2    DEFAULT NULL,
   contentID      IN     RAW,
   filter         IN     VARCHAR2    DEFAULT NULL,
   soft_delete    IN     BOOLEAN     DEFAULT NULL,
   principal      IN     VARCHAR2    DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of store |
| contentID | RAW | IN | Unique identifier for the file to be deleted |
| filter | VARCHAR2 | IN | A filter, if any, to be applied |
| soft_delete | BOOLEAN | IN | If 0, execute a hard (permanent) delete. For any value other than 0, perform a soft delete (see Oracle Database SecureFiles and Large Objects Developer's Guide , Deletion Operations). |
| principal | VARCHAR2 | IN | File system user for whom the access check is made |

## Usage Notes

Syntax DBMS_DBFS_CONTENT.DELETECONTENT ( store_name IN VARCHAR2 DEFAULT NULL, contentID IN RAW, filter IN VARCHAR2 DEFAULT NULL, soft_delete IN BOOLEAN DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL); Parameters Table 52-27 DELETECONTENT Procedure Parameters Parameter Description store_name Name of store contentID Unique identifier for the file to be deleted filter A filter, if any, to be applied soft_delete If 0, execute a hard (permanent) delete. For any value other than 0, perform a soft delete (see Oracle Database SecureFiles and Large Objects Developer's Guide , Deletion Operations). principal File system user for whom the access check is made