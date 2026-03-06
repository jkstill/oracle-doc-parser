---
id: 19c__DBMS_ADDM.GET_REPORT
name: DBMS_ADDM.GET_REPORT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADDM
tags: [dbms_addm]
source_file: DBMS_ADDM.html
---

# DBMS_ADDM.GET_REPORT

This function retrieves the default text report of an executed ADDM task.

## Syntax

```sql
DBMS_ADDM.GET_REPORT (
   task_name           IN VARCHAR2)
  RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2) | IN | Name of the task |

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_ADDM.GET_REPORT ( task_name IN VARCHAR2) RETURN CLOB; Parameters Table 14-15 GET_REPORT Function Parameters Parameter Description task_name Name of the task Examples Set long 1000000 Set pagesize 50000 SELECT DBMS_ADDM.GET_REPORT('my_partial_analysis_mode_task') FROM DUAL;