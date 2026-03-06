---
id: 19c__DBMS_SCHEDULER.EVALUATE_CALENDAR_STRING
name: DBMS_SCHEDULER.EVALUATE_CALENDAR_STRING
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.EVALUATE_CALENDAR_STRING

You can define repeat intervals of jobs, windows or schedules using the Scheduler calendaring syntax. This procedure evaluates the calendar expression and tells you the next execution date and time of a job or window. This is very useful for testing the correct definition of the calendar string without actually scheduling the job or window.

## Syntax

```sql
DBMS_SCHEDULER.EVALUATE_CALENDAR_STRING (
   calendar_string    IN  VARCHAR2,
   start_date         IN  TIMESTAMP WITH TIME ZONE,
   return_date_after  IN  TIMESTAMP WITH TIME ZONE,
   next_run_date      OUT TIMESTAMP WITH TIME ZONE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| calendar_string | VARCHAR2 | IN | The calendar expression to be evaluated. The string must be in the calendaring syntax described in " Operational Notes " . |
| start_date | TIMESTAMP | IN | The date and time after which the repeat interval becomes valid. It can also be used to fill in specific items that are missing from the calendar string. Can optionally be NULL . |
| return_date_after | TIMESTAMP | IN | The return_date_after argument helps the Scheduler determine which one of all possible matches (all valid execution dates) to return from those determined by the start_date and the calendar string. When a NULL value is passed for this argument, the Scheduler automatically fills in systimestamp as its value. |
| next_run_date | TIMESTAMP | OUT | The first timestamp that matches the calendar string and start date that occur after the value passed in for the return_date_after argument. |

## Usage Notes

This procedure can also get multiple steps of the repeat interval by passing the next_run_date returned by one invocation as the return_date_after argument of the next invocation. See the calendaring syntax described in " Operational Notes " . Syntax DBMS_SCHEDULER.EVALUATE_CALENDAR_STRING ( calendar_string IN VARCHAR2, start_date IN TIMESTAMP WITH TIME ZONE, return_date_after IN TIMESTAMP WITH TIME ZONE, next_run_date OUT TIMESTAMP WITH TIME ZONE); Parameters Table 151-61 EVALUATE_CALENDAR_STRING Procedure Parameters Parameter Description calendar_string The calendar expression to be evaluated. The string must be in the calendaring syntax described in " Operational Notes " . start_date The date and time after which the repeat interval becomes valid. It can also be used to fill in specific items that are missing from the calendar string. Can optionally be NULL . return_date_after The return_date_after argument helps the Scheduler determine which one of all possible matches (all valid execution dates) to return from those determined by the start_date and the calendar string. When a NULL value is passed for this argument, the Scheduler automatically fills in systimestamp as its value. next_run_date The first timestamp that matches the calendar string and start date that occur after the value passed in for the return_date_after argument. Examples The following code fragment can be used to determine the next five dates a job will run given a specific calendar string. SET SERVEROUTPUT ON; ALTER SESSION set NLS_DATE_FORMAT = 'DD-MON-YYYY HH24:MI:SS'; Session altered. DECLARE start_date TIMESTAMP; return_date_after TIMESTAMP; next_run_date TIMESTAMP; BEGIN start_date := to_timestamp_tz('01-JAN-2003 10:00:00','DD-MON-YYYY HH24:MI:SS'); return_date_after := start_date; FOR i IN 1..5 LOOP DBMS_SCHEDULER.EVALUATE_CALENDAR_STRING ( 'FREQ=DAILY;BYHOUR=9;BYMINUTE=30;BYDAY=MON,TUE,WED,THU,FRI', start_date, return_date_after, next_run_date); DBMS_OUTPUT.PUT_LINE('next_run_date: ' || next_run_date); return_date_after := next_run_date; END LOOP; END; / next_run_date: 02-JAN-03 09.30.00.000000 AM next_run_date: 03-JAN-03 09.30.00.000000 AM next_run_date: 06-JAN-03 09.30.00.000000 AM next_run_date: 07-JAN-03 09.30.00.000000 AM next_run_date: 08-JAN-03 09.30.00.000000 AM PL/SQL procedure successfully completed. Usage Notes No specific Scheduler privileges are required.