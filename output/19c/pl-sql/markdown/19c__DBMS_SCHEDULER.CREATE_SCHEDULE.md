---
id: 19c__DBMS_SCHEDULER.CREATE_SCHEDULE
name: DBMS_SCHEDULER.CREATE_SCHEDULE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.CREATE_SCHEDULE

This procedure creates a schedule.

## Syntax

```sql
DBMS_SCHEDULER.CREATE_SCHEDULE (
   schedule_name          IN VARCHAR2,
   start_date             IN TIMESTAMP WITH TIMEZONE DEFAULT NULL,
   repeat_interval        IN VARCHAR2,
   end_date               IN TIMESTAMP WITH TIMEZONE DEFAULT NULL,
   comments               IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schedule_name | VARCHAR2 | IN | The name to assign to the schedule. The name must be unique in the SQL namespace. For example, a schedule cannot have the same name as a table in a schema. If no name is specified, then an error occurs. |
| start_date | TIMESTAMP | IN | This attribute specifies the first date and time on which this schedule becomes valid. For a repeating schedule, the value for start_date is a reference date. In this case, the start of the schedule is not the start_date ; it depends on the repeat interval specified. start_date is used to determine the first instance of the schedule. If start_date is specified in the past and no value for repeat_interval is specified, the schedule is invalid. For a repeating job or window, start_date can be derived from the repeat_interval if it is not specified. If start_date is null, then the date that the job or window is enabled is used. start_date and repeat_interval cannot both be null. |
| repeat_interval | VARCHAR2 | IN | This attribute specifies how often the schedule repeats. It is expressed using calendaring syntax. See " Calendaring Syntax " for further information. PL/SQL expressions are not allowed as repeat intervals for named schedules. |
| end_date | TIMESTAMP | IN | The date and time after which jobs will not run and windows will not open. A non-repeating schedule that has no end_date is valid forever. end_date has to be after the start_date . If this is not the case, then an error is generated when the schedule is created. |
| comments | VARCHAR2 | IN | This attribute specifies an optional comment about the schedule. By default, this attribute is NULL . |

## Usage Notes

Syntax DBMS_SCHEDULER.CREATE_SCHEDULE ( schedule_name IN VARCHAR2, start_date IN TIMESTAMP WITH TIMEZONE DEFAULT NULL, repeat_interval IN VARCHAR2, end_date IN TIMESTAMP WITH TIMEZONE DEFAULT NULL, comments IN VARCHAR2 DEFAULT NULL); Parameters Table 151-33 CREATE_SCHEDULE Procedure Parameters Parameter Description schedule_name The name to assign to the schedule. The name must be unique in the SQL namespace. For example, a schedule cannot have the same name as a table in a schema. If no name is specified, then an error occurs. start_date This attribute specifies the first date and time on which this schedule becomes valid. For a repeating schedule, the value for start_date is a reference date. In this case, the start of the schedule is not the start_date ; it depends on the repeat interval specified. start_date is used to determine the first instance of the schedule. If start_date is specified in the past and no value for repeat_interval is specified, the schedule is invalid. For a repeating job or window, start_date can be derived from the repeat_interval if it is not specified. If start_date is null, then the date that the job or window is enabled is used. start_date and repeat_interval cannot both be null. repeat_interval This attribute specifies how often the schedule repeats. It is expressed using calendaring syntax. See " Calendaring Syntax " for further information. PL/SQL expressions are not allowed as repeat intervals for named schedules. end_date The date and time after which jobs will not run and windows will not open. A non-repeating schedule that has no end_date is valid forever. end_date has to be after the start_date . If this is not the case, then an error is generated when the schedule is created. comments This attribute specifies an optional comment about the schedule. By default, this attribute is NULL . Usage Notes This procedure requires the CREATE JOB privilege to create a schedule in your own schema or the CREATE ANY JOB privilege to create a schedule in someone else's schema by specifying schema.schedule_name . Once a schedule has been created, it can be used by other users. The schedule is created with access to PUBLIC . Therefore, there is no need to explicitly grant access to the schedule.