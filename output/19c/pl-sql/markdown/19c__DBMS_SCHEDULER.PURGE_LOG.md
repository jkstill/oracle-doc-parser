---
id: 19c__DBMS_SCHEDULER.PURGE_LOG
name: DBMS_SCHEDULER.PURGE_LOG
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.PURGE_LOG

The PURGE_LOG procedure purges rows from the job and window log that were not purged automatically by the scheduler.

## Syntax

```sql
DBMS_SCHEDULER.PURGE_LOG (
   log_history             IN PLS_INTEGER  DEFAULT 0,
   which_log               IN VARCHAR2     DEFAULT 'JOB_AND_WINDOW_LOG',
   job_name                IN VARCHAR2     DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| log_history | PLS_INTEGER | IN | This specifies how much history (in days) to keep. The valid range is 0 - 1000000. If set to 0, no history is kept. |
| which_log | VARCHAR2 | IN | This specifies the log type. Valid values are: job_log , window_log , and job_and_window_log . |
| job_name | VARCHAR2 | IN | This specifies which job-specific entries must be purged from the jog log. This can be a comma-delimited list of job names and job classes. Whenever job_name has a value other than NULL , the which_log argument implicitly includes the job log. |

## Usage Notes

By default, the Scheduler automatically purges all rows in the job log and window log that are older than 30 days. The PURGE_LOG procedure can be used to purge additional rows from the job and window log. Rows in the job log table pertaining to the steps of a chain are purged only when the entry for the main chain job is purged (either manually or automatically). Syntax DBMS_SCHEDULER.PURGE_LOG ( log_history IN PLS_INTEGER DEFAULT 0, which_log IN VARCHAR2 DEFAULT 'JOB_AND_WINDOW_LOG', job_name IN VARCHAR2 DEFAULT NULL); Parameters Table 151-71 PURGE_LOG Procedure Parameters Parameter Description log_history This specifies how much history (in days) to keep. The valid range is 0 - 1000000. If set to 0, no history is kept. which_log This specifies the log type. Valid values are: job_log , window_log , and job_and_window_log . job_name This specifies which job-specific entries must be purged from the jog log. This can be a comma-delimited list of job names and job classes. Whenever job_name has a value other than NULL , the which_log argument implicitly includes the job log. Usage Notes This procedure requires the MANAGE SCHEDULER privilege. Examples The following completely purges all rows from both the job log and the window log: DBMS_SCHEDULER.PURGE_LOG(); The following purges all rows from the window log that are older than 5 days: DBMS_SCHEDULER.PURGE_LOG(5, 'window_log'); The following purges all rows from the window log that are older than 1 day and all rows from the job log that are related to jobs in jobclass1 and older than 1 day: DBMS_SCHEDULER.PURGE_LOG(1, 'job_and_window_log', 'sys.jobclass1');