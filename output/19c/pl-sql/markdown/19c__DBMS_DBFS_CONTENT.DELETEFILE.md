---
id: 19c__DBMS_DBFS_CONTENT.DELETEFILE
name: DBMS_DBFS_CONTENT.DELETEFILE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.DELETEFILE

This procedure deletes the specified file.

## Syntax

```sql
DBMS_DBFS_CONTENT.DELETEFILE (
   path           IN     VARCHAR2,
   filter         IN     VARCHAR2    DEFAULT NULL,
   soft_delete    IN     BOOLEAN     DEFAULT NULL,
   store_name     IN     VARCHAR2    DEFAULT NULL,
   principal      IN     VARCHAR2    DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| path | VARCHAR2 | IN | Name of path to the file |
| filter | VARCHAR2 | IN | A filter, if any, to be applied |
| soft_delete | BOOLEAN | IN | If 0, execute a hard (permanent) delete. For any value other than 0, perform a soft delete (see Oracle Database SecureFiles and Large Objects Developer's Guide , Deletion Operations). |
| store_name | VARCHAR2 | IN | Name of store |
| principal | VARCHAR2 | IN | File system user for whom the access check is made |

## Usage Notes

Syntax DBMS_DBFS_CONTENT.DELETEFILE ( path IN VARCHAR2, filter IN VARCHAR2 DEFAULT NULL, soft_delete IN BOOLEAN DEFAULT NULL, store_name IN VARCHAR2 DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL); Parameters Table 52-29 DELETEFILE Procedure Parameters Parameter Description path Name of path to the file filter A filter, if any, to be applied soft_delete If 0, execute a hard (permanent) delete. For any value other than 0, perform a soft delete (see Oracle Database SecureFiles and Large Objects Developer's Guide , Deletion Operations). store_name Name of store principal File system user for whom the access check is made