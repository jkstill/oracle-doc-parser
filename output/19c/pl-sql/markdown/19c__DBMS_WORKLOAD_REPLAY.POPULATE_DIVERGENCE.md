---
id: 19c__DBMS_WORKLOAD_REPLAY.POPULATE_DIVERGENCE
name: DBMS_WORKLOAD_REPLAY.POPULATE_DIVERGENCE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.POPULATE_DIVERGENCE

This procedure precomputes the divergence information for the given call, stream, or the whole replay so that the GET_DIVERGING_STATEMENT Function returns as quickly as possible for the precomputed calls.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.POPULATE_DIVERGENCE (
   replay_id    IN   NUMBER,
   stream_id    IN   NUMBER DEFAULT NULL,
   call_counter IN   NUMBER DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| replay_id | NUMBER | IN | ID of the replay |
| stream_id | NUMBER | IN | Stream ID of the diverging call. If NULL is provided, then divergence information is precomputed for all diverging calls in the given replay. |
| call_counter | NUMBER | IN | Call counter of the diverging call. If NULL is provided, then divergence information is precomputed for all diverging calls in the given stream. |

## Usage Notes

Syntax DBMS_WORKLOAD_REPLAY.POPULATE_DIVERGENCE ( replay_id IN NUMBER, stream_id IN NUMBER DEFAULT NULL, call_counter IN NUMBER DEFAULT NULL); Parameters Table 191-23 POPULATE_DIVERGENCE Procedure Parameters Parameter Description replay_id ID of the replay stream_id Stream ID of the diverging call. If NULL is provided, then divergence information is precomputed for all diverging calls in the given replay. call_counter Call counter of the diverging call. If NULL is provided, then divergence information is precomputed for all diverging calls in the given stream.