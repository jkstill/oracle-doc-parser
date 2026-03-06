---
id: 19c__DBMS_WORKLOAD_REPLAY.EXPORT_AWR
name: DBMS_WORKLOAD_REPLAY.EXPORT_AWR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.EXPORT_AWR

This procedure exports the AWR snapshots associated with a stipulated replay ID.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.EXPORT_AWR (
   replay_id    IN  NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| replay_id | NUMBER) | IN | (Mandatory) ID of the replay whose AWR snapshots are to be exported |

## Usage Notes

Syntax DBMS_WORKLOAD_REPLAY.EXPORT_AWR ( replay_id IN NUMBER); Parameters Table 191-14 EXPORT_AWR Function Parameters Parameter Description replay_id (Mandatory) ID of the replay whose AWR snapshots are to be exported Usage Notes At the end of each replay, the corresponding AWR snapshots are automatically exported. Consequently, there is no need to do this manually after a workload replay is complete, unless the automatic EXPORT_AWR invocation failed. This procedure will work only if the corresponding workload replay was performed in the current database (meaning that the corresponding row in DBA_WORKLOAD_REPLAYS was not created by calling the GET_REPLAY_INFO Function ) and the AWR snapshots that correspond to that replay time period are still available.