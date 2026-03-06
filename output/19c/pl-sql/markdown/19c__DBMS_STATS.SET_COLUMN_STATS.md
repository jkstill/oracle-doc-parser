---
id: 19c__DBMS_STATS.SET_COLUMN_STATS
name: DBMS_STATS.SET_COLUMN_STATS
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.SET_COLUMN_STATS

This procedure sets column-related information.

## Syntax

```sql
DBMS_STATS.SET_COLUMN_STATS (
   ownname       VARCHAR2, 
   tabname       VARCHAR2, 
   colname       VARCHAR2, 
   partname      VARCHAR2 DEFAULT NULL,
   stattab       VARCHAR2 DEFAULT NULL, 
   statid        VARCHAR2 DEFAULT NULL,
   distcnt       NUMBER DEFAULT NULL,
   density       NUMBER DEFAULT NULL,
   nullcnt       NUMBER DEFAULT NULL,
   srec          StatRec DEFAULT NULL,
   avgclen       NUMBER DEFAULT NULL,
   flags         NUMBER DEFAULT NULL,
   statown       VARCHAR2 DEFAULT NULL,
   no_invalidate BOOLEAN DEFAULT to_no_invalidate_type(
                                    get_param('NO_INVALIDATE')),
   force         BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Name of the schema. |
| tabname | VARCHAR2 | IN | Name of the table to which this column belongs. |
| colname | VARCHAR2 | IN | Name of the column or extension |
| partname | VARCHAR2 | IN | Name of the table partition in which to store the statistics. If the table is partitioned and partname is NULL , then the statistics are stored at the global table level. |
| stattab | VARCHAR2 | IN | User statistics table identifier describing where to store the statistics. If stattab is NULL , then the statistics are stored directly in the dictionary. |
| statid | VARCHAR2 | IN | Identifier (optional) to associate with these statistics within stattab (Only pertinent if stattab is not NULL ) |
| ext_stats |  |  | User-defined statistics |
| stattypown |  |  | Schema of the statistics type |
| stattypname |  |  | Name of the statistics type |
| distcnt | NUMBER | IN | Number of distinct values |
| density | NUMBER | IN | Column density. If this value is NULL and if distcnt is not NULL , then density is derived from distcnt . |
| nullcnt | NUMBER | IN | Number of NULLs |
| srec | StatRec | IN | StatRec structure filled in by a call to PREPARE_COLUMN_VALUES or GET_COLUMN_STATS |
| avgclen | NUMBER | IN | Average length for the column (in bytes) |
| flags | NUMBER | IN | For internal Oracle use (should be left as NULL ) |
| statown | VARCHAR2 | IN | Schema containing stattab (if different than ownname ) |
| no_invalidate | BOOLEAN | IN | Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. You can change the default using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . |
| force | BOOLEAN | IN | Sets the values even if statistics of the column are locked |

## Usage Notes

In the version of this procedure that deals with user-defined statistics, the statistics type specified is the type to store in the dictionary, in addition to the actual user-defined statistics. If this statistics type is NULL , the statistics type associated with the index or column is stored. Syntax DBMS_STATS.SET_COLUMN_STATS ( ownname VARCHAR2, tabname VARCHAR2, colname VARCHAR2, partname VARCHAR2 DEFAULT NULL, stattab VARCHAR2 DEFAULT NULL, statid VARCHAR2 DEFAULT NULL, distcnt NUMBER DEFAULT NULL, density NUMBER DEFAULT NULL, nullcnt NUMBER DEFAULT NULL, srec StatRec DEFAULT NULL, avgclen NUMBER DEFAULT NULL, flags NUMBER DEFAULT NULL, statown VARCHAR2 DEFAULT NULL, no_invalidate BOOLEAN DEFAULT to_no_invalidate_type( get_param('NO_INVALIDATE')), force BOOLEAN DEFAULT FALSE); Use the following for user-defined statistics: DBMS_STATS.SET_COLUMN_STATS ( ownname VARCHAR2, tabname VARCHAR2, colname VARCHAR2, partname VARCHAR2 DEFAULT NULL, stattab VARCHAR2 DEFAULT NULL, statid VARCHAR2 DEFAULT NULL, ext_stats RAW, stattypown VARCHAR2 DEFAULT NULL, stattypname VARCHAR2 DEFAULT NULL, statown VARCHAR2 DEFAULT NULL, no_invalidate BOOLEAN DEFAULT to_no_invalidate_type( get_param('NO_INVALIDATE')), force BOOLEAN DEFAULT FALSE); Parameters Table 171-120 SET_COLUMN_STATS Procedure Parameters Parameter Description ownname Name of the schema. tabname Name of the table to which this column belongs. colname Name of the column or extension partname Name of the table partition in which to store the statistics. If the table is partitioned and partname is NULL , then the statistics are stored at the global table level. stattab User statistics table identifier describing where to store the statistics. If stattab is NULL , then the statistics are stored directly in the dictionary. statid Identifier (optional) to associate with these statistics within stattab (Only pertinent if stattab is not NULL ) ext_stats User-defined statistics stattypown Schema of the statistics type stattypname Name of the statistics type distcnt Number of distinct values density Column density. If this value is NULL and if distcnt is not NULL , then density is derived from distcnt . nullcnt Number of NULLs srec StatRec structure filled in by a call to PREPARE_COLUMN_VALUES or GET_COLUMN_STATS avgclen Average length for the column (in bytes) flags For internal Oracle use (should be left as NULL ) statown Schema containing stattab (if different than ownname ) no_invalidate Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. You can change the default using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . force Sets the values even if statistics of the column are locked Exceptions ORA-20000 : Object does not exist or insufficient privileges ORA-20001 : Invalid or inconsistent input values ORA-20005 : Object statistics are locked Usage Notes To invoke this procedure you must be owner of the table, or you need the ANALYZE ANY privilege. For objects owned by SYS , you need to be either the owner of the table, or you need the ANALYZE ANY DICTIONARY privilege or the SYSDBA privilege.