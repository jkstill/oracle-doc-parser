---
id: 19c__DBMS_WORKLOAD_REPLAY.REMOVE_SCHEDULE_ORDERING
name: DBMS_WORKLOAD_REPLAY.REMOVE_SCHEDULE_ORDERING
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.REMOVE_SCHEDULE_ORDERING

This procedure removes an existing schedule order from the current replay schedule.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.REMOVE_SCHEDULE_ORDERING (
   schedule_capture_id     IN         NUMBER,
   waitfor_capture_id      IN         NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schedule_capture_id | NUMBER | IN | Points to a capture that has been added to the current replay schedule (see procedure description). |
| waitfor_capture_id | NUMBER) | IN | Points to a capture that has been added to the current replay schedule. |

## Usage Notes

Together, schedule_capture_id and waitfor_capture_id form a schedule ordering that previously added by the ADD_SCHEDULE_ORDERING Function ( schedule_capture_id , waitfor_capture_id ). The order is that replay of capture indicated by schedule_capture_id will not start unless the replay of capture indicated by waiting_for_capture_id finishes. Syntax DBMS_WORKLOAD_REPLAY.REMOVE_SCHEDULE_ORDERING ( schedule_capture_id IN NUMBER, waitfor_capture_id IN NUMBER); Parameters Table 191-29 REMOVE_SCHEDULE_ORDERING Procedure Parameters Parameter Description schedule_capture_id Points to a capture that has been added to the current replay schedule (see procedure description). waitfor_capture_id Points to a capture that has been added to the current replay schedule. Usage Notes Prerequisites: The BEGIN_REPLAY_SCHEDULE Procedure must have been called. The replay schedule order should have already been added using the ADD_SCHEDULE_ORDERING Function .