---
id: 19c__DBMS_SYNC_REFRESH.ABORT_REFRESH
name: DBMS_SYNC_REFRESH.ABORT_REFRESH
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SYNC_REFRESH
tags: [dbms_sync_refresh]
source_file: DBMS_SYNC_REFRESH.html
---

# DBMS_SYNC_REFRESH.ABORT_REFRESH

This procedure undoes all the changes made by PREPARE_REFRESH or EXECUTE_REFRESH for the specified sync refresh groups. It helps you to recover to a state where the tables and materialized views are usable and consistent in case they encounter unexpected errors.

## Syntax

```sql
DBMS_SYNC_REFRESH.ABORT_REFRESH (
   group_id      IN NUMBER);

DBMS_SYNC_REFRESH.ABORT_REFRESH (
   group_id_list IN DBMS_UTILITY.NUMBER_ARRAY);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| group_id | NUMBER) | IN | The group ID of a sync refresh group. |
| group_id_list | DBMS_UTILITY.NUMBER_ARRAY) | IN | An array of group IDs of the sync refresh groups to be aborted for sync refresh. |

## Usage Notes

This procedure is overloaded. Syntax DBMS_SYNC_REFRESH.ABORT_REFRESH ( group_id IN NUMBER); DBMS_SYNC_REFRESH.ABORT_REFRESH ( group_id_list IN DBMS_UTILITY.NUMBER_ARRAY); Parameters Table 173-2 ABORT_REFRESH Procedure Parameters Parameter Description group_id The group ID of a sync refresh group. group_id_list An array of group IDs of the sync refresh groups to be aborted for sync refresh. Usage Notes If called after PREPARE_REFRESH , this procedure drops the outside tables created by it and unlocks the tables and materialized views in the sync refresh group. If called after EXECUTE_REFRESH fails, this procedure restores the state of tables to before EXECUTE_REFRESH by undoing any partition exchanges which successfully finished. This procedure releases the locks placed on the tables in the sync refresh group which were placed on them by the PREPARE_REFRESH procedure. See " PREPARE_REFRESH Procedure " for a description of these locks. ABORT_REFRESH will work only if a PREPARE_REFRESH or EXECUTE_REFRESH statement has failed. It cannot be used after successful runs of those commands, and throws an error in such cases.