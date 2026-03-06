---
id: 19c__DBMS_STATS.IMPORT_DATABASE_STATS
name: DBMS_STATS.IMPORT_DATABASE_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.IMPORT_DATABASE_STATS

This procedure imports statistics for all objects in the database from the user statistics table and stores them in the data dictionary.

## Syntax

```sql
DBMS_STATS.IMPORT_DATABASE_STATS (
   stattab         VARCHAR2, 
   statid          VARCHAR2 DEFAULT NULL,
   statown         VARCHAR2 DEFAULT NULL,
   no_invalidate   BOOLEAN DEFAULT to_no_invalidate_type(
                                    get_param('NO_INVALIDATE')),
   force           BOOLEAN DEFAULT FALSE,
   stat_category   VARCHAR2 DEFAULT DEFAULT_STAT_CATEGORY);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| stattab | VARCHAR2 | IN | Specifies the statistics table that contains the statistics to be imported. |
| statid | VARCHAR2 | IN | Identifier (optional) to associate with these statistics within stattab |
| statown | VARCHAR2 | IN | Schema containing stattab (if different from current schema) |
| no_invalidate | BOOLEAN | IN | Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. The default can be changed using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . |
| force | BOOLEAN | IN | Overrides statistics locked at the object (table) level: TRUE - Ignores the statistics lock and imports the statistics FALSE - The statistics will be imported only if they are not locked |
| stat_category | VARCHAR2 | IN | Specifies what statistics to import, accepting multiple values separated by a comma. Values supported: OBJECT_STATS - table statistics, column statistics and index statistics (Default) SYNOPSES - information to support incremental statistics |

## Usage Notes

Syntax DBMS_STATS.IMPORT_DATABASE_STATS ( stattab VARCHAR2, statid VARCHAR2 DEFAULT NULL, statown VARCHAR2 DEFAULT NULL, no_invalidate BOOLEAN DEFAULT to_no_invalidate_type( get_param('NO_INVALIDATE')), force BOOLEAN DEFAULT FALSE, stat_category VARCHAR2 DEFAULT DEFAULT_STAT_CATEGORY); Parameters Table 171-73 IMPORT_DATABASE_STATS Procedure Parameters Parameter Description stattab Specifies the statistics table that contains the statistics to be imported. statid Identifier (optional) to associate with these statistics within stattab statown Schema containing stattab (if different from current schema) no_invalidate Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. The default can be changed using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . force Overrides statistics locked at the object (table) level: TRUE - Ignores the statistics lock and imports the statistics FALSE - The statistics will be imported only if they are not locked stat_category Specifies what statistics to import, accepting multiple values separated by a comma. Values supported: OBJECT_STATS - table statistics, column statistics and index statistics (Default) SYNOPSES - information to support incremental statistics Security Model You must have either the SYSDBA privilege or both the ANALYZE ANY DICTIONARY and ANALYZE ANY system privileges. Exceptions ORA-20000 : Object does not exist or insufficient privileges ORA-20001 : Invalid or inconsistent values in the user statistics table Usage Notes Oracle Database does not support export or import of statistics across databases of different character sets.