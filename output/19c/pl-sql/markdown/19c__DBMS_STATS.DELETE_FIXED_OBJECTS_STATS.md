---
id: 19c__DBMS_STATS.DELETE_FIXED_OBJECTS_STATS
name: DBMS_STATS.DELETE_FIXED_OBJECTS_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.DELETE_FIXED_OBJECTS_STATS

This procedure deletes statistics of all fixed tables.

## Syntax

```sql
DBMS_STATS.DELETE_FIXED_OBJECTS_STATS (
   stattab          VARCHAR2 DEFAULT NULL, 
   statid           VARCHAR2 DEFAULT NULL,
   statown          VARCHAR2 DEFAULT NULL,
   no_invalidate    BOOLEAN  DEFAULT to_no_invalidate_type (
                                     get_param('NO_INVALIDATE')),
   force            BOOLEAN  DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| stattab | VARCHAR2 | IN | The user statistics table identifier describing from where to delete the current statistics. If stattab is NULL , the statistics will be deleted directly in the dictionary. |
| statid | VARCHAR2 | IN | The (optional) identifier to associate with these statistics within stattab . This only applies if stattab is not NULL . |
| statown | VARCHAR2 | IN | Schema containing stattab (if different from current schema) |
| no_invalidate | BOOLEAN | IN | Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. The default can be changed using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . |
| force | BOOLEAN | IN | Ignores the statistics lock on objects and deletes the statistics if set to TRUE |

## Usage Notes

Syntax DBMS_STATS.DELETE_FIXED_OBJECTS_STATS ( stattab VARCHAR2 DEFAULT NULL, statid VARCHAR2 DEFAULT NULL, statown VARCHAR2 DEFAULT NULL, no_invalidate BOOLEAN DEFAULT to_no_invalidate_type ( get_param('NO_INVALIDATE')), force BOOLEAN DEFAULT FALSE); Parameters Table 171-22 DELETE_FIXED_OBJECTS_STATS Procedure Parameters Parameter Description stattab The user statistics table identifier describing from where to delete the current statistics. If stattab is NULL , the statistics will be deleted directly in the dictionary. statid The (optional) identifier to associate with these statistics within stattab . This only applies if stattab is not NULL . statown Schema containing stattab (if different from current schema) no_invalidate Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. The default can be changed using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . force Ignores the statistics lock on objects and deletes the statistics if set to TRUE Usage Notes You must have the SYSDBA or ANALYZE ANY DICTIONARY system privilege to execute this procedure. Exceptions ORA-20000 : Insufficient privileges ORA-20002 : Bad user statistics table, may need to upgrade it