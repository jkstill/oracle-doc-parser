---
id: 19c__DBMS_SCHEDULER.STOP_JOB
name: DBMS_SCHEDULER.STOP_JOB
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.STOP_JOB

This procedure stops currently running jobs or all jobs in a job class.

## Syntax

```sql
DBMS_SCHEDULER.STOP_JOB (
   job_name         IN VARCHAR2
   force            IN BOOLEAN DEFAULT FALSE
   commit_semantics IN VARCHAR2 DEFAULT 'STOP_ON_FIRST_ERROR');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| job_name | VARCHAR2 | IN | Name of a job to stop. Can be a comma-separate list of jobs, where each entry can be one of the following: Job name: the name of an existing job, optionally preceded by a schema name and dot separator. Job destination ID: a number, obtained from the JOB_DEST_ID column of the *_SCHEDULER_JOB_DESTS views, that represents the unique combination of a job, a credential, and a destination. Job class: the name of a job class. Must be preceded by the SYS schema name and a dot separator. If you specify a job class, all jobs that belong to that job class are stopped. If you specify a job that was created with a destination group as its destination_name attribute, all job instances on all destinations are stopped. |
| force | BOOLEAN | IN | If force is set to FALSE , the Scheduler tries to gracefully stop the job using an interrupt mechanism. This method gives control back to the slave process, which can update the status of the job in the job queue to stopped. If this fails, an error is returned. If force is set to TRUE , the Scheduler immediately terminates the job slave. Oracle recommends that STOP_JOB with force set to TRUE be used only after a STOP_JOB with force set to FALSE has failed. Use of the force option requires the MANAGE SCHEDULER system privilege. |
| commit_semantics | VARCHAR2 | IN | The commit semantics. The following two types are supported: STOP_ON_FIRST_ERROR : The procedure returns on the first error and commits previous successful stop operations to disk. This is the default. ABSORB_ERRORS : The procedure tries to absorb any errors, stops the rest of the jobs, and commits all the successful stop operations. This type is available only if no job classes are specified in the job_name list. If errors occur, you can query the view SCHEDULER_BATCH_ERRORS for details. |

## Usage Notes

After stopping the job, the state of a one-time job is set to STOPPED , whereas the state of a repeating job is set to SCHEDULED or COMPLETED , depending on whether the next run of the job is scheduled. If a job pointing to a chain is stopped, all running steps of the running chain are stopped. If a job has multiple destinations, the database attempts to stop the job at all destinations. For external jobs, STOP_JOB stops only the external process that was directly started by the job action. It does not stop child processes of external jobs. For in-memory full jobs in an Oracle Real Application Clusters environment, STOP_JOB uses the instance_id attribute of the job definition to determine in which instance (or all of them if the attribute is left null) to stop the in-memory full job. (In-memory full jobs are kept cached in memory, and as such are limited to the instance currently caching them. Because of this, the same job_name can in some conditions be used for different jobs on different instances.) Syntax DBMS_SCHEDULER.STOP_JOB ( job_name IN VARCHAR2 force IN BOOLEAN DEFAULT FALSE commit_semantics IN VARCHAR2 DEFAULT 'STOP_ON_FIRST_ERROR'); Parameters Table 151-102 STOP_JOB Procedure Parameters Parameter Description job_name Name of a job to stop. Can be a comma-separate list of jobs, where each entry can be one of the following: Job name: the name of an existing job, optionally preceded by a schema name and dot separator. Job destination ID: a number, obtained from the JOB_DEST_ID column of the *_SCHEDULER_JOB_DESTS views, that represents the unique combination of a job, a credential, and a destination. Job class: the name of a job class. Must be preceded by the SYS schema name and a dot separator. If you specify a job class, all jobs that belong to that job class are stopped. If you specify a job that was created with a destination group as its destination_name attribute, all job instances on all destinations are stopped. force If force is set to FALSE , the Scheduler tries to gracefully stop the job using an interrupt mechanism. This method gives control back to the slave process, which can update the status of the job in the job queue to stopped. If this fails, an error is returned. If force is set to TRUE , the Scheduler immediately terminates the job slave. Oracle recommends that STOP_JOB with force set to TRUE be used only after a STOP_JOB with force set to FALSE has failed. Use of the force option requires the MANAGE SCHEDULER system privilege. commit_semantics The commit semantics. The following two types are supported: STOP_ON_FIRST_ERROR : The procedure returns on the first error and commits previous successful stop operations to disk. This is the default. ABSORB_ERRORS : The procedure tries to absorb any errors, stops the rest of the jobs, and commits all the successful stop operations. This type is available only if no job classes are specified in the job_name list. If errors occur, you can query the view SCHEDULER_BATCH_ERRORS for details. Usage Notes STOP_JOB without the force option requires that you be the owner of the job or have ALTER privileges on that job. You can also stop a job if you have the CREATE ANY JOB or MANAGE SCHEDULER privilege. STOP_JOB with the force option requires that you have the MANAGE SCHEDULER privilege. Example The following is an example of using STOP_JOB . BEGIN DBMS_SCHEDULER.STOP_JOB('DSS.ETLJOB, 984, 1223, SYS.ETL_JOBCLASS'); END;