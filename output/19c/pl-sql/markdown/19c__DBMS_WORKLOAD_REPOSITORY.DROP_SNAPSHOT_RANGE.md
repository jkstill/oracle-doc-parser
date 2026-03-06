---
id: 19c__DBMS_WORKLOAD_REPOSITORY.DROP_SNAPSHOT_RANGE
name: DBMS_WORKLOAD_REPOSITORY.DROP_SNAPSHOT_RANGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY.DROP_SNAPSHOT_RANGE

This procedure drops a range of snapshots.

## Syntax

```sql
DBMS_WORKLOAD_REPOSITORY.DROP_SNAPSHOT_RANGE(
   low_snap_id    IN  NUMBER,
   high_snap_id   IN  NUMBER,
   dbid           IN  NUMBER   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| low_snap_id | NUMBER | IN | Low snapshot id of snapshots to drop. |
| high_snap_id | NUMBER | IN | High snapshot id of snapshots to drop. |
| dbid | NUMBER | IN | Database id (defaults to local DBID). |

## Usage Notes

Syntax DBMS_WORKLOAD_REPOSITORY.DROP_SNAPSHOT_RANGE( low_snap_id IN NUMBER, high_snap_id IN NUMBER, dbid IN NUMBER DEFAULT NULL); Parameters Table 192-33 DROP_SNAPSHOT_RANGE Procedure Parameters Parameter Description low_snap_id Low snapshot id of snapshots to drop. high_snap_id High snapshot id of snapshots to drop. dbid Database id (defaults to local DBID). Examples This example drops the range of snapshots between snapshot id 102 to 105 for the local database: EXECUTE DBMS_WORKLOAD_REPOSITORY.DROP_SNAPSHOT_RANGE(102, 105); If you query the dba_hist_snapshot view after the Drop Snapshot action, you will see that snapshots 102 to 105 are removed from the Workload Repository.