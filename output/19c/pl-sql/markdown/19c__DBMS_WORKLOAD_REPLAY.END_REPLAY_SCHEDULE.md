---
id: 19c__DBMS_WORKLOAD_REPLAY.END_REPLAY_SCHEDULE
name: DBMS_WORKLOAD_REPLAY.END_REPLAY_SCHEDULE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.END_REPLAY_SCHEDULE

This procedure wraps up the creation of the current schedule. The schedule is now saved and associated with the replay directory and can be used for a replay.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.END_REPLAY_SCHEDULE;
```

## Usage Notes

Syntax DBMS_WORKLOAD_REPLAY.END_REPLAY_SCHEDULE; Usage Notes The BEGIN_REPLAY_SCHEDULE Procedure must have already been called.