---
id: 19c__DBMS_WORKLOAD_REPLAY.GET_REPLAY_DIRECTORY
name: DBMS_WORKLOAD_REPLAY.GET_REPLAY_DIRECTORY
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.GET_REPLAY_DIRECTORY

This function returns the current replay directory set by the SET_REPLAY_DIRECTORY Procedure. It returns NULL if no replay directory has been set.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.GET_REPLAY_DIRECTORY
   RETURN VARCHAR2;
```

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_WORKLOAD_REPLAY.GET_REPLAY_DIRECTORY RETURN VARCHAR2;