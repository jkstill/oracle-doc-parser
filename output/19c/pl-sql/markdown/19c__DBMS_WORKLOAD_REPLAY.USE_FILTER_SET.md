---
id: 19c__DBMS_WORKLOAD_REPLAY.USE_FILTER_SET
name: DBMS_WORKLOAD_REPLAY.USE_FILTER_SET
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.USE_FILTER_SET

This procedure applies a filter set to a capture in the current replay schedule.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.USE_FILTER_SET( 
   capture_number   IN    VARCHAR2,
   filter_set       IN    VARCHAR2);

DBMS_WORKLOAD_REPLAY.USE_FILTER_SET( 
   filter_set       IN    VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| capture_number | VARCHAR2 | IN | Pointing to a capture of the current replay schedule |
| filter_set | VARCHAR2) | IN | Name of the filter set |

## Usage Notes

The filter set must have been created by calling the CREATE_FILTER_SET Procedure . Syntax DBMS_WORKLOAD_REPLAY.USE_FILTER_SET( capture_number IN VARCHAR2, filter_set IN VARCHAR2); DBMS_WORKLOAD_REPLAY.USE_FILTER_SET( filter_set IN VARCHAR2); Parameters Table 191-37 USE_FILTER_SET Procedure Parameters Parameter Description capture_number Pointing to a capture of the current replay schedule filter_set Name of the filter set Usage Notes The filter set must have been created by calling the CREATE_FILTER_SET Procedure .