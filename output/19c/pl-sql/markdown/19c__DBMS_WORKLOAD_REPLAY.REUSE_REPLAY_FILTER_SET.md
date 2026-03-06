---
id: 19c__DBMS_WORKLOAD_REPLAY.REUSE_REPLAY_FILTER_SET
name: DBMS_WORKLOAD_REPLAY.REUSE_REPLAY_FILTER_SET
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.REUSE_REPLAY_FILTER_SET

This procedure reuses filters in the specified filter set as if each were added using the ADD_SCHEDULE_ORDERING Function.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.REUSE_REPLAY_FILTER_SET( 
   replay_dir  IN VARCHAR2,
   filter_set  IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| replay_dir | VARCHAR2 | IN | Capture ID of the existing filter set with which it is associated |
| filter_set | VARCHAR2) | IN | Name of the filter set to be reused |

## Usage Notes

Each call adds one filter set, which is a collection of individual filters on various attributes. Also, a new filter rule can be added, and an existing filter can be deleted before invoking the CREATE_FILTER_SET Procedure to create a new filter set. Syntax DBMS_WORKLOAD_REPLAY.REUSE_REPLAY_FILTER_SET( replay_dir IN VARCHAR2, filter_set IN VARCHAR2); Parameters Table 191-31 REUSE_REPLAY_FILTER_SET Procedure Parameters Parameter Description replay_dir Capture ID of the existing filter set with which it is associated filter_set Name of the filter set to be reused