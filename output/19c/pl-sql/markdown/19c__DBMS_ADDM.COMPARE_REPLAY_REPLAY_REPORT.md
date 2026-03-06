---
id: 19c__DBMS_ADDM.COMPARE_REPLAY_REPLAY_REPORT
name: DBMS_ADDM.COMPARE_REPLAY_REPLAY_REPORT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADDM
tags: [dbms_addm]
source_file: DBMS_ADDM.html
---

# DBMS_ADDM.COMPARE_REPLAY_REPLAY_REPORT

This function produces a Compare Period ADDM report comparing the performance of a replay to another replay.

## Syntax

```sql
DBMS_ADDM.COMPARE_CAPTURE_REPLAY_REPORT (
   replay_id1            IN NUMBER,
   replay_id2            IN NUMBER,
   report_type           IN VARCHAR2 := 'HTML')
  RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| replay_id1 | NUMBER | IN | Replay ID to use as the base period. The base period is the baseline period to compare in order to determine improvement or regression. |
| replay_id2 | NUMBER | IN | Replay ID to use as the comparison period. The comparison period is the period to compare to the base period in order to determine improvement or regression. |
| report_type | VARCHAR2 | IN | 'HTML' (the default) for an HTML active report, 'XML' for an XML report |

**Returns:** `CLOB`

## Usage Notes

The AWR data must reside in the same database, but it can originate from different databases. The function generates a report in either XML or HTML(Active Report) format. Syntax DBMS_ADDM.COMPARE_CAPTURE_REPLAY_REPORT ( replay_id1 IN NUMBER, replay_id2 IN NUMBER, report_type IN VARCHAR2 := 'HTML') RETURN CLOB; Parameters Table 14-8 COMPARE_REPLAY_REPLAY_REPORT Function Parameters Parameter Description replay_id1 Replay ID to use as the base period. The base period is the baseline period to compare in order to determine improvement or regression. replay_id2 Replay ID to use as the comparison period. The comparison period is the period to compare to the base period in order to determine improvement or regression. report_type 'HTML' (the default) for an HTML active report, 'XML' for an XML report Return Values A CLOB containing a compare period ADDM report