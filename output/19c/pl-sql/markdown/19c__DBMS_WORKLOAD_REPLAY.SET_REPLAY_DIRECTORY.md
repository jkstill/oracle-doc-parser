---
id: 19c__DBMS_WORKLOAD_REPLAY.SET_REPLAY_DIRECTORY
name: DBMS_WORKLOAD_REPLAY.SET_REPLAY_DIRECTORY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.SET_REPLAY_DIRECTORY

This procedure sets a directory that contains multiple workload captures as the current replay directory.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.SET_REPLAY_DIRECTORY (
   replay_dir    IN    VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| replay_dir | VARCHAR2) | IN | Name of the OS directory containing the captures for a workload consolidation |

## Usage Notes

Syntax DBMS_WORKLOAD_REPLAY.SET_REPLAY_DIRECTORY ( replay_dir IN VARCHAR2); Parameters Table 191-33 SET_REPLAY_DIRECTORY Procedure Parameters Parameter Description replay_dir Name of the OS directory containing the captures for a workload consolidation