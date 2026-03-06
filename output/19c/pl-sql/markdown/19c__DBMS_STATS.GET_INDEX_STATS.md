---
id: 19c__DBMS_STATS.GET_INDEX_STATS
name: DBMS_STATS.GET_INDEX_STATS
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.GET_INDEX_STATS

This overloaded procedure gets all index-related statistics. In the form of this procedure that deals with user-defined statistics, the statistics type returned is the type stored, in addition to the user-defined statistics.

## Syntax

```sql
DBMS_STATS.GET_INDEX_STATS (
   ownname        VARCHAR2, 
   indname        VARCHAR2,
   partname       VARCHAR2 DEFAULT NULL,
   stattab        VARCHAR2 DEFAULT NULL, 
   statid         VARCHAR2 DEFAULT NULL,
   numrows    OUT NUMBER, 
   numlblks   OUT NUMBER,
   numdist    OUT NUMBER, 
   avglblk    OUT NUMBER,
   avgdblk    OUT NUMBER, 
   clstfct    OUT NUMBER,
   indlevel   OUT NUMBER,
   statown        VARCHAR2 DEFAULT NULL);

DBMS_STATS.GET_INDEX_STATS (
   ownname        VARCHAR2, 
   indname        VARCHAR2,
   partname       VARCHAR2 DEFAULT NULL,
   stattab        VARCHAR2 DEFAULT NULL, 
   statid         VARCHAR2 DEFAULT NULL,
   numrows    OUT NUMBER, 
   numlblks   OUT NUMBER,
   numdist    OUT NUMBER, 
   avglblk    OUT NUMBER,
   avgdblk    OUT NUMBER, 
   clstfct    OUT NUMBER,
   indlevel   OUT NUMBER,
   statown        VARCHAR2 DEFAULT NULL,
   guessq     OUT NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Name of the schema |
| indname | VARCHAR2 | IN | Name of the index |
| partname | VARCHAR2 | IN | Name of the index partition for which to get the statistics. If the index is partitioned and if partname is NULL , then the statistics are retrieved for the global index level. |
| stattab | VARCHAR2 | IN | User statistics table identifier describing from where to retrieve the statistics. If stattab is NULL , then the statistics are retrieved directly from the dictionary. |
| statid | VARCHAR2 | IN | Identifier (optional) to associate with these statistics within stattab (Only pertinent if stattab is not NULL ) |
| ext_stats |  |  | User-defined statistics |
| stattypown |  |  | Schema of the statistics type |
| stattypname |  |  | Name of the statistics type |
| numrows | NUMBER | OUT | Number of rows in the index (partition) |
| numlblks | NUMBER | OUT | Number of leaf blocks in the index (partition) |
| numdist | NUMBER | OUT | Number of distinct keys in the index (partition) |
| avglblk | NUMBER | OUT | Average integral number of leaf blocks in which each distinct key appears for this index (partition) |
| avgdblk | NUMBER | OUT | Average integral number of data blocks in the table pointed to by a distinct key for this index (partition) |
| clstfct | NUMBER | OUT | Clustering factor for the index (partition) |
| indlevel | NUMBER | OUT | Height of the index (partition) |
| statown | VARCHAR2 | IN | Schema containing stattab (if different than ownname ) |
| guessq | NUMBER) | OUT | Guess quality for the index (partition) |

## Usage Notes

Syntax DBMS_STATS.GET_INDEX_STATS ( ownname VARCHAR2, indname VARCHAR2, partname VARCHAR2 DEFAULT NULL, stattab VARCHAR2 DEFAULT NULL, statid VARCHAR2 DEFAULT NULL, numrows OUT NUMBER, numlblks OUT NUMBER, numdist OUT NUMBER, avglblk OUT NUMBER, avgdblk OUT NUMBER, clstfct OUT NUMBER, indlevel OUT NUMBER, statown VARCHAR2 DEFAULT NULL); DBMS_STATS.GET_INDEX_STATS ( ownname VARCHAR2, indname VARCHAR2, partname VARCHAR2 DEFAULT NULL, stattab VARCHAR2 DEFAULT NULL, statid VARCHAR2 DEFAULT NULL, numrows OUT NUMBER, numlblks OUT NUMBER, numdist OUT NUMBER, avglblk OUT NUMBER, avgdblk OUT NUMBER, clstfct OUT NUMBER, indlevel OUT NUMBER, statown VARCHAR2 DEFAULT NULL, guessq OUT NUMBER); Use the following form of the procedure for user-defined statistics: DBMS_STATS.GET_INDEX_STATS ( ownname VARCHAR2, indname VARCHAR2, partname VARCHAR2 DEFAULT NULL, stattab VARCHAR2 DEFAULT NULL, statid VARCHAR2 DEFAULT NULL, ext_stats OUT RAW, stattypown OUT VARCHAR2 DEFAULT NULL, stattypname OUT VARCHAR2 DEFAULT NULL, statown VARCHAR2 DEFAULT NULL); Parameters Table 171-64 GET_INDEX_STATS Procedure Parameters Parameter Description ownname Name of the schema indname Name of the index partname Name of the index partition for which to get the statistics. If the index is partitioned and if partname is NULL , then the statistics are retrieved for the global index level. stattab User statistics table identifier describing from where to retrieve the statistics. If stattab is NULL , then the statistics are retrieved directly from the dictionary. statid Identifier (optional) to associate with these statistics within stattab (Only pertinent if stattab is not NULL ) ext_stats User-defined statistics stattypown Schema of the statistics type stattypname Name of the statistics type numrows Number of rows in the index (partition) numlblks Number of leaf blocks in the index (partition) numdist Number of distinct keys in the index (partition) avglblk Average integral number of leaf blocks in which each distinct key appears for this index (partition) avgdblk Average integral number of data blocks in the table pointed to by a distinct key for this index (partition) clstfct Clustering factor for the index (partition) indlevel Height of the index (partition) statown Schema containing stattab (if different than ownname ) guessq Guess quality for the index (partition) Security Model Before invoking this procedure, ensure that the table exists. To invoke this procedure you must be owner of the table, or you need the ANALYZE ANY privilege. For objects owned by SYS , you need to be either the owner of the table, or you need the ANALYZE ANY DICTIONARY privilege or the SYSDBA privilege. Exceptions ORA-20000 : Object does not exist or insufficient privileges or no statistics have been stored for requested object Usage Notes The optimizer uses the cached data to estimate number of cached blocks for index or statistics table access. The database calculates the total cost of the operation by combining the I/O cost of reading not cached blocks from disk, the CPU cost of getting cached blocks from the buffer cache, and the CPU cost of processing the data. The database maintains cachedblk and cachehit at all times. However, the database uses the corresponding caching statistics for optimization as part of the table and index statistics only when the user calls the DBMS_STATS.GATHER_[TABLE/INDEX/SCHEMA/DATABASE]_STATS procedure for automatic mode or DBMS_STATS.GATHER_SYSTEM_STATS for manual mode. To prevent the user from utilizing inaccurate and unreliable data, the optimizer computes a “confidence factor” for each cachehit and a cachedblk for each object. If the confidence factor for the value meets confidence criteria, then the database uses this value; otherwise, the database uses defaults. The automatic maintenance algorithm for object caching statistics assumes that only one major database workload exists. The algorithm adjusts statistics to this workload, ignoring other "minor" workloads. If this assumption is false, then you must use manual mode for maintaining object caching statistics. The object caching statistics maintenance algorithm for automatic mode prevents you from using statistics in the following situations: When not enough data has been analyzed, such as when an object has been recently created When the system does not have one major workload resulting in averages not corresponding to real values See Also: Oracle Database SQL Tuning Guide to learn how to manage optimizer statistics