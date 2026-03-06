---
id: 19c__DBMS_STATS.DELETE_SCHEMA_STATS
name: DBMS_STATS.DELETE_SCHEMA_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.DELETE_SCHEMA_STATS

This procedure deletes statistics for an entire schema.

## Syntax

```sql
DBMS_STATS.DELETE_SCHEMA_STATS (
   ownname          VARCHAR2, 
   stattab          VARCHAR2 DEFAULT NULL, 
   statid           VARCHAR2 DEFAULT NULL,
   statown          VARCHAR2 DEFAULT NULL,
   no_invalidate    BOOLEAN DEFAULT to_no_invalidate_type (
                                     get_param('NO_INVALIDATE')),
   force            BOOLEAN DEFAULT FALSE,
   stat_category   VARCHAR2 DEFAULT DEFAULT_DEL_STAT_CATEGORY);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Specifies the name of the schema. |
| stattab | VARCHAR2 | IN | Identifies the table where statistics are stored. If stattab is NULL , then the procedure deletes statistics directly from the data dictionary. |
| statid | VARCHAR2 | IN | Specifies the identifier (optional) associated with these statistics within stattab . This parameter is only relevant if stattab is not NULL . |
| statown | VARCHAR2 | IN | Specifies the schema containing stattab (if different than ownname ). |
| no_invalidate | BOOLEAN | IN | Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. You can change the default using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . |
| force | BOOLEAN | IN | Indicates whether to force the deletion for locked statistics. When the value is TRUE , this procedure deletes table statistics even if locked. |
| stat_category | VARCHAR2 | IN | Specifies which statistics to process. The following values are supported: OBJECT_STATS — Specifies table statistics, column statistics, and index statistics. SYNOPSES — Specifies metadata for incremental statistics. REALTIME_STATS — Specifies only real-time statistics. MODELS — supports import, export, and deletion for regression models in real-time stats. You can specify a list of comma-delimited values. For example, ' OBJECT_STATS, SYNOPSES ' specifies table statistics, column statistics, index statistics, and synopses. The default value is ' OBJECT_STATS, SYNOPSES, REALTIME_STATS, MODELS '. |

## Usage Notes

Syntax DBMS_STATS.DELETE_SCHEMA_STATS ( ownname VARCHAR2, stattab VARCHAR2 DEFAULT NULL, statid VARCHAR2 DEFAULT NULL, statown VARCHAR2 DEFAULT NULL, no_invalidate BOOLEAN DEFAULT to_no_invalidate_type ( get_param('NO_INVALIDATE')), force BOOLEAN DEFAULT FALSE, stat_category VARCHAR2 DEFAULT DEFAULT_DEL_STAT_CATEGORY); Parameters Table 171-28 DELETE_SCHEMA_STATS Procedure Parameters Parameter Description ownname Specifies the name of the schema. stattab Identifies the table where statistics are stored. If stattab is NULL , then the procedure deletes statistics directly from the data dictionary. statid Specifies the identifier (optional) associated with these statistics within stattab . This parameter is only relevant if stattab is not NULL . statown Specifies the schema containing stattab (if different than ownname ). no_invalidate Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. You can change the default using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . force Indicates whether to force the deletion for locked statistics. When the value is TRUE , this procedure deletes table statistics even if locked. stat_category Specifies which statistics to process. The following values are supported: OBJECT_STATS — Specifies table statistics, column statistics, and index statistics. SYNOPSES — Specifies metadata for incremental statistics. REALTIME_STATS — Specifies only real-time statistics. MODELS — supports import, export, and deletion for regression models in real-time stats. You can specify a list of comma-delimited values. For example, ' OBJECT_STATS, SYNOPSES ' specifies table statistics, column statistics, index statistics, and synopses. The default value is ' OBJECT_STATS, SYNOPSES, REALTIME_STATS, MODELS '. Security Model To invoke this procedure you must be owner of the table or have the ANALYZE ANY privilege. For objects owned by SYS , you must be either the owner of the table or have either the ANALYZE ANY DICTIONARY privilege or the SYSDBA privilege. Exceptions ORA-20000 : Object does not exist or insufficient privileges