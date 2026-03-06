---
id: 19c__DBMS_MVIEW.PURGE_LOG
name: DBMS_MVIEW.PURGE_LOG
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MVIEW
tags: [dbms_mview]
source_file: DBMS_MVIEW.html
---

# DBMS_MVIEW.PURGE_LOG

This procedure purges rows from the materialized view log.

## Syntax

```sql
DBMS_MVIEW.PURGE_LOG (
   master        IN   VARCHAR2,
   num           IN   BINARY_INTEGER := 1,
   flag          IN   VARCHAR2       := 'NOP');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| master | VARCHAR2 | IN | Name of the master table or master materialized view. |
| num | BINARY_INTEGER | IN | Number of least recently refreshed materialized views whose rows you want to remove from materialized view log. For example, the following statement deletes rows needed to refresh the two least recently refreshed materialized views: DBMS_MVIEW.PURGE_LOG('master_table', 2); To delete all rows in the materialized view log, indicate a high number of materialized views to disregard, as in this example: DBMS_MVIEW.PURGE_LOG('master_table',9999); This statement completely purges the materialized view log that corresponds to master_table if fewer than 9999 materialized views are based on master_table . A simple materialized view whose rows have been purged from the materialized view log must be completely refreshed the next time it is refreshed. |
| flag | VARCHAR2 | IN | Specify delete to guarantee that rows are deleted from the materialized view log for at least one materialized view. This parameter can override the setting for the parameter num . For example, the following statement deletes rows from the materialized view log that has dependency rows in the least recently refreshed materialized view: DBMS_MVIEW.PURGE_LOG('master_table',1,'delete'); |

## Usage Notes

Syntax DBMS_MVIEW.PURGE_LOG ( master IN VARCHAR2, num IN BINARY_INTEGER := 1, flag IN VARCHAR2 := 'NOP'); Parameters Table 113-8 PURGE_LOG Procedure Parameters Parameter Description master Name of the master table or master materialized view. num Number of least recently refreshed materialized views whose rows you want to remove from materialized view log. For example, the following statement deletes rows needed to refresh the two least recently refreshed materialized views: DBMS_MVIEW.PURGE_LOG('master_table', 2); To delete all rows in the materialized view log, indicate a high number of materialized views to disregard, as in this example: DBMS_MVIEW.PURGE_LOG('master_table',9999); This statement completely purges the materialized view log that corresponds to master_table if fewer than 9999 materialized views are based on master_table . A simple materialized view whose rows have been purged from the materialized view log must be completely refreshed the next time it is refreshed. flag Specify delete to guarantee that rows are deleted from the materialized view log for at least one materialized view. This parameter can override the setting for the parameter num . For example, the following statement deletes rows from the materialized view log that has dependency rows in the least recently refreshed materialized view: DBMS_MVIEW.PURGE_LOG('master_table',1,'delete');