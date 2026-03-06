---
id: 19c__DBMS_WORKLOAD_REPLAY.CANCEL_REPLAY
name: DBMS_WORKLOAD_REPLAY.CANCEL_REPLAY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.CANCEL_REPLAY

This procedure cancels workload replay in progress. All the external replay clients (WRC) will automatically be notified to stop issuing the captured workload and exit.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.CANCEL_REPLAY (
   error_msg    IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| error_msg | VARCHAR2 | IN | An optional reason for cancelling the replay can be passed which is recorded into DBA_WORKLOAD_REPLAYS . ERROR_MESSAGE . |

## Usage Notes

Syntax DBMS_WORKLOAD_REPLAY.CANCEL_REPLAY ( error_msg IN VARCHAR2 DEFAULT NULL); Parameters Table 191-8 CANCEL_REPLAY Procedure Parameters Parameter Description error_msg An optional reason for cancelling the replay can be passed which is recorded into DBA_WORKLOAD_REPLAYS . ERROR_MESSAGE . Usage Notes Prerequisite: A call to the INITIALIZE_REPLAY Procedure , or PREPARE_REPLAY Procedure , or START_REPLAY Procedure was already issued.