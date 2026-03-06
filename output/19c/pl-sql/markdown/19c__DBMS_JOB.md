---
id: 19c__DBMS_JOB
name: DBMS_JOB
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_JOB
tags: [dbms_job]
source_file: DBMS_JOB.html
---

# DBMS_JOB

These notes describe stopping a job, and working with Oracle Real Application Clusters.

## Syntax

```sql
DBMS_JOB.SUBMIT( 
   job       OUT    BINARY_INTEGER,
   what      IN     VARCHAR2, 
   next_date IN     DATE DEFAULT SYSDATE, 
   interval  IN     VARCHAR2 DEFAULT 'NULL',
   no_parse  IN     BOOLEAN DEFAULT FALSE,
   instance  IN     BINARY_INTEGER DEFAULT ANY_INSTANCE,
   force     IN     BOOLEAN DEFAULT FALSE);
```

## Usage Notes

Stopping a Job Note that, once a job is started and running, there is no easy way to stop the job. Working with Oracle Real Application Clusters DBMS_JOB supports multi-instance execution of jobs. By default jobs can be executed on any instance, but only one single instance will execute the job. In addition, you can force instance binding by binding the job to a particular instance. You implement instance binding by specifying an instance number to the instance affinity parameter. Note, however, that in Oracle Database 10g Release 1 (10.1) instance binding is not recommended. Service affinity is preferred. This concept is implemented in the DBMS_SCHEDULER package. The following procedures can be used to create, alter or run jobs with instance affinity. Note that not specifying affinity means any instance can run the job. DBMS_JOB.SUBMIT DBMS_JOB.INSTANCE DBMS_JOB.CHANGE DBMS_JOB.RUN DBMS_JOB.SUBMIT To submit a job to the job queue, use the following syntax: DBMS_JOB.SUBMIT( job OUT BINARY_INTEGER, what IN VARCHAR2, next_date IN DATE DEFAULT SYSDATE, interval IN VARCHAR2 DEFAULT 'NULL', no_parse IN BOOLEAN DEFAULT FALSE, instance IN BINARY_INTEGER DEFAULT ANY_INSTANCE, force IN BOOLEAN DEFAULT FALSE); Use the parameters instance and force to control job and instance affinity. The default value of instance is 0 (zero) to indicate that any instance can execute the job. To run the job on a certain instance, specify the instance value. Oracle displays error ORA-23319 if the instance value is a negative number or NULL. The force parameter defaults to false. If force is TRUE, any positive integer is acceptable as the job instance. If force is FALSE, the specified instance must be running, or Oracle displays error number ORA-23428. DBMS_JOB.INSTANCE To assign a particular instance to execute a job, use the following syntax: DBMS_JOB.INSTANCE( JOB IN BINARY_INTEGER, instance IN BINARY_INTEGER, force IN BOOLEAN DEFAULT FALSE); The FORCE parameter in this example defaults to FALSE. If the instance value is 0 (zero), job affinity is altered and any available instance can execute the job despite the value of force. If the INSTANCE value is positive and the FORCE parameter is FALSE, job affinity is altered only if the specified instance is running, or Oracle displays error ORA-23428. If the force parameter is TRUE , any positive integer is acceptable as the job instance and the job affinity is altered. Oracle displays error ORA-23319 if the instance value is negative or NULL . DBMS_JOB.CHANGE To alter user-definable parameters associated with a job, use the following syntax: DBMS_JOB.CHANGE( JOB IN BINARY_INTEGER, what IN VARCHAR2 DEFAULT NULL, next_date IN DATE DEFAULT NULL, interval IN VARCHAR2 DEFAULT NULL, instance IN BINARY_INTEGER DEFAULT NULL, force IN BOOLEAN DEFAULT FALSE ); Two parameters, instance and force, appear in this example. The default value of instance is null indicating that job affinity will not change. The default value of force is FALSE. Oracle displays error ORA-23428 if the specified instance is not running and error ORA-23319 if the instance number is negative.