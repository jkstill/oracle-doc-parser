---
id: 19c__DBMS_WORKLOAD_REPLAY.GET_DIVERGING_STATEMENT
name: DBMS_WORKLOAD_REPLAY.GET_DIVERGING_STATEMENT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.GET_DIVERGING_STATEMENT

This function retrieves information about a diverging call, including the statement text, the SQL ID, and the binds. If the replay of a recorded user call has data or error divergence, it is a diverging call.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.GET_DIVERGING_STATEMENT (
   replay_id    IN NUMBER,
   stream_id    IN NUMBER,
   call_counter IN NUMBER)
  RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| replay_id | NUMBER | IN | ID of the replay in which that call diverged |
| stream_id | NUMBER | IN | Stream ID of the diverging call |
| call_counter | NUMBER) | IN | Call counter of the diverging call |

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_WORKLOAD_REPLAY.GET_DIVERGING_STATEMENT ( replay_id IN NUMBER, stream_id IN NUMBER, call_counter IN NUMBER) RETURN CLOB; Parameters Table 191-16 GET_DIVERGING_STATEMENT Function Parameters Parameter Description replay_id ID of the replay in which that call diverged stream_id Stream ID of the diverging call call_counter Call counter of the diverging call Usage Notes Returns a CLOB formatted as XML that contains: SQL ID SQL Text Bind information: position, name and value This function will silently invoke the POPULATE_DIVERGENCE Procedure to read the information from the capture files. Therefore, if divergence has not been populated, then the first call to this function for a particular diverging call might take longer, especially in very large captures.