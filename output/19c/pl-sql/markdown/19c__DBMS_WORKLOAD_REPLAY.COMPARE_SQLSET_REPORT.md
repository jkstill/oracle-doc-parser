---
id: 19c__DBMS_WORKLOAD_REPLAY.COMPARE_SQLSET_REPORT
name: DBMS_WORKLOAD_REPLAY.COMPARE_SQLSET_REPORT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.COMPARE_SQLSET_REPORT

This procedure generates a report comparing a sqlset captured during replay to one captured during workload capture or to one captured during another replay of the same capture.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.COMPARE_SQLSET_REPORT (
   replay_id1    IN NUMBER,
   replay_id2    IN NUMBER,
   format        IN VARCHAR2,
   r_level       IN VARCHAR2 DEFAULT 'ALL',
   r_sections    IN VARCHAR2 DEFAULT 'ALL',
   result        OUT CLOB )
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| replay_id1 | NUMBER | IN | First ID of the workload replay after a change |
| replay_id2 | NUMBER | IN | Second ID of the workload replay before a change. If this is NULL , then the comparison is done with the capture. |
| format | VARCHAR2 | IN | Specifies the report format. Valid values are DBMS_WORKLOAD_CAPTURE . TYPE_HTML , DBMS_WORKLOAD_CAPTURE . TYPE_XML and DBMS_WORKLOAD_CAPTURE.TYPE_TEXT . |
| r_level | VARCHAR2 | IN | See level parameter in the REPORT_ANALYSIS_TASK Function in the DBMS_SQLPA package |
| r_sections | VARCHAR2 | IN | See section parameter in the REPORT_ANALYSIS_TASK Function in the DBMS_SQLPA package |
| result | CLOB | OUT | Output of the report ( CLOB ) |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_WORKLOAD_REPLAY.COMPARE_SQLSET_REPORT ( replay_id1 IN NUMBER, replay_id2 IN NUMBER, format IN VARCHAR2, r_level IN VARCHAR2 DEFAULT 'ALL', r_sections IN VARCHAR2 DEFAULT 'ALL', result OUT CLOB ) RETURN VARCHAR2; Parameters Table 191-10 COMPARE_SQLSET_REPORT Function Parameters Parameter Description replay_id1 First ID of the workload replay after a change replay_id2 Second ID of the workload replay before a change. If this is NULL , then the comparison is done with the capture. format Specifies the report format. Valid values are DBMS_WORKLOAD_CAPTURE . TYPE_HTML , DBMS_WORKLOAD_CAPTURE . TYPE_XML and DBMS_WORKLOAD_CAPTURE.TYPE_TEXT . r_level See level parameter in the REPORT_ANALYSIS_TASK Function in the DBMS_SQLPA package r_sections See section parameter in the REPORT_ANALYSIS_TASK Function in the DBMS_SQLPA package result Output of the report ( CLOB )