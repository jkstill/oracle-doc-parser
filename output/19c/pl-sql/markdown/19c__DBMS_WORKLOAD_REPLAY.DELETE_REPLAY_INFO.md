---
id: 19c__DBMS_WORKLOAD_REPLAY.DELETE_REPLAY_INFO
name: DBMS_WORKLOAD_REPLAY.DELETE_REPLAY_INFO
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.DELETE_REPLAY_INFO

This procedure deletes the rows in DBA_WORKLOAD_REPLAYS that correspond to the given workload replay ID.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.DELETE_REPLAY_INFO (
   replay_id    IN  NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| replay_id | NUMBER) | IN | (Mandatory) ID of the workload replay that must be deleted. Corresponds to DBA_WORKLOAD_REPLAYS . ID |

## Usage Notes

Syntax DBMS_WORKLOAD_REPLAY.DELETE_REPLAY_INFO ( replay_id IN NUMBER); Parameters Table 191-13 DELETE_REPLAY_INFO Procedure Parameters Parameter Description replay_id (Mandatory) ID of the workload replay that must be deleted. Corresponds to DBA_WORKLOAD_REPLAYS . ID