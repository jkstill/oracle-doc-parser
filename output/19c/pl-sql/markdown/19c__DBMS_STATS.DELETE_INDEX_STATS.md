---
id: 19c__DBMS_STATS.DELETE_INDEX_STATS
name: DBMS_STATS.DELETE_INDEX_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.DELETE_INDEX_STATS

This procedure deletes index-related statistics.

## Syntax

```sql
DBMS_STATS.DELETE_INDEX_STATS (
   ownname          VARCHAR2, 
   indname          VARCHAR2,
   partname         VARCHAR2 DEFAULT NULL,
   stattab          VARCHAR2 DEFAULT NULL, 
   statid           VARCHAR2 DEFAULT NULL,
   cascade_parts    BOOLEAN  DEFAULT TRUE,
   statown          VARCHAR2 DEFAULT NULL,
   no_invalidate    BOOLEAN  DEFAULT to_no_invalidate_type (
                                     get_param('NO_INVALIDATE')),
   stattype         VARCHAR2 DEFAULT 'ALL',
   force            BOOLEAN  DEFAULT FALSE);
   stat_category    VARCHAR2 DEFAULT DEFAULT_DEL_STAT_CATEGORY);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Name of the schema |
| indname | VARCHAR2 | IN | Name of the index |
| partname | VARCHAR2 | IN | Name of the index partition for which to delete the statistics. If the index is partitioned and if partname is NULL , then index statistics are deleted at the global level. |
| stattab | VARCHAR2 | IN | User statistics table identifier describing from where to delete the statistics. If stattab is NULL , then the statistics are deleted directly from the dictionary. |
| statid | VARCHAR2 | IN | Identifier (optional) to associate with these statistics within stattab (Only pertinent if stattab is not NULL ) |
| cascade_parts | BOOLEAN | IN | If the index is partitioned and if partname is NULL , then setting this to TRUE causes the deletion of statistics for this index for all underlying partitions as well |
| statown | VARCHAR2 | IN | Schema containing stattab (if different than ownname ) |
| no_invalidate | BOOLEAN | IN | Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. The default can be changed using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . |
| stattype | VARCHAR2 | IN | Statistics type |
| force | BOOLEAN | IN | When value of this argument is TRUE , deletes index statistics even if locked |
| stat_category | VARCHAR2 | IN | Statistics to delete. It accepts multiple values separated by comma: OBJECT_STATS — table statistics, column statistics and index statistics SYNOPSES — information to support incremental statistics REALTIME_STATS — Specifies only real-time statistics. MODELS — supports import, export, and deletion for regression models in real-time stats. The default is 'OBJECT_STATS, SYNOPSES, REALTIME_STATS, MODELS' |

## Usage Notes

Syntax DBMS_STATS.DELETE_INDEX_STATS ( ownname VARCHAR2, indname VARCHAR2, partname VARCHAR2 DEFAULT NULL, stattab VARCHAR2 DEFAULT NULL, statid VARCHAR2 DEFAULT NULL, cascade_parts BOOLEAN DEFAULT TRUE, statown VARCHAR2 DEFAULT NULL, no_invalidate BOOLEAN DEFAULT to_no_invalidate_type ( get_param('NO_INVALIDATE')), stattype VARCHAR2 DEFAULT 'ALL', force BOOLEAN DEFAULT FALSE); stat_category VARCHAR2 DEFAULT DEFAULT_DEL_STAT_CATEGORY); Parameters Table 171-23 DELETE_INDEX_STATS Procedure Parameters Parameter Description ownname Name of the schema indname Name of the index partname Name of the index partition for which to delete the statistics. If the index is partitioned and if partname is NULL , then index statistics are deleted at the global level. stattab User statistics table identifier describing from where to delete the statistics. If stattab is NULL , then the statistics are deleted directly from the dictionary. statid Identifier (optional) to associate with these statistics within stattab (Only pertinent if stattab is not NULL ) cascade_parts If the index is partitioned and if partname is NULL , then setting this to TRUE causes the deletion of statistics for this index for all underlying partitions as well statown Schema containing stattab (if different than ownname ) no_invalidate Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. The default can be changed using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . stattype Statistics type force When value of this argument is TRUE , deletes index statistics even if locked stat_category Statistics to delete. It accepts multiple values separated by comma: OBJECT_STATS — table statistics, column statistics and index statistics SYNOPSES — information to support incremental statistics REALTIME_STATS — Specifies only real-time statistics. MODELS — supports import, export, and deletion for regression models in real-time stats. The default is 'OBJECT_STATS, SYNOPSES, REALTIME_STATS, MODELS' Exceptions ORA-20000 : Object does not exist or insufficient privileges ORA-20005 : Object statistics are locked Usage Notes To invoke this procedure you must be owner of the table, or you need the ANALYZE ANY privilege. For objects owned by SYS , you need to be either the owner of the table, or you need the ANALYZE ANY DICTIONARY privilege or the SYSDBA privilege.