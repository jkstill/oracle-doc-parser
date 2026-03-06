---
id: 19c__DBMS_SCHEDULER.DROP_SCHEDULE
name: DBMS_SCHEDULER.DROP_SCHEDULE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.DROP_SCHEDULE

This procedure drops a schedule.

## Syntax

```sql
DBMS_SCHEDULER.DROP_SCHEDULE (
   schedule_name    IN VARCHAR2,
   force            IN BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schedule_name | VARCHAR2 | IN | The name of the schedule. Can be a comma-delimited list. |
| force | BOOLEAN | IN | If force is set to FALSE , the schedule must not be referenced by any job or window, otherwise an error will occur. If force is set to TRUE , any jobs or windows that use this schedule are disabled before the schedule is dropped Running jobs and open windows that point to the schedule are not affected. |

## Usage Notes

Syntax DBMS_SCHEDULER.DROP_SCHEDULE ( schedule_name IN VARCHAR2, force IN BOOLEAN DEFAULT FALSE); Parameters Table 151-57 DROP_SCHEDULE Procedure Parameters Parameter Description schedule_name The name of the schedule. Can be a comma-delimited list. force If force is set to FALSE , the schedule must not be referenced by any job or window, otherwise an error will occur. If force is set to TRUE , any jobs or windows that use this schedule are disabled before the schedule is dropped Running jobs and open windows that point to the schedule are not affected. Usage Notes You must be the owner of the schedule being dropped or have ALTER privileges for the schedule or the CREATE ANY JOB privilege.