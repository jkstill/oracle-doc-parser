---
id: 19c__DBMS_STATS.DELETE_TABLE_STATS
name: DBMS_STATS.DELETE_TABLE_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.DELETE_TABLE_STATS

This procedure deletes table-related statistics.

## Syntax

```sql
DBMS_STATS.DELETE_TABLE_STATS (
   ownname          VARCHAR2, 
   tabname          VARCHAR2, 
   partname         VARCHAR2 DEFAULT NULL,
   stattab          VARCHAR2 DEFAULT NULL, 
   statid           VARCHAR2 DEFAULT NULL,
   cascade_parts    BOOLEAN  DEFAULT TRUE, 
   cascade_columns  BOOLEAN  DEFAULT TRUE,
   cascade_indexes  BOOLEAN  DEFAULT TRUE,
   statown          VARCHAR2 DEFAULT NULL,
   no_invalidate    BOOLEAN  DEFAULT to_no_invalidate_type (
                                     get_param('NO_INVALIDATE')),
   force            BOOLEAN  DEFAULT FALSE,
   stat_category    VARCHAR2 DEFAULT DEFAULT_STAT_CATEGORY);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Specifies the name of the schema. |
| tabname | VARCHAR2 | IN | Specifies the name of the table to which this column belongs. |
| partname | VARCHAR2 | IN | Specifies the name of the table partition or subpartition from which to get the statistics. If the table is partitioned and if partname is NULL , then the statistics are retrieved from the global table level. |
| stattab | VARCHAR2 | IN | Identifies the user statistics table where statistics will be retrieved. If stattab is NULL , then the procedure retrieves statistics directly from the dictionary. |
| statid | VARCHAR2 | IN | Specifies the identifier (optional) associated with these statistics within stattab . This parameter is only relevant if stattab is not NULL . |
| cascade_parts | BOOLEAN | IN | Specifies whether the procedure should operate on underlying partitions. If the table is partitioned, and if partname is NULL , then specifying TRUE deletes statistics for underlying partitions. |
| cascade_columns | BOOLEAN | IN | Indicates whether to invoke the DELETE_COLUMN_STATS procedure. If TRUE , then this procedure calls DELETE_COLUMN_STATS for all underlying columns. |
| cascade_indexes | BOOLEAN | IN | Indicates whether to invoke the DELETE_INDEX_STATS procedure. If TRUE , then this procedure calls DELETE_INDEX_STATS for all underlying columns. |
| statown | VARCHAR2 | IN | Specifies the schema containing stattab (if different than ownname ). |
| no_invalidate | BOOLEAN | IN | Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. You can change the default using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . |
| force | BOOLEAN | IN | Indicates whether to force the deletion for locked statistics. When the value is TRUE , this procedure deletes table statistics even if locked. |
| stat_category | VARCHAR2 | IN | Specifies which statistics to process. The following values are supported: OBJECT_STATS — Specifies table statistics, column statistics, and index statistics. SYNOPSES — Specifies metadata for incremental statistics. REALTIME_STATS — Specifies only real-time statistics . You can specify a list of comma-delimited values. For example, 'OBJECT_STATS, SYNOPSES' specifies table statistics, column statistics, index statistics, and synopses. The default value is 'OBJECT_STATS, REALTIME_STATS' . |

## Usage Notes

Syntax DBMS_STATS.DELETE_TABLE_STATS ( ownname VARCHAR2, tabname VARCHAR2, partname VARCHAR2 DEFAULT NULL, stattab VARCHAR2 DEFAULT NULL, statid VARCHAR2 DEFAULT NULL, cascade_parts BOOLEAN DEFAULT TRUE, cascade_columns BOOLEAN DEFAULT TRUE, cascade_indexes BOOLEAN DEFAULT TRUE, statown VARCHAR2 DEFAULT NULL, no_invalidate BOOLEAN DEFAULT to_no_invalidate_type ( get_param('NO_INVALIDATE')), force BOOLEAN DEFAULT FALSE, stat_category VARCHAR2 DEFAULT DEFAULT_STAT_CATEGORY); Parameters Table 171-32 DELETE_TABLE_STATS Procedure Parameters Parameter Description ownname Specifies the name of the schema. tabname Specifies the name of the table to which this column belongs. partname Specifies the name of the table partition or subpartition from which to get the statistics. If the table is partitioned and if partname is NULL , then the statistics are retrieved from the global table level. stattab Identifies the user statistics table where statistics will be retrieved. If stattab is NULL , then the procedure retrieves statistics directly from the dictionary. statid Specifies the identifier (optional) associated with these statistics within stattab . This parameter is only relevant if stattab is not NULL . cascade_parts Specifies whether the procedure should operate on underlying partitions. If the table is partitioned, and if partname is NULL , then specifying TRUE deletes statistics for underlying partitions. cascade_columns Indicates whether to invoke the DELETE_COLUMN_STATS procedure. If TRUE , then this procedure calls DELETE_COLUMN_STATS for all underlying columns. cascade_indexes Indicates whether to invoke the DELETE_INDEX_STATS procedure. If TRUE , then this procedure calls DELETE_INDEX_STATS for all underlying columns. statown Specifies the schema containing stattab (if different than ownname ). no_invalidate Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. You can change the default using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . force Indicates whether to force the deletion for locked statistics. When the value is TRUE , this procedure deletes table statistics even if locked. stat_category Specifies which statistics to process. The following values are supported: OBJECT_STATS — Specifies table statistics, column statistics, and index statistics. SYNOPSES — Specifies metadata for incremental statistics. REALTIME_STATS — Specifies only real-time statistics . You can specify a list of comma-delimited values. For example, 'OBJECT_STATS, SYNOPSES' specifies table statistics, column statistics, index statistics, and synopses. The default value is 'OBJECT_STATS, REALTIME_STATS' . Security Model To invoke this procedure you must be owner of the table or have the ANALYZE ANY privilege. For objects owned by SYS , you must be either the owner of the table or have either the ANALYZE ANY DICTIONARY privilege or the SYSDBA privilege. Exceptions ORA-20000 : Object does not exist or insufficient privileges ORA-20002 : Bad user statistics table, may need to upgrade it ORA-20005 : Object statistics are locked