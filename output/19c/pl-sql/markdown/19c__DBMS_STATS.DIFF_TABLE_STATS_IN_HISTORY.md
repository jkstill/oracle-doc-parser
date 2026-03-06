---
id: 19c__DBMS_STATS.DIFF_TABLE_STATS_IN_HISTORY
name: DBMS_STATS.DIFF_TABLE_STATS_IN_HISTORY
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.DIFF_TABLE_STATS_IN_HISTORY

This function compares statistics for a table as of two specified timestamps.

## Syntax

```sql
DBMS_STATS.DIFF_TABLE_STATS_IN_HISTORY( 
   ownname        IN  VARCHAR2,
   tabname        IN  VARCHAR2,
   time1          IN  TIMESTAMP WITH TIME ZONE,
   time2          IN  TIMESTAMP WITH TIME ZONE DEFAULT NULL,
   pctthreshold   IN  NUMBER                   DEFAULT 10)
RETURN DiffRepTab pipelined;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Specifies the owner of the table. Specify NULL for current schema. |
| tabname | VARCHAR2 | IN | Specifies the table for which statistics are to be compared. |
| time1 | TIMESTAMP | IN | Specifies the first timestamp for comparison. |
| time2 | TIMESTAMP | IN | Specifies the second timestamp for comparison. |
| pctthreshold | NUMBER | IN | Specifies the threshold limit. The function reports differences in statistics only if the change percentage exceeds this limit. The default value is 10 . |

**Returns:** `DiffRepTab`

## Usage Notes

Syntax DBMS_STATS.DIFF_TABLE_STATS_IN_HISTORY( ownname IN VARCHAR2, tabname IN VARCHAR2, time1 IN TIMESTAMP WITH TIME ZONE, time2 IN TIMESTAMP WITH TIME ZONE DEFAULT NULL, pctthreshold IN NUMBER DEFAULT 10) RETURN DiffRepTab pipelined; Parameters Table 171-33 DIFF_TABLE_STATS_IN_HISTORY Function Parameters Parameter Description ownname Specifies the owner of the table. Specify NULL for current schema. tabname Specifies the table for which statistics are to be compared. time1 Specifies the first timestamp for comparison. time2 Specifies the second timestamp for comparison. pctthreshold Specifies the threshold limit. The function reports differences in statistics only if the change percentage exceeds this limit. The default value is 10 . Security Model To invoke this procedure you must be owner of the table or have the ANALYZE ANY privilege. For objects owned by SYS , you must be either the owner of the table or have either the ANALYZE ANY DICTIONARY privilege or the SYSDBA privilege. Usage Notes If the second timestamp is NULL , then the function compares the current statistics in the data dictionary with the statistics as of the first timestamp.