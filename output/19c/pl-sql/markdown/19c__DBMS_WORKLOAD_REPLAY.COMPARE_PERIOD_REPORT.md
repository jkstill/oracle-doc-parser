---
id: 19c__DBMS_WORKLOAD_REPLAY.COMPARE_PERIOD_REPORT
name: DBMS_WORKLOAD_REPLAY.COMPARE_PERIOD_REPORT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.COMPARE_PERIOD_REPORT

This procedure generates a report comparing a replay to its capture or to another replay of the same capture.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.COMPARE_PERIOD_REPORT (
   replay_id1   IN   NUMBER,
   replay_id2   IN   NUMBER,
   format       IN   VARCHAR2,
   result       OUT  CLOB );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| replay_id1 | NUMBER | IN | First ID of the workload replay whose report is requested |
| replay_id2 | NUMBER | IN | Second ID of the workload replay whose report is requested. If this is NULL , then the comparison is done with the capture. |
| format | VARCHAR2 | IN | Specifies the report format. Valid values are DBMS_WORKLOAD_CAPTURE . TYPE_HTML and DBMS_WORKLOAD_CAPTURE . TYPE_XML . |
| result | CLOB | OUT | Output of the report ( CLOB ) |

## Usage Notes

Syntax DBMS_WORKLOAD_REPLAY.COMPARE_PERIOD_REPORT ( replay_id1 IN NUMBER, replay_id2 IN NUMBER, format IN VARCHAR2, result OUT CLOB ); Parameters Table 191-9 COMPARE_PERIOD_REPORT Procedure Parameters Parameter Description replay_id1 First ID of the workload replay whose report is requested replay_id2 Second ID of the workload replay whose report is requested. If this is NULL , then the comparison is done with the capture. format Specifies the report format. Valid values are DBMS_WORKLOAD_CAPTURE . TYPE_HTML and DBMS_WORKLOAD_CAPTURE . TYPE_XML . result Output of the report ( CLOB )