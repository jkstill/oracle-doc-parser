---
id: 19c__DBMS_DBFS_CONTENT.DELETEDIRECTORY
name: DBMS_DBFS_CONTENT.DELETEDIRECTORY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.DELETEDIRECTORY

This procedure deletes a directory.

## Syntax

```sql
DBMS_DBFS_CONTENT.DELETEDIRECTORY (
   path           IN     VARCHAR2,
   filter         IN     VARCHAR2    DEFAULT NULL,
   soft_delete    IN     BOOLEAN     DEFAULT NULL,
   recurse        IN     BOOLEAN     DEFAULT FALSE,
   store_name     IN     VARCHAR2    DEFAULT NULL,
   principal      IN     VARCHAR2    DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| path | VARCHAR2 | IN | Name of path to the directory |
| filter | VARCHAR2 | IN | A filter, if any, to be applied |
| soft_delete | BOOLEAN | IN | If 0, execute a hard (permanent) delete. For any value other than 0, perform a soft delete see Oracle Database SecureFiles and Large Objects Developer's Guide , Deletion Operations. |
| recurse | BOOLEAN | IN | If 0, do not execute recursively. Otherwise, recursively delete the directories and files below the given directory. |
| store_name | VARCHAR2 | IN | Name of store |
| principal | VARCHAR2 | IN | File system user for whom the access check is made |

## Usage Notes

If recurse is nonzero, it recursively deletes all elements of the directory. A filter, if supplied, determines which elements of the directory are deleted. Syntax DBMS_DBFS_CONTENT.DELETEDIRECTORY ( path IN VARCHAR2, filter IN VARCHAR2 DEFAULT NULL, soft_delete IN BOOLEAN DEFAULT NULL, recurse IN BOOLEAN DEFAULT FALSE, store_name IN VARCHAR2 DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL); Parameters Table 52-28 DELETEDIRECTORY Procedure Parameters Parameter Description path Name of path to the directory filter A filter, if any, to be applied soft_delete If 0, execute a hard (permanent) delete. For any value other than 0, perform a soft delete see Oracle Database SecureFiles and Large Objects Developer's Guide , Deletion Operations. recurse If 0, do not execute recursively. Otherwise, recursively delete the directories and files below the given directory. store_name Name of store principal File system user for whom the access check is made