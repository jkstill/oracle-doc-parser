---
id: 19c__DBMS_WORKLOAD_CAPTURE.GET_CAPTURE_INFO
name: DBMS_WORKLOAD_CAPTURE.GET_CAPTURE_INFO
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_CAPTURE
tags: [dbms_workload_capture]
source_file: DBMS_WORKLOAD_CAPTURE.html
---

# DBMS_WORKLOAD_CAPTURE.GET_CAPTURE_INFO

This procedure retrieves all information regarding a workload capture present in the stipulated directory, imports the information into the DBA_WORKLOAD_CAPTURES and DBA_WORKLOAD_FILTERS views, and returns the appropriate DBA_WORKLOAD_CAPTURES . ID

## Syntax

```sql
DBMS_WORKLOAD_CAPTURE.GET_CAPTURE_INFO
   dir     IN   VARCHAR2)
  RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dir | VARCHAR2) | IN | Name of the DIRECTORY object (case sensitive) where all the workload capture files are located (Mandatory) |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_WORKLOAD_CAPTURE.GET_CAPTURE_INFO dir IN VARCHAR2) RETURN NUMBER; Parameters Table 190-9 GET_CAPTURE_INFO Function Parameters Parameter Description dir Name of the DIRECTORY object (case sensitive) where all the workload capture files are located (Mandatory) Usage Notes If an appropriate row describing the capture in the stipulated directory already exists in DBA_WORKLOAD_CAPTURES , the GET_CAPTURE_INFO Function simply returns that row's DBA_WORKLOAD_CAPTURES . ID . If no existing row matches the capture present in the stipulated directory a new row is inserted to DBA_WORKLOAD_CAPTURES and that row's ID is returned.