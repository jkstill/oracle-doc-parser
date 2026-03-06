---
id: 19c__DBMS_WORKLOAD_REPLAY.ADD_SCHEDULE_ORDERING
name: DBMS_WORKLOAD_REPLAY.ADD_SCHEDULE_ORDERING
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.ADD_SCHEDULE_ORDERING

This function adds a schedule order between two captures.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.ADD_SCHEDULE_ORDERING (
   schedule_capture_id     IN VARCHAR2,
   waitfor_capture_id      IN VARCHAR2)
  RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schedule_capture_id | VARCHAR2 | IN | Points to a capture that has been added to the current replay schedule. According to the new schedule ordering added by this subprogram, its replay will not start until the replay of another capture specified by waitfor_capture_id runs to completion. |
| waitfor_capture_id | VARCHAR2) | IN | Points to a capture that has been added to the current replay schedule. According to the new schedule ordering added by this subprogram, the replay of capture specified by schedule_capture_id will not start until the replay of this capture runs to completion. |

**Returns:** `NUMBER`

## Usage Notes

Together, schedule_capture_id and waitfor_capture_id form a schedule ordering that previously added by the ADD_SCHEDULE_ORDERING Function . The order is that replay of capture indicated by schedule_capture_id will not start unless the replay of capture indicated by waiting_for_capture_id finishes. Syntax DBMS_WORKLOAD_REPLAY.ADD_SCHEDULE_ORDERING ( schedule_capture_id IN VARCHAR2, waitfor_capture_id IN VARCHAR2) RETURN NUMBER; Parameters Table 191-4 ADD_SCHEDULE_ORDERING Function Parameters Parameter Description schedule_capture_id Points to a capture that has been added to the current replay schedule. According to the new schedule ordering added by this subprogram, its replay will not start until the replay of another capture specified by waitfor_capture_id runs to completion. waitfor_capture_id Points to a capture that has been added to the current replay schedule. According to the new schedule ordering added by this subprogram, the replay of capture specified by schedule_capture_id will not start until the replay of this capture runs to completion. Return Values Returns a non-zero error code if the constraint cannot be added Usage Notes The two captures must have already been added to the replay schedule.