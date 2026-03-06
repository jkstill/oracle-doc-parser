---
id: 19c__DBMS_STATS.LOCK_TABLE_STATS
name: DBMS_STATS.LOCK_TABLE_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.LOCK_TABLE_STATS

This procedure locks the statistics on the table.

## Syntax

```sql
DBMS_STATS.LOCK_TABLE_STATS (
   ownname    VARCHAR2,
   tabname    VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Name of the schema |
| tabname | VARCHAR2) | IN | Name of the table |

## Usage Notes

Syntax DBMS_STATS.LOCK_TABLE_STATS ( ownname VARCHAR2, tabname VARCHAR2); Parameters Table 171-85 LOCK_TABLE_STATS Procedure Parameters Parameter Description ownname Name of the schema tabname Name of the table Usage Notes To invoke this procedure you must be owner of the table, or you need the ANALYZE ANY privilege. For objects owned by SYS , you need to be either the owner of the table, or you need the ANALYZE ANY DICTIONARY privilege or the SYSDBA privilege. When statistics on a table are locked, all the statistics depending on the table, including table statistics, column statistics, histograms and statistics on all dependent indexes, are considered to be locked. The SET_*, DELETE_*, IMPORT_*, GATHER_* procedures that modify statistics in the dictionary of an individual table, index or column will raise an error if statistics of the object is locked. Procedures that operates on multiple objects (such as GATHER_SCHEMA_STATS ) will skip modifying the statistics of an object if it is locked. Many procedures have force argument to override the lock. This procedure either freezes the current set of the statistics or keeps the statistics empty (uncollected) to use dynamic statistics. The locked or unlocked state is not exported along with the table statistics when using EXPORT_*_STATS procedures. Neither the UNLOCK_SCHEMA_STATS Procedure nor the UNLOCK_TABLE_STATS Procedure is designed to unlock statistics of corresponding partitions. When you invoke the LOCK_TABLE_STATS Procedure , it sets the statistics lock bit at the table level. In that case, you cannot gather statistics on dependent objects such as partitions and indexes. By the same token, if table statistics are locked, the dependents are locked and you do not need to explicitly invoke the LOCK_PARTITION_STATS Procedure .