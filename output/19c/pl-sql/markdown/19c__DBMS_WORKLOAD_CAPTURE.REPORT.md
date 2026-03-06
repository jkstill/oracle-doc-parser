---
id: 19c__DBMS_WORKLOAD_CAPTURE.REPORT
name: DBMS_WORKLOAD_CAPTURE.REPORT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_CAPTURE
tags: [dbms_workload_capture]
source_file: DBMS_WORKLOAD_CAPTURE.html
---

# DBMS_WORKLOAD_CAPTURE.REPORT

This function generates a report on the stipulated workload capture.

## Syntax

```sql
DBMS_WORKLOAD_CAPTURE.REPORT (
   capture_id      IN   NUMBER,
   format          IN   VARCHAR2)
 RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| capture_id | NUMBER | IN | ID of the workload capture whose capture report is required. (Mandatory) This relates to the directory that contains the workload capture on which the Report needs to be generated. Should be a valid DIRECTORY object that points to a valid directory in the host system that contains a workload capture. |
| format | VARCHAR2) | IN | Specifies the report format. Valid values are DBMS_WORKLOAD_CAPTURE . TYPE_TEXT and DBMS_WORKLOAD_CAPTURE . TYPE_HTML .(Mandatory) |

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_WORKLOAD_CAPTURE.REPORT ( capture_id IN NUMBER, format IN VARCHAR2) RETURN CLOB; Parameters Table 190-11 REPORT Function Parameters Parameter Description capture_id ID of the workload capture whose capture report is required. (Mandatory) This relates to the directory that contains the workload capture on which the Report needs to be generated. Should be a valid DIRECTORY object that points to a valid directory in the host system that contains a workload capture. format Specifies the report format. Valid values are DBMS_WORKLOAD_CAPTURE . TYPE_TEXT and DBMS_WORKLOAD_CAPTURE . TYPE_HTML .(Mandatory) Return Values The report body in the desired format returned as a CLOB . Table 190-12 Constants Used by Report Function Constant Type Value Description TYPE_HTML VARCHAR2(4) 'HTML' Generates the HTML version of the report TYPE_TEXT VARCHAR2(4) 'TEXT' Used as input to the format argument to generate the text version of the report