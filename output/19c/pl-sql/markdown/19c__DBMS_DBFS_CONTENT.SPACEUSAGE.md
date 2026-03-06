---
id: 19c__DBMS_DBFS_CONTENT.SPACEUSAGE
name: DBMS_DBFS_CONTENT.SPACEUSAGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.SPACEUSAGE

This procedure queries file system space usage statistics.

## Syntax

```sql
DBMS_DBFS_CONTENT.SPACEUSAGE (
   path          IN        VARCHAR2,
   blksize       OUT       INTEGER,
   tbytes        OUT       INTEGER,
   fbytes        OUT       INTEGER,
   nfile         OUT       INTEGER,
   ndir          OUT       INTEGER,
   nlink         OUT       INTEGER,
   nref          OUT       INTEGER,
   store_name    IN        VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| path | VARCHAR2 | IN | Name of path to file items |
| blksize | INTEGER | OUT | Natural tablespace blocksize that holds the store. If multiple tablespaces with different blocksizes are used, any valid blocksize is acceptable. |
| tbytes | INTEGER | OUT | Total size of the store in bytes computed over all segments that comprise the store |
| fbytes | INTEGER | OUT | Free or unused size of the store in bytes computed over all segments that comprise the store |
| nfile | INTEGER | OUT | Number of currently available files in the store |
| ndir | INTEGER | OUT | Number of currently available directories in the store |
| nlink | INTEGER | OUT | Number of currently available links in the store |
| nref | INTEGER | OUT | Number of currently available references in the store |
| store_name | VARCHAR2 | IN | Name of store |

## Usage Notes

Providers are expected to support this subprogram for their stores (and to make a best effort determination of space usage, especially if the store consists of multiple tables, indexes, LOBs, and so on). Syntax DBMS_DBFS_CONTENT.SPACEUSAGE ( path IN VARCHAR2, blksize OUT INTEGER, tbytes OUT INTEGER, fbytes OUT INTEGER, nfile OUT INTEGER, ndir OUT INTEGER, nlink OUT INTEGER, nref OUT INTEGER, store_name IN VARCHAR2 DEFAULT NULL); Parameters Table 52-74 SPACEUSAGE Procedure Parameters Parameter Description path Name of path to file items blksize Natural tablespace blocksize that holds the store. If multiple tablespaces with different blocksizes are used, any valid blocksize is acceptable. tbytes Total size of the store in bytes computed over all segments that comprise the store fbytes Free or unused size of the store in bytes computed over all segments that comprise the store nfile Number of currently available files in the store ndir Number of currently available directories in the store nlink Number of currently available links in the store nref Number of currently available references in the store store_name Name of store Usage Notes A space usage query on the top-level root directory returns a combined summary of the space usage of all available distinct stores under it (if the same store is mounted multiple times, is still counted only once). Since database objects are dynamically expandable, it is not easy to estimate the division between "free" space and "used" space.