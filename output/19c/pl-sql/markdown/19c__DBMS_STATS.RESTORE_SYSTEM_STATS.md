---
id: 19c__DBMS_STATS.RESTORE_SYSTEM_STATS
name: DBMS_STATS.RESTORE_SYSTEM_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.RESTORE_SYSTEM_STATS

This procedure restores system statistics as of a specified timestamp ( as_of_timestamp ).

## Syntax

```sql
DBMS_STATS.RESTORE_SCHEMA_STATS( 
   as_of_timestamp        TIMESTAMP WITH TIME ZONE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| as_of_timestamp | TIMESTAMP | IN | The timestamp to which to restore statistics |

## Usage Notes

Syntax DBMS_STATS.RESTORE_SCHEMA_STATS( as_of_timestamp TIMESTAMP WITH TIME ZONE); Parameters Table 171-114 RESTORE_SYSTEM_STATS Procedure Parameters Parameter Description as_of_timestamp The timestamp to which to restore statistics Exceptions ORA-20000 : Object does not exist or insufficient privileges ORA-20001 : Invalid or inconsistent values ORA-20006 : Unable to restore statistics, statistics history not available Usage Notes To run this procedure, you need the GATHER_SYSTEM_STATISTICS role.