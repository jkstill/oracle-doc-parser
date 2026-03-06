---
id: 19c__DBMS_SCHEDULER.ENABLE
name: DBMS_SCHEDULER.ENABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.ENABLE

This procedure enables a program, job, chain, window, database destination, external destination, file watcher, or group.

## Syntax

```sql
DBMS_SCHEDULER.ENABLE (
   name              IN VARCHAR2,
   commit_semantics  IN VARCHAR2 DEFAULT 'STOP_ON_FIRST_ERROR');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | The name of the Scheduler object being enabled. Can be a comma-delimited list of names. If a job class name is specified, then all the jobs in the job class are enabled. If a group name is specified, then the group is enabled, but the enabled state of the group members is unaffected. |
| commit_semantics | VARCHAR2 | IN | The commit semantics. The following types are supported: STOP_ON_FIRST_ERROR - The procedure returns on the first error and previous successful enable operations are committed to disk. This is the default. TRANSACTIONAL - The procedure returns on the first error and everything that happened before that error is rolled back. This type is only supported when enabling a job or a list of jobs. ABSORB_ERRORS - The procedure tries to absorb any errors and enable the rest of the jobs. It commits all the enable operations that were successful. If errors occur, you can query the view SCHEDULER_BATCH_ERRORS for details. This type is only supported when enabling a job or a list of jobs. |

## Usage Notes

When an object is enabled, its enabled attribute is set to TRUE . By default, jobs, chains, and programs are created disabled and database destinations, external destinations, file watchers, windows, and groups are created enabled. If a job was disabled and you enable it, the Scheduler begins to automatically run the job according to its schedule. Enabling a disabled job also resets the job RUN_COUNT , FAILURE_COUNT and RETRY_COUNT columns in the *_SCHEDULER_JOBS data dictionary views. Validity checks are performed before enabling an object. If the check fails, the object is not enabled, and an appropriate error is returned. This procedure does not return an error if the object was already enabled. Syntax DBMS_SCHEDULER.ENABLE ( name IN VARCHAR2, commit_semantics IN VARCHAR2 DEFAULT 'STOP_ON_FIRST_ERROR'); Parameters Table 151-59 ENABLE Procedure Parameters Parameter Description name The name of the Scheduler object being enabled. Can be a comma-delimited list of names. If a job class name is specified, then all the jobs in the job class are enabled. If a group name is specified, then the group is enabled, but the enabled state of the group members is unaffected. commit_semantics The commit semantics. The following types are supported: STOP_ON_FIRST_ERROR - The procedure returns on the first error and previous successful enable operations are committed to disk. This is the default. TRANSACTIONAL - The procedure returns on the first error and everything that happened before that error is rolled back. This type is only supported when enabling a job or a list of jobs. ABSORB_ERRORS - The procedure tries to absorb any errors and enable the rest of the jobs. It commits all the enable operations that were successful. If errors occur, you can query the view SCHEDULER_BATCH_ERRORS for details. This type is only supported when enabling a job or a list of jobs. Usage Notes Window names must be preceded by SYS . To run ENABLE for a window or group of type WINDOW , you must have the MANAGE SCHEDULER privilege. For a job of type EXECUTABLE (or for a job that points to a program of type EXECUTABLE ), the job owner must have the CREATE EXTERNAL JOB system privilege before the job can be enabled or run. To enable a file watcher, the file watcher owner must have the EXECUTE privilege on the designated credential. You can use ENABLE with any schema except the SYS schema.