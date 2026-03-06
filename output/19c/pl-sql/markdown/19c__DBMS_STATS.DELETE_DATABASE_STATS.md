---
id: 19c__DBMS_STATS.DELETE_DATABASE_STATS
name: DBMS_STATS.DELETE_DATABASE_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.DELETE_DATABASE_STATS

This procedure deletes statistics for all the tables in a database.

## Syntax

```sql
DBMS_STATS.DELETE_DATABASE_STATS (
   stattab          VARCHAR2 DEFAULT NULL, 
   statid           VARCHAR2 DEFAULT NULL,
   statown          VARCHAR2 DEFAULT NULL,
   no_invalidate    BOOLEAN  DEFAULT to_no_invalidate_type (
                                     get_param('NO_INVALIDATE')),
   force            BOOLEAN  DEFAULT FALSE,
   stat_category    VARCHAR2 DEFAULT DEFAULT_DEL_STAT_CATEGORY);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| stattab | VARCHAR2 | IN | User statistics table identifier describing from where to delete the statistics. If stattab is NULL , then the statistics are deleted directly in the dictionary. |
| statid | VARCHAR2 | IN | Identifier (optional) to associate with these statistics within stattab (Only pertinent if stattab is not NULL ) |
| statown | VARCHAR2 | IN | Schema containing stattab (if different from current schema) |
| no_invalidate | BOOLEAN | IN | Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. The default can be changed using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . |
| force | BOOLEAN | IN | When the value of this argument is TRUE , deletes statistics of tables in a database even if they are locked |
| stat_category | VARCHAR2 | IN | Statistics to delete. It accepts multiple values separated by comma: OBJECT_STATS — table statistics, column statistics and index statistics SYNOPSES — information to support incremental statistics REALTIME_STATS — specifies only real-time statistics. MODELS — supports import, export, and deletion for regression models in real-time stats. The default is ' OBJECT_STATS, SYNOPSES, REALTIME_STATS, MODELS ' |

## Usage Notes

Syntax DBMS_STATS.DELETE_DATABASE_STATS ( stattab VARCHAR2 DEFAULT NULL, statid VARCHAR2 DEFAULT NULL, statown VARCHAR2 DEFAULT NULL, no_invalidate BOOLEAN DEFAULT to_no_invalidate_type ( get_param('NO_INVALIDATE')), force BOOLEAN DEFAULT FALSE, stat_category VARCHAR2 DEFAULT DEFAULT_DEL_STAT_CATEGORY); Parameters Table 171-20 DELETE_DATABASE_STATS Procedure Parameters Parameter Description stattab User statistics table identifier describing from where to delete the statistics. If stattab is NULL , then the statistics are deleted directly in the dictionary. statid Identifier (optional) to associate with these statistics within stattab (Only pertinent if stattab is not NULL ) statown Schema containing stattab (if different from current schema) no_invalidate Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. The default can be changed using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . force When the value of this argument is TRUE , deletes statistics of tables in a database even if they are locked stat_category Statistics to delete. It accepts multiple values separated by comma: OBJECT_STATS — table statistics, column statistics and index statistics SYNOPSES — information to support incremental statistics REALTIME_STATS — specifies only real-time statistics. MODELS — supports import, export, and deletion for regression models in real-time stats. The default is ' OBJECT_STATS, SYNOPSES, REALTIME_STATS, MODELS ' Exceptions ORA-20000 : Object does not exist or insufficient privileges Usage Notes To run this procedure, you need to have the SYSDBA role or both ANALYZE ANY DICTIONARY and ANALYZE ANY system privileges.