---
id: 19c__DBMS_WORKLOAD_CAPTURE.EXPORT_AWR
name: DBMS_WORKLOAD_CAPTURE.EXPORT_AWR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_CAPTURE
tags: [dbms_workload_capture]
source_file: DBMS_WORKLOAD_CAPTURE.html
---

# DBMS_WORKLOAD_CAPTURE.EXPORT_AWR

This procedure exports the AWR snapshots associated with a given capture ID.

## Syntax

```sql
DBMS_WORKLOAD_CAPTURE.EXPORT_AWR (
   capture_id     IN NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| capture_id | NUMBER) | IN | ID of the capture whose AWR snapshots are to be exported. (Mandatory) |

## Usage Notes

Syntax DBMS_WORKLOAD_CAPTURE.EXPORT_AWR ( capture_id IN NUMBER); Parameters Table 190-7 EXPORT_AWR Procedure Parameters Parameter Description capture_id ID of the capture whose AWR snapshots are to be exported. (Mandatory) Usage Notes This procedure works only if the corresponding workload capture was performed in the current database (meaning that the corresponding row in DBA_WORKLOAD_CAPTURES was not created by calling the GET_CAPTURE_INFO Function ) and the AWR snapshots that correspond to the original capture time period are still available.