---
id: 19c__DBMS_STATS.RESTORE_DICTIONARY_STATS
name: DBMS_STATS.RESTORE_DICTIONARY_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.RESTORE_DICTIONARY_STATS

This procedure restores statistics of all dictionary tables (tables of ' SYS ', ' SYSTEM ' and RDBMS component schemas) as of a specified timestamp ( as_of_timestamp ).

## Syntax

```sql
DBMS_STATS.RESTORE_DICTIONARY_STATS( 
   as_of_timestamp        TIMESTAMP WITH TIME ZONE, 
   force                  BOOLEAN DEFAULT FALSE,
   no_invalidate          BOOLEAN DEFAULT to_no_invalidate_type
                                                    (GET_PARAM('NO_INVALIDATE')));
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| as_of_timestamp | TIMESTAMP | IN | Timestamp to which to restore statistics |
| force | BOOLEAN | IN | Restores statistics even if their statistics are locked |
| no_invalidate | BOOLEAN | IN | Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. You can change the default using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . |

## Usage Notes

Syntax DBMS_STATS.RESTORE_DICTIONARY_STATS( as_of_timestamp TIMESTAMP WITH TIME ZONE, force BOOLEAN DEFAULT FALSE, no_invalidate BOOLEAN DEFAULT to_no_invalidate_type (GET_PARAM('NO_INVALIDATE'))); Parameters Table 171-111 RESTORE_DICTIONARY_STATS Procedure Parameters Parameter Description as_of_timestamp Timestamp to which to restore statistics force Restores statistics even if their statistics are locked no_invalidate Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. You can change the default using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . Usage Notes To run this procedure, you must have the SYSDBA or both ANALYZE ANY DICTIONARY and ANALYZE ANY system privilege. Exceptions ORA-20000 : Object does not exist or insufficient privileges ORA-20001 : Invalid or inconsistent values ORA-20006 : Unable to restore statistics, statistics history not available