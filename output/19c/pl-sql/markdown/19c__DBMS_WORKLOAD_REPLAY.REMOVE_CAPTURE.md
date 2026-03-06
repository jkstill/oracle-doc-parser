---
id: 19c__DBMS_WORKLOAD_REPLAY.REMOVE_CAPTURE
name: DBMS_WORKLOAD_REPLAY.REMOVE_CAPTURE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.REMOVE_CAPTURE

This procedure removes the given capture from the current schedule.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.REMOVE_CAPTURE (
   schedule_capture_number    IN     NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schedule_capture_number | NUMBER) | IN | Unique ID that identifies this capture within this schedule |

## Usage Notes

Syntax DBMS_WORKLOAD_REPLAY.REMOVE_CAPTURE ( schedule_capture_number IN NUMBER); Parameters Table 191-28 REMOVE_CAPTURE Procedure Parameters Parameter Description schedule_capture_number Unique ID that identifies this capture within this schedule