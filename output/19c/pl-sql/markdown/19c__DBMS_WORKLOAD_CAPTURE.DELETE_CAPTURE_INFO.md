---
id: 19c__DBMS_WORKLOAD_CAPTURE.DELETE_CAPTURE_INFO
name: DBMS_WORKLOAD_CAPTURE.DELETE_CAPTURE_INFO
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_CAPTURE
tags: [dbms_workload_capture]
source_file: DBMS_WORKLOAD_CAPTURE.html
---

# DBMS_WORKLOAD_CAPTURE.DELETE_CAPTURE_INFO

This procedure deletes the rows in the DBA_WORKLOAD_CAPTURES and DBA_WORKLOAD_FILTERS views that corresponds to the given workload capture ID.

## Syntax

```sql
DBMS_WORKLOAD_CAPTURE.DELETE_CAPTURE_INFO
   capture_id     IN   NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| capture_id | NUMBER) | IN | ID of the workload capture that needs to be deleted. Corresponds to DBA_WORKLOAD_CAPTURES . ID . (Mandatory) |

## Usage Notes

Syntax DBMS_WORKLOAD_CAPTURE.DELETE_CAPTURE_INFO capture_id IN NUMBER); Parameters Table 190-4 DELETE_CAPTURE_INFO Procedure Parameters Parameter Description capture_id ID of the workload capture that needs to be deleted. Corresponds to DBA_WORKLOAD_CAPTURES . ID . (Mandatory) Usage Notes Passing the ID of a capture that is in progress will first automatically stop that capture.