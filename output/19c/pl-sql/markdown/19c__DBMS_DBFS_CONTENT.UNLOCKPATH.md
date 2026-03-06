---
id: 19c__DBMS_DBFS_CONTENT.UNLOCKPATH
name: DBMS_DBFS_CONTENT.UNLOCKPATH
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.UNLOCKPATH

This procedure unlocks path items that were previously locked with the LOCKPATH Procedure.

## Syntax

```sql
DBMS_DBFS_CONTENT.UNLOCKPATH (
   path           IN     VARCHAR2,
   who            IN     VARCHAR2,
   waitForRowLock IN     INTEGER     DEFAULT 1,
   store_name     IN     VARCHAR2    DEFAULT NULL,
   principal      IN     VARCHAR2    DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| path | VARCHAR2 | IN | Name of path to file items |
| who | VARCHAR2 | IN | Transaction identifier that has locked the path |
| waitForRowLock | INTEGER | IN | Determines if a row is locked by a transaction or not |
| store_name | VARCHAR2 | IN | Name of store |
| principal | VARCHAR2 | IN | Agent (principal) invoking the current operation |

## Usage Notes

Syntax DBMS_DBFS_CONTENT.UNLOCKPATH ( path IN VARCHAR2, who IN VARCHAR2, waitForRowLock IN INTEGER DEFAULT 1, store_name IN VARCHAR2 DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL); Parameters Table 52-77 UNLOCKPATH Procedure Parameters Parameter Description path Name of path to file items who Transaction identifier that has locked the path waitForRowLock Determines if a row is locked by a transaction or not store_name Name of store principal Agent (principal) invoking the current operation