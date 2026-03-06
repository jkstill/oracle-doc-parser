---
id: 19c__DBMS_STATS.GET_COLUMN_STATS
name: DBMS_STATS.GET_COLUMN_STATS
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.GET_COLUMN_STATS

These overloaded procedures get column-related statistics. In the user-defined statistics version, the procedure returns the type of statistics stored.

## Syntax

```sql
DBMS_STATS.GET_COLUMN_STATS (
   ownname        VARCHAR2, 
   tabname        VARCHAR2, 
   colname        VARCHAR2, 
   partname       VARCHAR2 DEFAULT NULL,
   stattab        VARCHAR2 DEFAULT NULL, 
   statid         VARCHAR2 DEFAULT NULL,
   distcnt OUT    NUMBER, 
   density OUT    NUMBER,
   nullcnt OUT    NUMBER, 
   srec    OUT    StatRec,
   avgclen OUT    NUMBER,
   statown        VARCHAR2 DEFAULT NULL,
   realtime_stats BOOLEAN iDEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Name of the schema |
| tabname | VARCHAR2 | IN | Specifies the name of the table to which this column belongs. |
| colname | VARCHAR2 | IN | Specifies the name of the column or extension. |
| partname | VARCHAR2 | IN | Specifies the name of the table partition from which to get the statistics. If the table is partitioned, and if partname is NULL , then the procedure retrieves statistics at the global table level. |
| stattab | VARCHAR2 | IN | Specifies the statistics table ID describing where to retrieve the statistics. If stattab is NULL , then the procedure retrieves statistics directly from the data dictionary. |
| statid | VARCHAR2 | IN | Specifies an optional identifier associated with these statistics within stattab . This parameter is only relevant when stattab is not NULL . |
| ext_stats |  |  | Specifies the user-defined statistics. |
| stattypown |  |  | Specifies the schema of the statistics type. |
| stattypname |  |  | Specifies the name of the statistics type. |
| distcnt | NUMBER | OUT | Specifies the number of distinct values. |
| density | NUMBER | OUT | Specifies the column density. |
| nullcnt | NUMBER | OUT | Specifies the number of NULL values. |
| srec | StatRec | OUT | Specifies the structure holding the internal representation of the column minimum, maximum, and histogram values. |
| avgclen | NUMBER | OUT | Specifies the average length of the column (in bytes). |
| statown | VARCHAR2 | IN | Specifies the schema containing stattab (if different than ownname ). |
| realtime_stats | BOOLEAN | IN | Specifies whether to include real-time statistics. The default value is TRUE . When realtime_stats is FALSE , the database only includes optimizer statistics that were gathered by the GATHER_ * _STATS procedures. |

## Usage Notes

Syntax DBMS_STATS.GET_COLUMN_STATS ( ownname VARCHAR2, tabname VARCHAR2, colname VARCHAR2, partname VARCHAR2 DEFAULT NULL, stattab VARCHAR2 DEFAULT NULL, statid VARCHAR2 DEFAULT NULL, distcnt OUT NUMBER, density OUT NUMBER, nullcnt OUT NUMBER, srec OUT StatRec, avgclen OUT NUMBER, statown VARCHAR2 DEFAULT NULL, realtime_stats BOOLEAN iDEFAULT TRUE); Use the following for user-defined statistics: DBMS_STATS.GET_COLUMN_STATS ( ownname VARCHAR2, tabname VARCHAR2, colname VARCHAR2, partname VARCHAR2 DEFAULT NULL, stattab VARCHAR2 DEFAULT NULL, statid VARCHAR2 DEFAULT NULL, ext_stats OUT RAW, stattypown OUT VARCHAR2 DEFAULT NULL, stattypname OUT VARCHAR2 DEFAULT NULL, statown VARCHAR2 DEFAULT NULL); Parameters Table 171-63 GET_COLUMN_STATS Procedure Parameters Parameter Description ownname Name of the schema tabname Specifies the name of the table to which this column belongs. colname Specifies the name of the column or extension. partname Specifies the name of the table partition from which to get the statistics. If the table is partitioned, and if partname is NULL , then the procedure retrieves statistics at the global table level. stattab Specifies the statistics table ID describing where to retrieve the statistics. If stattab is NULL , then the procedure retrieves statistics directly from the data dictionary. statid Specifies an optional identifier associated with these statistics within stattab . This parameter is only relevant when stattab is not NULL . ext_stats Specifies the user-defined statistics. stattypown Specifies the schema of the statistics type. stattypname Specifies the name of the statistics type. distcnt Specifies the number of distinct values. density Specifies the column density. nullcnt Specifies the number of NULL values. srec Specifies the structure holding the internal representation of the column minimum, maximum, and histogram values. avgclen Specifies the average length of the column (in bytes). statown Specifies the schema containing stattab (if different than ownname ). realtime_stats Specifies whether to include real-time statistics. The default value is TRUE . When realtime_stats is FALSE , the database only includes optimizer statistics that were gathered by the GATHER_ * _STATS procedures. Security Model To invoke this procedure you must be owner of the table or have the ANALYZE ANY privilege. For objects owned by SYS , you must be the owner of the table, or have either the ANALYZE ANY DICTIONARY privilege or the SYSDBA privilege. Exceptions ORA-20000 : Object does not exist or insufficient privileges or no statistics have been stored for requested object Usage Notes Before invoking this procedure, ensure that the table exists.