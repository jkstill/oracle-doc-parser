---
id: 19c__DBMS_STATS.GET_TABLE_STATS
name: DBMS_STATS.GET_TABLE_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.GET_TABLE_STATS

This overloaded procedure gets all table-related statistics.

## Syntax

```sql
DBMS_STATS.GET_TABLE_STATS (
   ownname            VARCHAR2, 
   tabname            VARCHAR2, 
   partname           VARCHAR2 DEFAULT NULL,
   stattab            VARCHAR2 DEFAULT NULL,
   statid             VARCHAR2 DEFAULT NULL,
   numrows        OUT NUMBER, 
   numblks        OUT NUMBER,
   avgrlen        OUT NUMBER,
   statown            VARCHAR2 DEFAULT NULL,
   realtime_stats     BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Specifies the name of the schema. |
| tabname | VARCHAR2 | IN | Specifies the name of the table to which this column belongs. |
| partname | VARCHAR2 | IN | Specifies the name of the table partition from which to get the statistics. If the table is partitioned and if partname is NULL , then the statistics are retrieved from the global table level. |
| stattab | VARCHAR2 | IN | Specifies the user statistics table ID. This ID describes where to retrieve the statistics. If stattab is NULL , then the procedure gathers statistics directly from the data dictionary. |
| statid | VARCHAR2 | IN | Specifies the optional ID associates with these statistics within stattab . This ID is only relevant when stattab is not NULL . |
| numrows | NUMBER | OUT | Specifies the number of rows in the table or partition. |
| numblks | NUMBER | OUT | Specifies the number of blocks in the table or partition. |
| avgrlen | NUMBER | OUT | Specifies the average row length for the table or partition. |
| statown | VARCHAR2 | IN | Specifies the schema containing stattab (if different from ownname ). |
| im_imcu_count |  |  | Specifies the number of In-Memory Compression Units (IMCUs) in the table or partition. |
| im_block_count |  |  | Specifies the number of In-Memory blocks in the table or partition. An In-Memory block corresponds to a specific data block on disk. If the table is fully populated in the IM column store, then the number of In-Memory blocks equals the number of data blocks. |
| scanrate |  |  | Specifies the rate, in MB/s, at which the database scans external tables. This parameter is relevant only for external tables. |
| realtime_stats | BOOLEAN | IN | Specifies whether to include real-time statistics. The default value is TRUE . When realtime_stats is FALSE , the database only includes optimizer statistics that were gathered by the GATHER_ * _STATS procedures. |
| cachedblk |  |  | For internal use only. |
| cachehit |  |  | For internal use only. |

## Usage Notes

Syntax DBMS_STATS.GET_TABLE_STATS ( ownname VARCHAR2, tabname VARCHAR2, partname VARCHAR2 DEFAULT NULL, stattab VARCHAR2 DEFAULT NULL, statid VARCHAR2 DEFAULT NULL, numrows OUT NUMBER, numblks OUT NUMBER, avgrlen OUT NUMBER, statown VARCHAR2 DEFAULT NULL, realtime_stats BOOLEAN DEFAULT TRUE); DBMS_STATS.GET_TABLE_STATS ( ownname VARCHAR2, tabname VARCHAR2, partname VARCHAR2 DEFAULT NULL, stattab VARCHAR2 DEFAULT NULL, statid VARCHAR2 DEFAULT NULL, numrows OUT NUMBER, numblks OUT NUMBER, avgrlen OUT NUMBER, statown VARCHAR2 DEFAULT NULL, im_imcu_count OUT NUMBER, im_block_count OUT NUMBER, scanrate OUT NUMBER, realtime_stats BOOLEAN DEFAULT TRUE); DBMS_STATS.GET_TABLE_STATS ( ownname VARCHAR2, tabname VARCHAR2, partname VARCHAR2 DEFAULT NULL, stattab VARCHAR2 DEFAULT NULL, statid VARCHAR2 DEFAULT NULL, numrows OUT NUMBER, numblks OUT NUMBER, avgrlen OUT NUMBER, cachedblk OUT NUMBER, cachehit OUT NUMBER, realtime_stats BOOLEAN DEFAULT TRUE); Parameters Table 171-69 GET_TABLE_STATS Procedure Parameters Parameter Description ownname Specifies the name of the schema. tabname Specifies the name of the table to which this column belongs. partname Specifies the name of the table partition from which to get the statistics. If the table is partitioned and if partname is NULL , then the statistics are retrieved from the global table level. stattab Specifies the user statistics table ID. This ID describes where to retrieve the statistics. If stattab is NULL , then the procedure gathers statistics directly from the data dictionary. statid Specifies the optional ID associates with these statistics within stattab . This ID is only relevant when stattab is not NULL . numrows Specifies the number of rows in the table or partition. numblks Specifies the number of blocks in the table or partition. avgrlen Specifies the average row length for the table or partition. statown Specifies the schema containing stattab (if different from ownname ). im_imcu_count Specifies the number of In-Memory Compression Units (IMCUs) in the table or partition. im_block_count Specifies the number of In-Memory blocks in the table or partition. An In-Memory block corresponds to a specific data block on disk. If the table is fully populated in the IM column store, then the number of In-Memory blocks equals the number of data blocks. scanrate Specifies the rate, in MB/s, at which the database scans external tables. This parameter is relevant only for external tables. realtime_stats Specifies whether to include real-time statistics. The default value is TRUE . When realtime_stats is FALSE , the database only includes optimizer statistics that were gathered by the GATHER_ * _STATS procedures. cachedblk For internal use only. cachehit For internal use only. Security Model Before invoking this procedure, ensure that the table exists. To invoke this procedure you must be owner of the table, or you need the ANALYZE ANY privilege. For objects owned by SYS , you must be either the owner of the table, or have the ANALYZE ANY DICTIONARY or SYSDBA privilege. Exceptions ORA-20000 : Object does not exist or insufficient privileges or no statistics have been stored for requested object ORA-20002 : Bad user statistics table; may need to upgrade it Usage Notes The optimizer uses the cached data to estimate number of cached blocks for index or statistics table access. The database calculates the total cost of the operation by combining the I/O cost of reading not cached blocks from disk, the CPU cost of getting cached blocks from the buffer cache, and the CPU cost of processing the data. The database maintains cachedblk and cachehit at all times. However, the database uses the corresponding caching statistics for optimization as part of the table and index statistics only when the user calls the DBMS_STATS.GATHER_ * _STATS procedure for automatic mode or DBMS_STATS.GATHER_SYSTEM_STATS for manual mode. To prevent the user from utilizing inaccurate and unreliable data, the optimizer computes a “confidence factor” for each cachehit and a cachedblk for each object. If the confidence factor for the value meets confidence criteria, then the database uses this value; otherwise, the database uses defaults. The automatic maintenance algorithm for object caching statistics assumes that only one major database workload exists. The algorithm adjusts statistics to this workload, ignoring other "minor" workloads. If this assumption is false, then you must use manual mode for maintaining object caching statistics. The object caching statistics maintenance algorithm for automatic mode prevents you from using statistics in the following situations When not enough data has been analyzed, such as when an object has been recently created When the system does not have one major workload resulting in averages not corresponding to real values The database does not support export or import of statistics across databases of different character sets. See Also: Oracle Database SQL Tuning Guide to learn how to manage optimizer statistics preferences