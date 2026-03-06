---
id: 19c__DBMS_STATS.GATHER_INDEX_STATS
name: DBMS_STATS.GATHER_INDEX_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.GATHER_INDEX_STATS

This procedure gathers index statistics. It attempts to parallelize as much of the work as possible.

## Syntax

```sql
DBMS_STATS.GATHER_INDEX_STATS (
   ownname          VARCHAR2, 
   indname          VARCHAR2, 
   partname         VARCHAR2 DEFAULT NULL,
   estimate_percent NUMBER   DEFAULT to_estimate_percent_type 
                                                (GET_PARAM('ESTIMATE_PERCENT')),
   stattab          VARCHAR2 DEFAULT NULL, 
   statid           VARCHAR2 DEFAULT NULL,
   statown          VARCHAR2 DEFAULT NULL,
   degree           NUMBER   DEFAULT to_degree_type(get_param('DEGREE')),
   granularity      VARCHAR2 DEFAULT GET_PARAM('GRANULARITY'),
   no_invalidate    BOOLEAN  DEFAULT to_no_invalidate_type 
                                               (GET_PARAM('NO_INVALIDATE')),
   force            BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Schema of index to analyze |
| indname | VARCHAR2 | IN | Name of index |
| partname | VARCHAR2 | IN | Name of partition |
| estimate_percent | NUMBER | IN | Percentage of rows to estimate ( NULL means compute). The valid range is [0.000001,100] . Use the constant DBMS_STATS . AUTO_SAMPLE_SIZE to have Oracle determine the appropriate sample size for good statistics. This is the default.The default value can be changed using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . |
| stattab | VARCHAR2 | IN | User statistics table identifier describing where to save the current statistics |
| statid | VARCHAR2 | IN | Identifier (optional) to associate with these statistics within stattab |
| statown | VARCHAR2 | IN | Schema containing stattab (if different than ownname ) |
| degree | NUMBER | IN | Degree of parallelism. The default for degree is NULL . The default value can be changed using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . NULL means use the table default value specified by the DEGREE clause in the CREATE TABLE or ALTER TABLE statement. Use the constant DBMS_STATS.DEFAULT_DEGREE to specify the default value based on the initialization parameters. The AUTO_DEGREE value determines the degree of parallelism automatically. This is between 1 (serial execution) and DEFAULT_DEGREE (the system default value based on number of CPUs and initialization parameters) according to the size of the object. When using DEGREE=>NULL , DEGREE=>n , or DEGREE=>DBMS_STATS.DEFAULT_DEGREE , the current implementation of DBMS_STATS may use serial execution if the size of the object does not warrant parallel execution. |
| granularity | VARCHAR2 | IN | Granularity of statistics to collect (only pertinent if the table is partitioned). 'ALL' - Gathers all (subpartition, partition, and global) statistics 'AUTO' - Determines the granularity based on the partitioning type. This is the default value. 'DEFAULT' - Gathers global and partition-level statistics. This option is obsolete, and while currently supported, it is included in the documentation for legacy reasons only. You should use the ' GLOBAL AND PARTITION ' for this functionality. Note that the default value is now ' AUTO '. 'GLOBAL' - Gathers global statistics ' GLOBAL AND PARTITION ' - Gathers the global and partition level statistics. No subpartition level statistics are gathered even if it is a composite partitioned object. 'PARTITION '- Gathers partition-level statistics 'SUBPARTITION' - Gathers subpartition-level statistics. |
| no_invalidate | BOOLEAN | IN | Does not invalidate the dependent cursors if set to TRUE . The procedure invalidates the dependent cursors immediately if set to FALSE . Use DBMS_STATS . AUTO_INVALIDATE . to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . |
| force | BOOLEAN | IN | Gather statistics on object even if it is locked |

## Usage Notes

Restrictions are described in the individual parameters. This operation will not parallelize with certain types of indexes, including cluster indexes, domain indexes, and bitmap join indexes. The granularity and no_invalidate arguments are not relevant to these types of indexes. Syntax DBMS_STATS.GATHER_INDEX_STATS ( ownname VARCHAR2, indname VARCHAR2, partname VARCHAR2 DEFAULT NULL, estimate_percent NUMBER DEFAULT to_estimate_percent_type (GET_PARAM('ESTIMATE_PERCENT')), stattab VARCHAR2 DEFAULT NULL, statid VARCHAR2 DEFAULT NULL, statown VARCHAR2 DEFAULT NULL, degree NUMBER DEFAULT to_degree_type(get_param('DEGREE')), granularity VARCHAR2 DEFAULT GET_PARAM('GRANULARITY'), no_invalidate BOOLEAN DEFAULT to_no_invalidate_type (GET_PARAM('NO_INVALIDATE')), force BOOLEAN DEFAULT FALSE); Parameters Table 171-55 GATHER_INDEX_STATS Procedure Parameters Parameter Description ownname Schema of index to analyze indname Name of index partname Name of partition estimate_percent Percentage of rows to estimate ( NULL means compute). The valid range is [0.000001,100] . Use the constant DBMS_STATS . AUTO_SAMPLE_SIZE to have Oracle determine the appropriate sample size for good statistics. This is the default.The default value can be changed using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . stattab User statistics table identifier describing where to save the current statistics statid Identifier (optional) to associate with these statistics within stattab statown Schema containing stattab (if different than ownname ) degree Degree of parallelism. The default for degree is NULL . The default value can be changed using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . NULL means use the table default value specified by the DEGREE clause in the CREATE TABLE or ALTER TABLE statement. Use the constant DBMS_STATS.DEFAULT_DEGREE to specify the default value based on the initialization parameters. The AUTO_DEGREE value determines the degree of parallelism automatically. This is between 1 (serial execution) and DEFAULT_DEGREE (the system default value based on number of CPUs and initialization parameters) according to the size of the object. When using DEGREE=>NULL , DEGREE=>n , or DEGREE=>DBMS_STATS.DEFAULT_DEGREE , the current implementation of DBMS_STATS may use serial execution if the size of the object does not warrant parallel execution. granularity Granularity of statistics to collect (only pertinent if the table is partitioned). 'ALL' - Gathers all (subpartition, partition, and global) statistics 'AUTO' - Determines the granularity based on the partitioning type. This is the default value. 'DEFAULT' - Gathers global and partition-level statistics. This option is obsolete, and while currently supported, it is included in the documentation for legacy reasons only. You should use the ' GLOBAL AND PARTITION ' for this functionality. Note that the default value is now ' AUTO '. 'GLOBAL' - Gathers global statistics ' GLOBAL AND PARTITION ' - Gathers the global and partition level statistics. No subpartition level statistics are gathered even if it is a composite partitioned object. 'PARTITION '- Gathers partition-level statistics 'SUBPARTITION' - Gathers subpartition-level statistics. no_invalidate Does not invalidate the dependent cursors if set to TRUE . The procedure invalidates the dependent cursors immediately if set to FALSE . Use DBMS_STATS . AUTO_INVALIDATE . to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . force Gather statistics on object even if it is locked Exceptions ORA-20000 : Index does not exist or insufficient privileges ORA-20001 : Bad input value Usage Notes To invoke this procedure you must be owner of the table, or you need the ANALYZE ANY privilege. For objects owned by SYS , you need to be either the owner of the table, or you need the ANALYZE ANY DICTIONARY privilege or the SYSDBA privilege.