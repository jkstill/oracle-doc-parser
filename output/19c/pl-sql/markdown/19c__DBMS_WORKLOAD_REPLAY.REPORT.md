---
id: 19c__DBMS_WORKLOAD_REPLAY.REPORT
name: DBMS_WORKLOAD_REPLAY.REPORT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.REPORT

This function generates a report on the stipulated workload replay.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.REPORT (
   replay_id          IN NUMBER,
   format             IN VARCHAR2)
  RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| replay_id | NUMBER | IN | (Mandatory) Specifies the ID of the workload replay whose report is requested. |
| format | VARCHAR2) | IN | (Mandatory) Specifies the report format. Valid values: HTML - Generates the HTML version of the report XML - Generates the XML version of the report TEXT - Generates the text version of the report |

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_WORKLOAD_REPLAY.REPORT ( replay_id IN NUMBER, format IN VARCHAR2) RETURN CLOB; Parameters Table 191-30 REPORT Function Parameters Parameter Description replay_id (Mandatory) Specifies the ID of the workload replay whose report is requested. format (Mandatory) Specifies the report format. Valid values: HTML - Generates the HTML version of the report XML - Generates the XML version of the report TEXT - Generates the text version of the report Return Values The report body in the desired format returned as a CLOB