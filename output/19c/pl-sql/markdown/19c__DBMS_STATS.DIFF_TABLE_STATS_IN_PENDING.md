---
id: 19c__DBMS_STATS.DIFF_TABLE_STATS_IN_PENDING
name: DBMS_STATS.DIFF_TABLE_STATS_IN_PENDING
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.DIFF_TABLE_STATS_IN_PENDING

This function compares pending statistics to either the current statistics in the data dictionary, or user-specified historical statistics.

## Syntax

```sql
DBMS_STATS.DIFF_TABLE_STATS_IN_PENDING( 
      ownname        IN  VARCHAR2,
      tabname        IN  VARCHAR2,
      timestamp      IN  TIMESTAMP WITH TIME ZONE,
      pctthreshold   IN  NUMBER  DEFAULT 10)
RETURN DiffRepTab pipelined;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Owner of the table. Specify NULL for the current schema. |
| tabname | VARCHAR2 | IN | Table for which statistics are to be compared. |
| timestamp | TIMESTAMP | IN | Timestamp in the statistics history that corresponds to the desired statistics. If the timestamp is NULL , then this function compares the current statistics in the dictionary with the pending statistics (default). |
| pctthreshold | NUMBER | IN | Limit for reporting. The function reports difference in statistics only if it exceeds the specified limit. The default value is 10 . |

**Returns:** `DiffRepTab`

## Usage Notes

Syntax DBMS_STATS.DIFF_TABLE_STATS_IN_PENDING( ownname IN VARCHAR2, tabname IN VARCHAR2, timestamp IN TIMESTAMP WITH TIME ZONE, pctthreshold IN NUMBER DEFAULT 10) RETURN DiffRepTab pipelined; Parameters Table 171-34 DIFF_TABLE_STATS_IN_PENDING Function Parameters Parameter Description ownname Owner of the table. Specify NULL for the current schema. tabname Table for which statistics are to be compared. timestamp Timestamp in the statistics history that corresponds to the desired statistics. If the timestamp is NULL , then this function compares the current statistics in the dictionary with the pending statistics (default). pctthreshold Limit for reporting. The function reports difference in statistics only if it exceeds the specified limit. The default value is 10 . Security Model To invoke this procedure you must be owner of the table, or you must have the ANALYZE ANY privilege. For objects owned by SYS , you must be either the owner of the table, or you must have either the ANALYZE ANY DICTIONARY privilege or the SYSDBA privilege.