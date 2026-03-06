---
id: 19c__DBMS_WORKLOAD_CAPTURE.DELETE_FILTER
name: DBMS_WORKLOAD_CAPTURE.DELETE_FILTER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_CAPTURE
tags: [dbms_workload_capture]
source_file: DBMS_WORKLOAD_CAPTURE.html
---

# DBMS_WORKLOAD_CAPTURE.DELETE_FILTER

This procedure deletes a specified filter.

## Syntax

```sql
DBMS_WORKLOAD_CAPTURE.DELETE_FILTER (
   filter_name           IN   VARCHAR2(40) NOT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| filter_name | VARCHAR2(40) | IN | Filter to be deleted |

## Usage Notes

Syntax DBMS_WORKLOAD_CAPTURE.DELETE_FILTER ( filter_name IN VARCHAR2(40) NOT NULL); Parameters Table 190-5 DELETE_FILTER Procedure Parameters Parameter Description filter_name Filter to be deleted Usage Notes The DELETE_FILTER Procedure only affects filters that have not been used by any previous capture. Consequently, filters can be deleted only if they have been added using the ADD_FILTER Procedures after any capture has been completed. Filters that have been added using ADD_FILTER before a START_CAPTURE and FINISH_CAPTURE cannot be deleted anymore using this subprogram.