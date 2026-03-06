---
id: 19c__DBMS_WORKLOAD_REPLAY.ADD_CAPTURE
name: DBMS_WORKLOAD_REPLAY.ADD_CAPTURE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.ADD_CAPTURE

This function adds the given capture to the current schedule. The directory has to be a valid capture processed in the current database's version. It returns a unique ID that identifies this capture within this schedule.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.ADD_CAPTURE (
   capture_dir_name      IN    VARCHAR2,
   start_delay_seconds   IN    NUMBER  DEFAULT 0,
   stop_replay           IN    BOOLEAN FALSE,
   take_begin_snapshot   IN    BOOLEAN TRUE,
   take_end_snapshot     IN    BOOLEAN TRUE,
   query_only            IN    BOOLEAN DEFAULT FALSE)
 RETURN NUMBER;

DBMS_WORKLOAD_REPLAY.ADD_CAPTURE (
   capture_dir_name      IN    VARCHAR2,
   start_delay_seconds   IN    NUMBER  DEFAULT 0,
   stop_replay           IN    BOOLEAN FALSE,
   take_begin_snapshot   IN    BOOLEAN TRUE,
   take_end_snapshot     IN    BOOLEAN TRUE,
   query_only            IN    VARCHAR2 DEFAULT 'N')
 RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| capture_dir_name | VARCHAR2 | IN | Name of the OS directory containing the capture under the replay top-level directory |
| start_delay_seconds | NUMBER | IN | Delay time in seconds before the replay of this capture starts |
| stop_replay | BOOLEAN | IN | Stop the replay after it finishes |
| take_begin_snapshot | BOOLEAN | IN | Take an AWR snapshot when the replay of this capture starts |
| take_end_snapshot | BOOLEAN | IN | Take an AWR snapshot when the replay of this capture finishes |
| query_only | BOOLEAN | IN | Replay only the read-only queries of this workload capture |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_WORKLOAD_REPLAY.ADD_CAPTURE ( capture_dir_name IN VARCHAR2, start_delay_seconds IN NUMBER DEFAULT 0, stop_replay IN BOOLEAN FALSE, take_begin_snapshot IN BOOLEAN TRUE, take_end_snapshot IN BOOLEAN TRUE, query_only IN BOOLEAN DEFAULT FALSE) RETURN NUMBER; DBMS_WORKLOAD_REPLAY.ADD_CAPTURE ( capture_dir_name IN VARCHAR2, start_delay_seconds IN NUMBER DEFAULT 0, stop_replay IN BOOLEAN FALSE, take_begin_snapshot IN BOOLEAN TRUE, take_end_snapshot IN BOOLEAN TRUE, query_only IN VARCHAR2 DEFAULT 'N') RETURN NUMBER; Parameters Table 191-2 ADD_CAPTURE Function Parameters Parameter Description capture_dir_name Name of the OS directory containing the capture under the replay top-level directory start_delay_seconds Delay time in seconds before the replay of this capture starts stop_replay Stop the replay after it finishes take_begin_snapshot Take an AWR snapshot when the replay of this capture starts take_end_snapshot Take an AWR snapshot when the replay of this capture finishes query_only Replay only the read-only queries of this workload capture Usage Notes The SET_REPLAY_DIRECTORY Procedure must have already been called.