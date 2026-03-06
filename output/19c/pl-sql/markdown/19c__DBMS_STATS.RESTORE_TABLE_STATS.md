---
id: 19c__DBMS_STATS.RESTORE_TABLE_STATS
name: DBMS_STATS.RESTORE_TABLE_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.RESTORE_TABLE_STATS

This procedure restores statistics of a table as of a specified timestamp ( as_of_timestamp ). It also restores statistics of associated indexes and columns.

## Syntax

```sql
DBMS_STATS.RESTORE_TABLE_STATS (
   ownname                   VARCHAR2, 
   tabname                   VARCHAR2, 
   as_of_timestamp           TIMESTAMP WITH TIME ZONE,
   restore_cluster_index     BOOLEAN DEFAULT FALSE,
   force                     BOOLEAN DEFAULT FALSE,
   no_invalidate             BOOLEAN DEFAULT to_no_invalidate_type
                                                    (GET_PARAM('NO_INVALIDATE')));
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | The schema of the table for which the statistics are to be restored |
| tabname | VARCHAR2 | IN | The table name |
| as_of_timestamp | TIMESTAMP | IN | The timestamp to which to restore statistics |
| restore_cluster_index | BOOLEAN | IN | If the table is part of a cluster, restore statistics of the cluster index if set to TRUE |
| force | BOOLEAN | IN | Restores statistics even if the table statistics are locked. If the table statistics were not locked at the specified timestamp, it unlocks the statistics. |
| no_invalidate | BOOLEAN | IN | Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. You can change the default using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . |

## Usage Notes

If the table statistics were locked at the specified timestamp the procedure will lock the statistics. The procedure will not restore user defined statistics. Syntax DBMS_STATS.RESTORE_TABLE_STATS ( ownname VARCHAR2, tabname VARCHAR2, as_of_timestamp TIMESTAMP WITH TIME ZONE, restore_cluster_index BOOLEAN DEFAULT FALSE, force BOOLEAN DEFAULT FALSE, no_invalidate BOOLEAN DEFAULT to_no_invalidate_type (GET_PARAM('NO_INVALIDATE'))); Parameters Table 171-115 RESTORE_TABLE_STATS Procedure Parameters Parameter Description ownname The schema of the table for which the statistics are to be restored tabname The table name as_of_timestamp The timestamp to which to restore statistics restore_cluster_index If the table is part of a cluster, restore statistics of the cluster index if set to TRUE force Restores statistics even if the table statistics are locked. If the table statistics were not locked at the specified timestamp, it unlocks the statistics. no_invalidate Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. You can change the default using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . Exceptions ORA-20000 : Object does not exist or insufficient privileges ORA-20001 : Invalid or inconsistent values ORA-20006 : Unable to restore statistics, statistics history not available Usage Notes To invoke this procedure you must be owner of the table, or you need the ANALYZE ANY privilege. For objects owned by SYS , you need to be either the owner of the table, or you need the ANALYZE ANY DICTIONARY privilege or the SYSDBA privilege.