---
id: 19c__DBMS_WORKLOAD_REPLAY.INITIALIZE_CONSOLIDATED_REPLAY
name: DBMS_WORKLOAD_REPLAY.INITIALIZE_CONSOLIDATED_REPLAY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.INITIALIZE_CONSOLIDATED_REPLAY

This procedure puts the database state in INIT for a multiple-capture replay.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.INITIALIZE_CONSOLIDATED_REPLAY (
   replay_name        IN    VARCHAR2,
   schedule_name      IN    VARCHAR2,
   plsql_mode         IN    VARCHAR2 DEFAULT 'TOP_LEVEL');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| replay_name | VARCHAR2 | IN | (Mandatory) Name of the workload replay. Every replay of a processed workload capture can be given a name. |
| schedule_name | VARCHAR2 | IN | Name of the schedule to be replayed. It must have been created through the BEGIN_REPLAY_SCHEDULE Procedure for the replay directory replay_dir . |
| plsql_mode | VARCHAR2 | IN | Specifies the replay options for PL/SQL calls: TOP_LEVEL — only top-level PL/SQL calls are replayed EXTENDED — SQL executed from PL/SQL or top-level SQL PL/SQL if there is no SQL recorded inside the PL/SQL are replayed. All captures must have been done in ‘EXTENDED’ PL/SQL mode. |

## Usage Notes

It uses the replay_dir which has already been defined by the SET_REPLAY_DIRECTORY Procedure , pointing to a directory that contains all the capture directories involved in the schedule. It reads data about schedule schedule_name from the directory, and loads required connection data into the replay system. Syntax DBMS_WORKLOAD_REPLAY.INITIALIZE_CONSOLIDATED_REPLAY ( replay_name IN VARCHAR2, schedule_name IN VARCHAR2, plsql_mode IN VARCHAR2 DEFAULT 'TOP_LEVEL'); Parameters Table 191-20 INITIALIZE_CONSOLIDATED_REPLAY Procedure Parameters Parameter Description replay_name (Mandatory) Name of the workload replay. Every replay of a processed workload capture can be given a name. schedule_name Name of the schedule to be replayed. It must have been created through the BEGIN_REPLAY_SCHEDULE Procedure for the replay directory replay_dir . plsql_mode Specifies the replay options for PL/SQL calls: TOP_LEVEL — only top-level PL/SQL calls are replayed EXTENDED — SQL executed from PL/SQL or top-level SQL PL/SQL if there is no SQL recorded inside the PL/SQL are replayed. All captures must have been done in ‘EXTENDED’ PL/SQL mode. Usage Notes Prerequisites: Workload capture was already processed using the PROCESS_CAPTURE Procedure in the same database version. Database state has been logically restored to what it was at the beginning of the original workload capture. The SET_REPLAY_DIRECTORY Procedure has been called.