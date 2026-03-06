---
id: 19c__DBMS_SCHEDULER.OPEN_WINDOW
name: DBMS_SCHEDULER.OPEN_WINDOW
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.OPEN_WINDOW

This procedure manually opens a window, unrelated to its schedule.

## Syntax

```sql
DBMS_SCHEDULER.OPEN_WINDOW (
   window_name             IN VARCHAR2,
   duration                IN INTERVAL DAY TO SECOND,
   force                   IN BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| window_name | VARCHAR2 | IN | The name of the window |
| duration | INTERVAL | IN | The duration of the window. It is of type interval day to second. If it is NULL , then the window opens for the regular duration as specified in the window metadata. |
| force | BOOLEAN | IN | If force is set to FALSE , then opening an already open window generates an error. If force is set to TRUE : You can open a window that is already open. The window stays open for the duration specified in the call, from the time the OPEN_WINDOW command was issued. For example: window1 was created with a duration of four hours. It has how been open for two hours. If, at this point, you reopen window1 using the OPEN_WINDOW call and do not specify a duration, then window1 stays open for four hours because it was created with that duration. If you specified a duration of 30 minutes, the window will close in 30 minutes. The Scheduler automatically closes any window that is open at that time, even if it has a higher priority. For the duration of this manually opened window, the Scheduler does not open any other scheduled windows even if they have a higher priority. |

## Usage Notes

The window opens and the resource plan associated with it takes effect immediately, for the duration specified or for the normal duration of the window, if no duration is given. Only an enabled window can be manually opened. Syntax DBMS_SCHEDULER.OPEN_WINDOW ( window_name IN VARCHAR2, duration IN INTERVAL DAY TO SECOND, force IN BOOLEAN DEFAULT FALSE); Parameters Table 151-70 OPEN_WINDOW Procedure Parameters Parameter Description window_name The name of the window duration The duration of the window. It is of type interval day to second. If it is NULL , then the window opens for the regular duration as specified in the window metadata. force If force is set to FALSE , then opening an already open window generates an error. If force is set to TRUE : You can open a window that is already open. The window stays open for the duration specified in the call, from the time the OPEN_WINDOW command was issued. For example: window1 was created with a duration of four hours. It has how been open for two hours. If, at this point, you reopen window1 using the OPEN_WINDOW call and do not specify a duration, then window1 stays open for four hours because it was created with that duration. If you specified a duration of 30 minutes, the window will close in 30 minutes. The Scheduler automatically closes any window that is open at that time, even if it has a higher priority. For the duration of this manually opened window, the Scheduler does not open any other scheduled windows even if they have a higher priority. Usage Notes Opening a window manually has no impact on regular scheduled runs of the window. The next open time of the window is not updated and is determined by the regular scheduled opening. When a window that was manually opened closes, the rules about overlapping windows are applied to determine which other window should be opened at that time if any at all. If there are jobs running when the window opens, the resources allocated to them might change if there is a switch in resource plan. If a window fails to switch resource plans because the designated resource plan no longer exists or because resource plan switching by windows is disabled (for example, by using the ALTER SYSTEM statement with the force option), the failure to switch resource plans is recorded in the window log. Opening a window requires the MANAGE SCHEDULER privilege.