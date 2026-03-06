---
id: 19c__DBMS_STATS.SET_TABLE_STATS
name: DBMS_STATS.SET_TABLE_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.SET_TABLE_STATS

This procedure creates artificial table statistics for testing purposes.

## Syntax

```sql
DBMS_STATS.SET_TABLE_STATS (
   ownname        VARCHAR2, 
   tabname        VARCHAR2, 
   partname       VARCHAR2 DEFAULT NULL,
   stattab        VARCHAR2 DEFAULT NULL, 
   statid         VARCHAR2 DEFAULT NULL,
   numrows        NUMBER   DEFAULT NULL, 
   numblks        NUMBER   DEFAULT NULL,
   avgrlen        NUMBER   DEFAULT NULL,
   flags          NUMBER   DEFAULT NULL,
   statown        VARCHAR2 DEFAULT NULL,
   no_invalidate  BOOLEAN  DEFAULT to_no_invalidate_type (
                                     get_param('NO_INVALIDATE')),
   cachedblk      NUMBER   DEFAULT NULL,
   cachehit       NUMBER   DEFAULT NULL,
   force          BOOLEAN  DEFAULT FALSE,
   im_imcu_count  NUMBER   DEFAULT NULL,
   im_block_count NUMBER   DEFAULT NULL,
   scanrate       NUMBER   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Name of the schema. |
| tabname | VARCHAR2 | IN | Name of the table. |
| partname | VARCHAR2 | IN | Name of the table partition in which to store the statistics. If the table is partitioned and partname is NULL , then the statistics are stored at the global table level. |
| stattab | VARCHAR2 | IN | Table in which to store the statistics. If stattab is NULL , then the database stores the statistics in the data dictionary. |
| statid | VARCHAR2 | IN | Identifier (optional) to associate with these statistics within stattab . This identifier is only relevant if stattab is not NULL . |
| numrows | NUMBER | IN | Number of rows in the table or partition. |
| numblks | NUMBER | IN | Number of blocks that the table or partition occupies. |
| avgrlen | NUMBER | IN | Average row length for the table or partition. |
| flags | NUMBER | IN | For internal use only. Do not set. |
| statown | VARCHAR2 | IN | Schema containing stattab (if different than ownname ). |
| no_invalidate | BOOLEAN | IN | Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. You can change the default using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . |
| cachedblk | NUMBER | IN | For internal use only. Do not set. |
| cachehit | NUMBER | IN | For internal use only. Do not set. |
| force | BOOLEAN | IN | A flag that determines the behavior when statistics are locked. If TRUE , then the procedure sets the values even if the table statistics are locked. By default, the setting is FALSE . |
| im_imcu_count | NUMBER | IN | The number of In-Memory Compression Units (IMCUs) in the table or partition. |
| im_block_count | NUMBER | IN | The number of In-Memory blocks in the table or partition. |
| scanrate | NUMBER | IN | The rate, in MB/s, at which the database scans external tables. This parameter is relevant only for external tables. |

## Usage Notes

Syntax DBMS_STATS.SET_TABLE_STATS ( ownname VARCHAR2, tabname VARCHAR2, partname VARCHAR2 DEFAULT NULL, stattab VARCHAR2 DEFAULT NULL, statid VARCHAR2 DEFAULT NULL, numrows NUMBER DEFAULT NULL, numblks NUMBER DEFAULT NULL, avgrlen NUMBER DEFAULT NULL, flags NUMBER DEFAULT NULL, statown VARCHAR2 DEFAULT NULL, no_invalidate BOOLEAN DEFAULT to_no_invalidate_type ( get_param('NO_INVALIDATE')), cachedblk NUMBER DEFAULT NULL, cachehit NUMBER DEFAULT NULL, force BOOLEAN DEFAULT FALSE, im_imcu_count NUMBER DEFAULT NULL, im_block_count NUMBER DEFAULT NULL, scanrate NUMBER DEFAULT NULL); Parameters Table 171-133 SET_TABLE_STATS Procedure Parameters Parameter Description ownname Name of the schema. tabname Name of the table. partname Name of the table partition in which to store the statistics. If the table is partitioned and partname is NULL , then the statistics are stored at the global table level. stattab Table in which to store the statistics. If stattab is NULL , then the database stores the statistics in the data dictionary. statid Identifier (optional) to associate with these statistics within stattab . This identifier is only relevant if stattab is not NULL . numrows Number of rows in the table or partition. numblks Number of blocks that the table or partition occupies. avgrlen Average row length for the table or partition. flags For internal use only. Do not set. statown Schema containing stattab (if different than ownname ). no_invalidate Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. You can change the default using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . cachedblk For internal use only. Do not set. cachehit For internal use only. Do not set. force A flag that determines the behavior when statistics are locked. If TRUE , then the procedure sets the values even if the table statistics are locked. By default, the setting is FALSE . im_imcu_count The number of In-Memory Compression Units (IMCUs) in the table or partition. im_block_count The number of In-Memory blocks in the table or partition. scanrate The rate, in MB/s, at which the database scans external tables. This parameter is relevant only for external tables. Security Model To invoke this procedure you must be owner of the table, or have the ANALYZE ANY privilege. For objects owned by SYS , you must be either the owner of the table, or have the ANALYZE ANY DICTIONARY privilege or the SYSDBA privilege. Exceptions ORA-20000 : Object does not exist or insufficient privileges ORA-20001 : Invalid input value ORA-20002 : Bad user statistics table; may need to upgrade it ORA-20005 : Object statistics are locked Usage Notes For testing purposes, you can manually create artificial statistics for a table, index, or the system using the DBMS_STATS.SET_*_STATS procedures. These procedures insert the artificial statistics into the data dictionary directly (when stattab is null) or into a user-created table. Note: The DBMS_STATS.SET_*_STATS procedures are intended for development testing only. Do not use them in a production database. If you set statistics in the data dictionary, then Oracle Database considers the set statistics as the “real” statistics, which means that statistics gathering jobs may not re-gather artificial statistics when they do not meet the criteria for staleness. The most typical use cases for the DBMS_STATS.SET_*_STATS procedures are showing how execution plans change as the numbers of rows or blocks in a table change, or creating realistic statistics for temporary tables. The optimizer uses the cached data to estimate number of cached blocks for index or statistics table access. The database calculates the total cost of the operation by combining the I/O cost of reading not cached blocks from disk, the CPU cost of getting cached blocks from the buffer cache, and the CPU cost of processing the data. The database maintains cachedblk and cachehit at all times. However, the database uses the corresponding caching statistics for optimization as part of the table and index statistics only when the user calls the DBMS_STATS.GATHER_[TABLE/INDEX/SCHEMA/DATABASE]_STATS procedure for automatic mode or DBMS_STATS.GATHER_SYSTEM_STATS for manual mode. To prevent the user from utilizing inaccurate and unreliable data, the optimizer computes a “confidence factor” for each cachehit and a cachedblk for each object. If the confidence factor for the value meets confidence criteria, then the database uses this value; otherwise, the database uses defaults. The automatic maintenance algorithm for object caching statistics assumes that only one major database workload exists. The algorithm adjusts statistics to this workload, ignoring other "minor" workloads. If this assumption is false, then you must use manual mode for maintaining object caching statistics. The object caching statistics maintenance algorithm for automatic mode prevents you from using statistics in the following situations: When not enough data has been analyzed, such as when an object has been recently created When the database does not have one major workload, resulting in averages that do not correspond to real values See Also: Oracle Database SQL Tuning Guide to learn how to set artificial statistics