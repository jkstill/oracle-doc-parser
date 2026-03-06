---
id: 19c__DBMS_WORKLOAD_REPLAY.BEGIN_REPLAY_SCHEDULE
name: DBMS_WORKLOAD_REPLAY.BEGIN_REPLAY_SCHEDULE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.BEGIN_REPLAY_SCHEDULE

This procedure initiates the creation of a reusable replay schedule.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.BEGIN_REPLAY_SCHEDULE  (
   replay_dir_obj     IN     VARCHAR2,
   schedule_name      IN     VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| replay_dir_obj | VARCHAR2 | IN | Directory object that points to the replay directory that contains all the capture directories involved in the schedule |
| schedule_name | VARCHAR2) | IN | Name of the schedule to be replayed |

## Usage Notes

Syntax DBMS_WORKLOAD_REPLAY.BEGIN_REPLAY_SCHEDULE ( replay_dir_obj IN VARCHAR2, schedule_name IN VARCHAR2); Parameters Table 191-6 BEGIN_REPLAY_SCHEDULE Procedure Parameters Parameter Description replay_dir_obj Directory object that points to the replay directory that contains all the capture directories involved in the schedule schedule_name Name of the schedule to be replayed Usage Notes Only one schedule can be in creation mode at a time. Calling the subprogram again before end_replay_schedule will raise an error. Prerequisites: The workload capture was already processed using the PROCESS_CAPTURE Procedure in the same database version. The user must have copied the capture directory appropriately. The database is not in replay mode. The SET_REPLAY_DIRECTORY Procedure has already been called.