---
id: 19c__DBMS_STATS.IMPORT_COLUMN_STATS
name: DBMS_STATS.IMPORT_COLUMN_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.IMPORT_COLUMN_STATS

This procedure retrieves statistics for a particular column from the user statistics table identified by stattab and stores them in the dictionary.

## Syntax

```sql
DBMS_STATS.IMPORT_COLUMN_STATS (
   ownname       VARCHAR2, 
   tabname       VARCHAR2, 
   colname       VARCHAR2,
   partname      VARCHAR2 DEFAULT NULL,
   stattab       VARCHAR2, 
   statid        VARCHAR2 DEFAULT NULL,
   statown       VARCHAR2 DEFAULT NULL,
   no_invalidate BOOLEAN DEFAULT to_no_invalidate_type (
                                     get_param('NO_INVALIDATE')),
   force         BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Name of the schema |
| tabname | VARCHAR2 | IN | Name of the table to which this column belongs |
| colname | VARCHAR2 | IN | Name of the column or extension |
| partname | VARCHAR2 | IN | Name of the table partition. If the table is partitioned and if partname is NULL , then global and partition column statistics are imported. |
| stattab | VARCHAR2 | IN | User statistics table identifier describing from where to retrieve the statistics |
| statid | VARCHAR2 | IN | Identifier to associate with these statistics within stattab (optional) |
| statown | VARCHAR2 | IN | Schema containing stattab (if different than ownname ) |
| no_invalidate | BOOLEAN | IN | Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. You can change the default using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . |
| force | BOOLEAN | IN | If set to TRUE , imports statistics even if statistics are locked |

## Usage Notes

Syntax DBMS_STATS.IMPORT_COLUMN_STATS ( ownname VARCHAR2, tabname VARCHAR2, colname VARCHAR2, partname VARCHAR2 DEFAULT NULL, stattab VARCHAR2, statid VARCHAR2 DEFAULT NULL, statown VARCHAR2 DEFAULT NULL, no_invalidate BOOLEAN DEFAULT to_no_invalidate_type ( get_param('NO_INVALIDATE')), force BOOLEAN DEFAULT FALSE); Parameters Table 171-71 IMPORT_COLUMN_STATS Procedure Parameters Parameter Description ownname Name of the schema tabname Name of the table to which this column belongs colname Name of the column or extension partname Name of the table partition. If the table is partitioned and if partname is NULL , then global and partition column statistics are imported. stattab User statistics table identifier describing from where to retrieve the statistics statid Identifier to associate with these statistics within stattab (optional) statown Schema containing stattab (if different than ownname ) no_invalidate Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. You can change the default using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . force If set to TRUE , imports statistics even if statistics are locked Usage Notes To invoke this procedure you must be owner of the table, or you need the ANALYZE ANY privilege. For objects owned by SYS , you need to be either the owner of the table, or you need the ANALYZE ANY DICTIONARY privilege or the SYSDBA privilege. Exceptions ORA-20000 : Object does not exist or insufficient privileges ORA-20001 : Invalid or inconsistent values in the user statistics table ORA-20005 : Object statistics are locked Usage Notes Oracle does not support export or import of statistics across databases of different character sets.