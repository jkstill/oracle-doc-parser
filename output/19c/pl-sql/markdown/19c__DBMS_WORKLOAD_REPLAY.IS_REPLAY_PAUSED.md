---
id: 19c__DBMS_WORKLOAD_REPLAY.IS_REPLAY_PAUSED
name: DBMS_WORKLOAD_REPLAY.IS_REPLAY_PAUSED
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.IS_REPLAY_PAUSED

This function reports whether the replay is currently paused.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.IS_REPLAY_PAUSED
   RETURN BOOLEAN;
```

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_WORKLOAD_REPLAY.IS_REPLAY_PAUSED RETURN BOOLEAN; Return Values Returns TRUE if the PAUSE_REPLAY Procedure has been called successfully and the RESUME_REPLAY Procedure has not been called yet. Usage Notes A call to the START_REPLAY Procedure must have already been issued as a prerequisite.