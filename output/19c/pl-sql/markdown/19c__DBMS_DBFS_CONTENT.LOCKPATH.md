---
id: 19c__DBMS_DBFS_CONTENT.LOCKPATH
name: DBMS_DBFS_CONTENT.LOCKPATH
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.LOCKPATH

This procedure applies user-level locks to the given valid path name (subject to store feature support), and optionally associates user-data with the lock.

## Syntax

```sql
DBMS_DBFS_CONTENT.LOCKPATH (
   path           IN     VARCHAR2,
   who            IN     VARCHAR2,
   lock_type      IN     INTEGER,
   waitForRowLock IN     INTEGER     DEFAULT 1,
   store_name     IN     VARCHAR2    DEFAULT NULL,
   principal      IN     VARCHAR2    DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| path | VARCHAR2 | IN | Name of path to file items |
| who | VARCHAR2 | IN | Transaction identifier that has locked the path |
| lock_type | INTEGER | IN | One of the available lock types (see Table 52-6 ) |
| waitForRowLock | INTEGER | IN | Determines if a row is locked by a transaction or not |
| store_name | VARCHAR2 | IN | Name of store |
| principal | VARCHAR2 | IN | Agent (principal) invoking the current operation |

## Usage Notes

Syntax DBMS_DBFS_CONTENT.LOCKPATH ( path IN VARCHAR2, who IN VARCHAR2, lock_type IN INTEGER, waitForRowLock IN INTEGER DEFAULT 1, store_name IN VARCHAR2 DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL); Parameters Table 52-49 LOCKPATH Procedure Parameters Parameter Description path Name of path to file items who Transaction identifier that has locked the path lock_type One of the available lock types (see Table 52-6 ) waitForRowLock Determines if a row is locked by a transaction or not store_name Name of store principal Agent (principal) invoking the current operation