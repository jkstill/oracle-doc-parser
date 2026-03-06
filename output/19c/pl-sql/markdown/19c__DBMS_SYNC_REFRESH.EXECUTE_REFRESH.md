---
id: 19c__DBMS_SYNC_REFRESH.EXECUTE_REFRESH
name: DBMS_SYNC_REFRESH.EXECUTE_REFRESH
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SYNC_REFRESH
tags: [dbms_sync_refresh]
source_file: DBMS_SYNC_REFRESH.html
---

# DBMS_SYNC_REFRESH.EXECUTE_REFRESH

This procedure executes sync refresh on the sync refresh groups prepared by DBMS_SYNC_REFRESH.PREPARE_REFRESH . These groups are identified by their group IDs.

## Syntax

```sql
DBMS_SYNC_REFRESH.EXECUTE_REFRESH (
   group_id   IN NUMBER);

DBMS_SYNC_REFRESH.EXECUTE_REFRESH (
   group_id_list  IN DBMS_UTILITY.NUMBER_ARRAY);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| group_id | NUMBER) | IN | The group ID of a sync refresh group. |
| group_id_list | DBMS_UTILITY.NUMBER_ARRAY) | IN | An array of group IDs of the sync refresh groups to be executed for sync refresh. |

## Usage Notes

Note this procedure will only perform the refresh on those materialized views that have been registered for synch refresh; any other materialized views will become stale once this procedure completes. For more information on how to monitor the status of the two synchronous refresh operations, PREPARE_REFRESH and EXECUTE_REFRESH and how to troubleshoot errors that might occur using the information in the catalog views, refer to "Trouble-Shooting Synchronous Refresh Operations" in Oracle Database Data Warehousing Guide. This procedure is overloaded. Syntax DBMS_SYNC_REFRESH.EXECUTE_REFRESH ( group_id IN NUMBER); DBMS_SYNC_REFRESH.EXECUTE_REFRESH ( group_id_list IN DBMS_UTILITY.NUMBER_ARRAY); Parameters Table 173-5 EXECUTE_REFRESH Procedure Parameters Parameter Description group_id The group ID of a sync refresh group. group_id_list An array of group IDs of the sync refresh groups to be executed for sync refresh. Usage Notes This procedure also releases the locks placed on the tables in the sync refresh group that were placed on them by the PREPARE_REFRESH procedure. See " PREPARE_REFRESH Procedure " for a description of these locks and Oracle Database Reference for information regarding the status of the refresh operation after DBMS_SYNC_REFRESH.EXECUTE_REFRESH .