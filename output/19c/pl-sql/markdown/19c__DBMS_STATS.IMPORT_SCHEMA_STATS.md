---
id: 19c__DBMS_STATS.IMPORT_SCHEMA_STATS
name: DBMS_STATS.IMPORT_SCHEMA_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.IMPORT_SCHEMA_STATS

This procedure imports statistics for all objects in the schema identified by ownname from the user statistics table and stores them in the data dictionary.

## Syntax

```sql
DBMS_STATS.IMPORT_SCHEMA_STATS (
   ownname         VARCHAR2,
   stattab         VARCHAR2, 
   statid          VARCHAR2 DEFAULT NULL,
   statown         VARCHAR2 DEFAULT NULL,
   no_invalidate   BOOLEAN  DEFAULT to_no_invalidate_type(
                                    get_param('NO_INVALIDATE')),
   force           BOOLEAN DEFAULT FALSE,
   stat_category   VARCHAR2 DEFAULT DEFAULT_STAT_CATEGORY);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Specifies the name of the schema. |
| stattab | VARCHAR2 | IN | Identifies the user table that stores the statistics to be imported. |
| statid | VARCHAR2 | IN | Specifies the ID associated with these statistics within stattab . |
| statown | VARCHAR2 | IN | Specifies the schema containing stattab (if different than ownname ). |
| no_invalidate | BOOLEAN | IN | Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. You can change the default using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . |
| force | BOOLEAN | IN | Specifies whether to override statistics locked at the object level. The possible values are as follows: TRUE — Ignores the statistics lock and imports the statistics. FALSE — Imports the statistics only if there is no lock. This is the default. |
| stat_category | VARCHAR2 | IN | Specifies which statistics to process. The following values are supported: OBJECT_STATS — Specifies table statistics, column statistics, and index statistics. SYNOPSES — Specifies metadata for incremental statistics. REALTIME_STATS — Specifies only real-time statistics . You can specify a list of comma-delimited values. For example, 'OBJECT_STATS, SYNOPSES' specifies table statistics, column statistics, index statistics, and synopses. The default value is 'OBJECT_STATS, REALTIME_STATS' . |

## Usage Notes

Syntax DBMS_STATS.IMPORT_SCHEMA_STATS ( ownname VARCHAR2, stattab VARCHAR2, statid VARCHAR2 DEFAULT NULL, statown VARCHAR2 DEFAULT NULL, no_invalidate BOOLEAN DEFAULT to_no_invalidate_type( get_param('NO_INVALIDATE')), force BOOLEAN DEFAULT FALSE, stat_category VARCHAR2 DEFAULT DEFAULT_STAT_CATEGORY); Parameters Table 171-78 IMPORT_SCHEMA_STATS Procedure Parameters Parameter Description ownname Specifies the name of the schema. stattab Identifies the user table that stores the statistics to be imported. statid Specifies the ID associated with these statistics within stattab . statown Specifies the schema containing stattab (if different than ownname ). no_invalidate Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. You can change the default using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . force Specifies whether to override statistics locked at the object level. The possible values are as follows: TRUE — Ignores the statistics lock and imports the statistics. FALSE — Imports the statistics only if there is no lock. This is the default. stat_category Specifies which statistics to process. The following values are supported: OBJECT_STATS — Specifies table statistics, column statistics, and index statistics. SYNOPSES — Specifies metadata for incremental statistics. REALTIME_STATS — Specifies only real-time statistics . You can specify a list of comma-delimited values. For example, 'OBJECT_STATS, SYNOPSES' specifies table statistics, column statistics, index statistics, and synopses. The default value is 'OBJECT_STATS, REALTIME_STATS' . Security Model To invoke this procedure you must be owner of the table or have the ANALYZE ANY privilege. For objects owned by SYS , you must be either the owner of the table or have either the ANALYZE ANY DICTIONARY privilege or the SYSDBA privilege. Exceptions ORA-20000 : Object does not exist or insufficient privileges ORA-20001 : Invalid or inconsistent values in the user statistics table Usage Notes Oracle Database does not support export or import of statistics across databases of different character sets.