---
id: 19c__DBMS_STATS.DIFF_TABLE_STATS_IN_STATTAB
name: DBMS_STATS.DIFF_TABLE_STATS_IN_STATTAB
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.DIFF_TABLE_STATS_IN_STATTAB

This function compares table statistics from two sources.

## Syntax

```sql
DBMS_STATS.DIFF_TABLE_STATS_IN_STATTAB( 
   ownname        IN  VARCHAR2,
   tabname        IN  VARCHAR2,
   stattab1       IN  VARCHAR2,
   stattab2       IN  VARCHAR2 DEFAULT NULL,
   pctthreshold   IN  NUMBER   DEFAULT 10,
   statid1        IN  VARCHAR2 DEFAULT NULL,
   statid2        IN  VARCHAR2 DEFAULT NULL,
   stattab1own    IN  VARCHAR2 DEFAULT NULL,
   stattab2own    IN  VARCHAR2 DEFAULT NULL)
RETURN DiffRepTab pipelined;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Specifies the owner of the table. Specify NULL for current schema. |
| tabname | VARCHAR2 | IN | Specifies the table for which statistics are to be compared. |
| stattab1 | VARCHAR2 | IN | Specifies the user statistics table 1. |
| stattab2 | VARCHAR2 | IN | Specifies the user statistics table 2. If NULL , the function compares statistics in stattab1 with current statistics in the data dictionary. This is the default. To compare two sets within the statistics table, specify the same table as stattab1 (see statid below). |
| pctthreshold | NUMBER | IN | Specifies the percent thresholds for comparison. The function reports difference in statistics only if it exceeds this limit. The default value is 10 . |
| stadid1 |  |  | (optional) Identifies statistics set within stattab1 . |
| stadid2 |  |  | (optional) Identifies statistics set within stattab2 . |
| stattab1own | VARCHAR2 | IN | Specifies the schema containing stattab1 (if other than ownname ). |
| stattab2own | VARCHAR2 | IN | Specifies the schema containing stattab2 (if other than ownname ). |

**Returns:** `DiffRepTab`

## Usage Notes

The function can obtain statistics from the following sources: Two user statistics tables A single user statistics table containing two sets of statistics that can be identified using statids A user statistics table and dictionary The function also compares the statistics of the dependent objects: indexes, columns, and partitions. It displays statistics of the objects from both sources when the difference between those statistics exceeds a certain threshold (%). You can specify this threshold as an argument to the function. The function uses the statistics corresponding to the first source ( stattab1 or time1 ) as the basis for computing the difference percentage. Syntax DBMS_STATS.DIFF_TABLE_STATS_IN_STATTAB( ownname IN VARCHAR2, tabname IN VARCHAR2, stattab1 IN VARCHAR2, stattab2 IN VARCHAR2 DEFAULT NULL, pctthreshold IN NUMBER DEFAULT 10, statid1 IN VARCHAR2 DEFAULT NULL, statid2 IN VARCHAR2 DEFAULT NULL, stattab1own IN VARCHAR2 DEFAULT NULL, stattab2own IN VARCHAR2 DEFAULT NULL) RETURN DiffRepTab pipelined; Parameters Table 171-35 DIFF_TABLE_STATS_IN_STATTAB Function Parameters Parameter Description ownname Specifies the owner of the table. Specify NULL for current schema. tabname Specifies the table for which statistics are to be compared. stattab1 Specifies the user statistics table 1. stattab2 Specifies the user statistics table 2. If NULL , the function compares statistics in stattab1 with current statistics in the data dictionary. This is the default. To compare two sets within the statistics table, specify the same table as stattab1 (see statid below). pctthreshold Specifies the percent thresholds for comparison. The function reports difference in statistics only if it exceeds this limit. The default value is 10 . stadid1 (optional) Identifies statistics set within stattab1 . stadid2 (optional) Identifies statistics set within stattab2 . stattab1own Specifies the schema containing stattab1 (if other than ownname ). stattab2own Specifies the schema containing stattab2 (if other than ownname ). Security Model To invoke this procedure you must be owner of the table or have the ANALYZE ANY privilege. For objects owned by SYS , you must be either the owner of the table or have either the ANALYZE ANY DICTIONARY privilege or the SYSDBA privilege.