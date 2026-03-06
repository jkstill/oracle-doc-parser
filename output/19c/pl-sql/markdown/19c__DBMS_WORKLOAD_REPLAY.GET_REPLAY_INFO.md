---
id: 19c__DBMS_WORKLOAD_REPLAY.GET_REPLAY_INFO
name: DBMS_WORKLOAD_REPLAY.GET_REPLAY_INFO
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.GET_REPLAY_INFO

This function retrieves information about the workload capture and the history of all the workload replay attempts from the stipulated directory.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.GET_REPLAY_INFO (
   replay_dir    IN VARCHAR2,
   load_details  IN BOOLEAN DFAULT FALSE)
 RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| replay_dir | VARCHAR2 | IN | (Mandatory) Name of the workload replay directory object (case sensitive). |
| load_details | BOOLEAN | IN | Load the divergence and tracked commits data. The default value is FALSE . |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_WORKLOAD_REPLAY.GET_REPLAY_INFO ( replay_dir IN VARCHAR2, load_details IN BOOLEAN DFAULT FALSE) RETURN NUMBER; Parameters Table 191-17 GET_REPLAY_INFO Function Parameters Parameter Description replay_dir (Mandatory) Name of the workload replay directory object (case sensitive). load_details Load the divergence and tracked commits data. The default value is FALSE . Return Values The procedure returns the CAPTURE_ID , which can be associated with both DBA_WORKLOAD_CAPTURES . ID and DBA_WORKLOAD_REPLAYS . CAPTURE_ID to access the imported information. Usage Notes The procedure first imports a row into DBA_WORKLOAD_CAPTURES which will contain information about the capture. It then imports a row for every replay attempt retrieved from the given replay directory into DBA_WORKLOAD_REPLAYS . The procedure will not insert new rows to DBA_WORKLOAD_CAPTURES and DBA_WORKLOAD_REPLAYS if these views already contain rows describing the capture and replay history present in the given directory.