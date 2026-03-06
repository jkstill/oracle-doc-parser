---
id: 19c__DBMS_WORKLOAD_REPLAY.START_CONSOLIDATED_REPLAY
name: DBMS_WORKLOAD_REPLAY.START_CONSOLIDATED_REPLAY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.START_CONSOLIDATED_REPLAY

This procedure starts the replay of a multiple-capture capture. It should be used only for consolidated replays.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.START_CONSOLIDATED_REPLAY;
```

## Usage Notes

Syntax DBMS_WORKLOAD_REPLAY.START_CONSOLIDATED_REPLAY; Usage Notes Prerequisites: The call to the PREPARE_REPLAY Procedure was already issued. A sufficient number of external replay clients (WRC) that can faithfully replay the captured workload already started. The status of such external replay clients can be monitored using V$WORKLOAD_REPLAY_CLIENTS .