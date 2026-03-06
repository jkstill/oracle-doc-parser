---
id: 19c__DBMS_WORKLOAD_REPLAY.PAUSE_REPLAY
name: DBMS_WORKLOAD_REPLAY.PAUSE_REPLAY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.PAUSE_REPLAY

This procedure pauses the in-progress workload replay.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.PAUSE_REPLAY;
```

## Usage Notes

All subsequent user calls from the replay clients will be stalled until either a call to the RESUME_REPLAY Procedure is issued or the replay is cancelled. Syntax DBMS_WORKLOAD_REPLAY.PAUSE_REPLAY; Usage Notes Prerequisite: A call to the START_REPLAY Procedure must have already been issued. User calls that were already in-progress when this procedure was invoked are allowed to run to completion. Only subsequent user calls, when issued, are paused.