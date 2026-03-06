---
id: 19c__DBMS_SCHEDULER.DROP_WINDOW
name: DBMS_SCHEDULER.DROP_WINDOW
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.DROP_WINDOW

This procedure drops a window. All metadata about the window is removed from the database. The window is removed from any groups that reference it.

## Syntax

```sql
DBMS_SCHEDULER.DROP_WINDOW (
   window_name             IN VARCHAR2,
   force                   IN BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| window_name | VARCHAR2 | IN | The name of the window. Can be a comma-delimited list. |
| force | BOOLEAN | IN | If force is set to FALSE , the window must be not be open or referenced by any job, otherwise an error occurs. If force is set to TRUE , the window is dropped and those jobs that have the window as their schedule are disabled. However, jobs that have a window group, of which the dropped window is a member, as their schedule, are not disabled. If the window is open then, the Scheduler attempts to first close the window and then drop it. When the window is closed, normal close window rules apply. Running jobs that have the window as their schedule is allowed to continue, unless the stop_on_window_close flag is set to TRUE for the job. If this is the case, the job is stopped when the window is dropped. |

## Usage Notes

Syntax DBMS_SCHEDULER.DROP_WINDOW ( window_name IN VARCHAR2, force IN BOOLEAN DEFAULT FALSE); Parameters Table 151-58 DROP_WINDOW Procedure Parameters Parameter Description window_name The name of the window. Can be a comma-delimited list. force If force is set to FALSE , the window must be not be open or referenced by any job, otherwise an error occurs. If force is set to TRUE , the window is dropped and those jobs that have the window as their schedule are disabled. However, jobs that have a window group, of which the dropped window is a member, as their schedule, are not disabled. If the window is open then, the Scheduler attempts to first close the window and then drop it. When the window is closed, normal close window rules apply. Running jobs that have the window as their schedule is allowed to continue, unless the stop_on_window_close flag is set to TRUE for the job. If this is the case, the job is stopped when the window is dropped. Usage Notes Dropping a window requires the MANAGE SCHEDULER privilege.