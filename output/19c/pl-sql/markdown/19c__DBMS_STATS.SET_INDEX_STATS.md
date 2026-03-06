---
id: 19c__DBMS_STATS.SET_INDEX_STATS
name: DBMS_STATS.SET_INDEX_STATS
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.SET_INDEX_STATS

These procedures set index-related statistics.

## Syntax

```sql
DBMS_STATS.SET_INDEX_STATS (
   ownname       VARCHAR2,
   indname       VARCHAR2,
   partname      VARCHAR2  DEFAULT NULL,
   stattab       VARCHAR2  DEFAULT NULL,
   statid        VARCHAR2  DEFAULT NULL,
   numrows       NUMBER    DEFAULT NULL,
   numlblks      NUMBER    DEFAULT NULL,
   numdist       NUMBER    DEFAULT NULL,
   avglblk       NUMBER    DEFAULT NULL,
   avgdblk       NUMBER    DEFAULT NULL,
   clstfct       NUMBER    DEFAULT NULL,
   indlevel      NUMBER    DEFAULT NULL,
   flags         NUMBER    DEFAULT NULL,
   statown       VARCHAR2  DEFAULT NULL,
   no_invalidate BOOLEAN   DEFAULT to_no_invalidate_type(
                                    get_param('NO_INVALIDATE')),
   guessq        NUMBER    DEFAULT NULL,
   cachedblk     NUMBER    DEFAULT NULL,
   cachehit      NUMBER    DEFUALT NULL,
   force         BOOLEAN   DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Name of the schema |
| indname | VARCHAR2 | IN | Name of the index |
| partname | VARCHAR2 | IN | Name of the index partition in which to store the statistics. If the index is partitioned and if partname is NULL , then the statistics are stored at the global index level. |
| stattab | VARCHAR2 | IN | User statistics table identifier describing where to store the statistics. If stattab is NULL , then the statistics are stored directly in the dictionary. |
| statid | VARCHAR2 | IN | Identifier (optional) to associate with these statistics within stattab (Only pertinent if stattab is not NULL ) |
| ext_stats |  |  | User-defined statistics |
| stattypown |  |  | Schema of the statistics type |
| stattypname |  |  | Name of the statistics type |
| numrows | NUMBER | IN | Number of rows in the index (partition) |
| numlblks | NUMBER | IN | Number of leaf blocks in the index (partition) |
| numdist | NUMBER | IN | Number of distinct keys in the index (partition) |
| avglblk | NUMBER | IN | Average integral number of leaf blocks in which each distinct key appears for this index (partition). If not provided, then this value is derived from numlblks and numdist . |
| avgdblk | NUMBER | IN | Average integral number of data blocks in the table pointed to by a distinct key for this index (partition). If not provided, then this value is derived from clstfct and numdist . |
| clstfct | NUMBER | IN | See clustering_factor column of the all_indexes view for a description |
| indlevel | NUMBER | IN | Height of the index (partition) |
| flags | NUMBER | IN | For internal Oracle use (should be left as NULL ) |
| statown | VARCHAR2 | IN | Schema containing stattab (if different than ownname ) |
| no_invalidate | BOOLEAN | IN | Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. You can change the default using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . |
| guessq | NUMBER | IN | Guess quality. See the pct_direct_access column of the all_indexes view for a description. |
| cachedblk | NUMBER | IN | Internal use only. Do not set. |
| cachehit | NUMBER | IN | Internal use only. Do not set. |
| force | BOOLEAN | IN | Sets the values even if statistics of the index are locked |

## Usage Notes

The version of this procedure that accepts ext_stats sets statistics for use with domain indexes. The statistics type specified is the type to store in the dictionary, in addition to the actual user-defined statistics. If this statistics type is null, then the database stores the statistics type associated with the index or column. Syntax DBMS_STATS.SET_INDEX_STATS ( ownname VARCHAR2, indname VARCHAR2, partname VARCHAR2 DEFAULT NULL, stattab VARCHAR2 DEFAULT NULL, statid VARCHAR2 DEFAULT NULL, numrows NUMBER DEFAULT NULL, numlblks NUMBER DEFAULT NULL, numdist NUMBER DEFAULT NULL, avglblk NUMBER DEFAULT NULL, avgdblk NUMBER DEFAULT NULL, clstfct NUMBER DEFAULT NULL, indlevel NUMBER DEFAULT NULL, flags NUMBER DEFAULT NULL, statown VARCHAR2 DEFAULT NULL, no_invalidate BOOLEAN DEFAULT to_no_invalidate_type( get_param('NO_INVALIDATE')), guessq NUMBER DEFAULT NULL, cachedblk NUMBER DEFAULT NULL, cachehit NUMBER DEFUALT NULL, force BOOLEAN DEFAULT FALSE); Use the following syntax for user-defined domain index statistics: DBMS_STATS.SET_INDEX_STATS ( ownname VARCHAR2, indname VARCHAR2, partname VARCHAR2 DEFAULT NULL, stattab VARCHAR2 DEFAULT NULL, statid VARCHAR2 DEFAULT NULL, ext_stats RAW, stattypown VARCHAR2 DEFAULT NULL, stattypname VARCHAR2 DEFAULT NULL, statown VARCHAR2 DEFAULT NULL, no_invalidate BOOLEAN DEFAULT to_no_invalidate_type( get_param('NO_INVALIDATE')), force BOOLEAN DEFAULT FALSE); Parameters Table 171-125 SET_INDEX_STATS Procedure Parameters Parameter Description ownname Name of the schema indname Name of the index partname Name of the index partition in which to store the statistics. If the index is partitioned and if partname is NULL , then the statistics are stored at the global index level. stattab User statistics table identifier describing where to store the statistics. If stattab is NULL , then the statistics are stored directly in the dictionary. statid Identifier (optional) to associate with these statistics within stattab (Only pertinent if stattab is not NULL ) ext_stats User-defined statistics stattypown Schema of the statistics type stattypname Name of the statistics type numrows Number of rows in the index (partition) numlblks Number of leaf blocks in the index (partition) numdist Number of distinct keys in the index (partition) avglblk Average integral number of leaf blocks in which each distinct key appears for this index (partition). If not provided, then this value is derived from numlblks and numdist . avgdblk Average integral number of data blocks in the table pointed to by a distinct key for this index (partition). If not provided, then this value is derived from clstfct and numdist . clstfct See clustering_factor column of the all_indexes view for a description indlevel Height of the index (partition) flags For internal Oracle use (should be left as NULL ) statown Schema containing stattab (if different than ownname ) no_invalidate Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. You can change the default using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . guessq Guess quality. See the pct_direct_access column of the all_indexes view for a description. cachedblk Internal use only. Do not set. cachehit Internal use only. Do not set. force Sets the values even if statistics of the index are locked Security Model To invoke this procedure you must be owner of the table, or you need the ANALYZE ANY privilege. For objects owned by SYS , you need to be either the owner of the table, or you need the ANALYZE ANY DICTIONARY privilege or the SYSDBA privilege. Exceptions ORA-20000 : Object does not exist or insufficient privileges ORA-20001 : Invalid input value ORA-20005 : Object statistics are locked