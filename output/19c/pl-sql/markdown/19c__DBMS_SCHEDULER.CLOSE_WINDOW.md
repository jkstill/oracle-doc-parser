---
id: 19c__DBMS_SCHEDULER.CLOSE_WINDOW
name: DBMS_SCHEDULER.CLOSE_WINDOW
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.CLOSE_WINDOW

This procedure closes an open window prematurely. A closed window means that it is no longer in effect. When a window is closed, the Scheduler switches the resource plan to the one that is in effect outside the window, or in the case of overlapping windows, to another window.

## Syntax

```sql
DBMS_SCHEDULER.CLOSE_WINDOW (
   window_name             IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| window_name | VARCHAR2) | IN | The name of the window |

## Usage Notes

Syntax DBMS_SCHEDULER.CLOSE_WINDOW ( window_name IN VARCHAR2); Parameters Table 151-19 CLOSE_WINDOW Procedure Parameters Parameter Description window_name The name of the window Usage Notes If you try to close a window that does not exist or is not open, an error is generated. A job that is running does not stop when the window it is running in closes, unless the attribute stop_on_window_close is set to TRUE for the job. However, the resources allocated to the job can change if the resource plan changes. When a running job has a group of type WINDOW as its schedule, the job is not stopped when its window is closed if another window in the same window group becomes active. This is the case even if the job has the attribute stop_on_window_close set to TRUE . Closing a window requires the MANAGE SCHEDULER privilege.