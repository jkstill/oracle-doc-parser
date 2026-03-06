---
id: 19c__DBA_WORKLOAD_REPLAY_SCHEDULES
name: DBA_WORKLOAD_REPLAY_SCHEDULES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_WORKLOAD_REPLAY_SCHEDULES.html
---

# DBA_WORKLOAD_REPLAY_SCHEDULES

DBA_WORKLOAD_REPLAY_SCHEDULES displays the names of replay schedules for the current replay directory.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SCHEDULE_NAME | VARCHAR2(128) | The name of a schedule to be replayed. It defines one or multiple workload captures, and the order to start their replays. |
| DIRECTORY | VARCHAR2(128) | Directory object name for the replay schedule name |
| STATUS | VARCHAR2(128) | NEW if the schedule is being created, CURRENT if the schedule is currently being used by a replay, otherwise NULL |

## Usage Notes

A replay schedule defines one or multiple workload captures, and the order to start their replays. The current replay directory is set by DBMS_WORKLOAD_REPLAY.SET_REPLAY_DIRECTORY('replay_dir') . Each row in the view contains information about one replay schedule. See Also: " DBA_WORKLOAD_SCHEDULE_CAPTURES " displays the workload captures in a replay schedule. " DBA_WORKLOAD_SCHEDULE_ORDERING " displays the order to start captures in a replay schedule. Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_WORKLOAD_REPLAY package See Also: " DBA_WORKLOAD_SCHEDULE_CAPTURES " displays the workload captures in a replay schedule. " DBA_WORKLOAD_SCHEDULE_ORDERING " displays the order to start captures in a replay schedule. Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_WORKLOAD_REPLAY package