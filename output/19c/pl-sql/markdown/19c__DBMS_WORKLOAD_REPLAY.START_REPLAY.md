---
id: 19c__DBMS_WORKLOAD_REPLAY.START_REPLAY
name: DBMS_WORKLOAD_REPLAY.START_REPLAY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.START_REPLAY

This procedure starts the workload replay.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.START_REPLAY;
```

## Usage Notes

All the external replay clients (WRC) that are currently connected to the replay database will automatically be notified, and those replay clients (WRC) will begin issuing the captured workload. It should only be used for consolidated replays. Syntax DBMS_WORKLOAD_REPLAY.START_REPLAY; Usage Notes Prerequisites: The call to the PREPARE_REPLAY Procedure was already issued. A sufficient number of external replay clients (WRC) that can faithfully replay the captured workload already started. The status of such external replay clients can be monitored using V$WORKLOAD_REPLAY_CLIENTS . Use the WRC's CALIBRATE mode to determine the number of replay clients that might be required to faithfully replay the captured workload. For example: $ wrc mode=calibrate replaydir=.