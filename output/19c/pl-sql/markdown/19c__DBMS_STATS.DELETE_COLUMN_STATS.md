---
id: 19c__DBMS_STATS.DELETE_COLUMN_STATS
name: DBMS_STATS.DELETE_COLUMN_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.DELETE_COLUMN_STATS

This procedure deletes column-related statistics.

## Syntax

```sql
DBMS_STATS.DELETE_COLUMN_STATS (
   ownname        VARCHAR2, 
   tabname        VARCHAR2, 
   colname        VARCHAR2, 
   partname       VARCHAR2 DEFAULT NULL,
   stattab        VARCHAR2 DEFAULT NULL, 
   statid         VARCHAR2 DEFAULT NULL,
   cascade_parts  BOOLEAN  DEFAULT TRUE,
   statown        VARCHAR2 DEFAULT NULL,
   no_invalidate  BOOLEAN  DEFAULT to_no_invalidate_type (
                                     get_param('NO_INVALIDATE')),
   force          BOOLEAN  DEFAULT FALSE,
   col_stat_type  VARCHAR2 DEFAULT 'ALL');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Name of the schema |
| tabname | VARCHAR2 | IN | Name of the table to which this column belongs |
| colname | VARCHAR2 | IN | Name of the column or extension |
| partname | VARCHAR2 | IN | Name of the table partition for which to delete the statistics. If the table is partitioned and if partname is NULL , then global column statistics are deleted. |
| stattab | VARCHAR2 | IN | User statistics table identifier describing from where to delete the statistics. If stattab is NULL , then the statistics are deleted directly from the dictionary. |
| statid | VARCHAR2 | IN | Identifier (optional) to associate with these statistics within stattab (Only pertinent if stattab is not NULL ). |
| cascade_parts | BOOLEAN | IN | If the table is partitioned and if partname is NULL , then setting this to true causes the deletion of statistics for this column for all underlying partitions as well. |
| statown | VARCHAR2 | IN | Schema containing stattab (if different than ownname ) |
| no_invalidate | BOOLEAN | IN | Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. The default can be changed using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . |
| force | BOOLEAN | IN | When value of this argument is TRUE , deletes column statistics even if locked |
| col_stat_type | VARCHAR2 | IN | Type of column statistics to be deleted. This argument takes the following values: HISTOGRAM - delete column histogram only ALL - delete base column statistics and histogram |

## Usage Notes

Syntax DBMS_STATS.DELETE_COLUMN_STATS ( ownname VARCHAR2, tabname VARCHAR2, colname VARCHAR2, partname VARCHAR2 DEFAULT NULL, stattab VARCHAR2 DEFAULT NULL, statid VARCHAR2 DEFAULT NULL, cascade_parts BOOLEAN DEFAULT TRUE, statown VARCHAR2 DEFAULT NULL, no_invalidate BOOLEAN DEFAULT to_no_invalidate_type ( get_param('NO_INVALIDATE')), force BOOLEAN DEFAULT FALSE, col_stat_type VARCHAR2 DEFAULT 'ALL'); Parameters Table 171-17 DELETE_COLUMN_STATS Procedure Parameters Parameter Description ownname Name of the schema tabname Name of the table to which this column belongs colname Name of the column or extension partname Name of the table partition for which to delete the statistics. If the table is partitioned and if partname is NULL , then global column statistics are deleted. stattab User statistics table identifier describing from where to delete the statistics. If stattab is NULL , then the statistics are deleted directly from the dictionary. statid Identifier (optional) to associate with these statistics within stattab (Only pertinent if stattab is not NULL ). cascade_parts If the table is partitioned and if partname is NULL , then setting this to true causes the deletion of statistics for this column for all underlying partitions as well. statown Schema containing stattab (if different than ownname ) no_invalidate Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. The default can be changed using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . force When value of this argument is TRUE , deletes column statistics even if locked col_stat_type Type of column statistics to be deleted. This argument takes the following values: HISTOGRAM - delete column histogram only ALL - delete base column statistics and histogram Exceptions ORA-20000 : Object does not exist or insufficient privileges ORA-20005 : Object statistics are locked Usage Notes To invoke this procedure you must be owner of the table, or you need the ANALYZE ANY privilege. For objects owned by SYS , you need to be either the owner of the table, or you need the ANALYZE ANY DICTIONARY privilege or the SYSDBA privilege.