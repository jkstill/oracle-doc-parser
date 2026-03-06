---
id: 19c__DBMS_WORKLOAD_REPLAY.DELETE_FILTER
name: DBMS_WORKLOAD_REPLAY.DELETE_FILTER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.DELETE_FILTER

This procedure deletes the named filter.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.DELETE_FILTER(
   fname    IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| fname | VARCHAR2) | IN | (Mandatory) Name of the filter that must be deleted |

## Usage Notes

Syntax DBMS_WORKLOAD_REPLAY.DELETE_FILTER( fname IN VARCHAR2); Parameters Table 191-12 DELETE_FILTER Procedure Parameters Parameter Description fname (Mandatory) Name of the filter that must be deleted Usage Notes The DELETE_FILTER Procedure only affects filters that have not been used by any previous capture. Consequently, filters can be deleted only if they have been added using the ADD_FILTER Procedures after any capture has been completed. Filters that have been added using ADD_FILTER before a START_CAPTURE and FINISH_CAPTURE cannot be deleted anymore using this subprogram.