---
id: 19c__DBMS_JOB.SUBMIT
name: DBMS_JOB.SUBMIT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_JOB
tags: [dbms_job]
source_file: DBMS_JOB.html
---

# DBMS_JOB.SUBMIT

This procedure submits a new job. It chooses the job from the sequence sys . jobseq .

## Syntax

```sql
DBMS_JOB.SUBMIT ( 
   job       OUT BINARY_INTEGER,
   what      IN  VARCHAR2,
   next_date IN  DATE DEFAULT SYSDATE,
   interval  IN  VARCHAR2 DEFAULT 'null',
   no_parse  IN  BOOLEAN DEFAULT FALSE,
   instance  IN  BINARY_INTEGER DEFAULT any_instance,
   force     IN  BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| job | BINARY_INTEGER | OUT | System-assigned ID of the job being run. To find this ID, query the JOB column of the USER_JOBS or DBA_JOBS view |
| what | VARCHAR2 | IN | PL/SQL text o the job to be run. This must be a valid PL/SQL statement or block of code. For example, to run a stored procedure P , you could pass the string P ; (with the semi-colon) to this routine. The SQL that you submit in the what parameter is wrapped in the following PL/SQL block: DECLARE job BINARY_INTEGER := :job; next_date DATE := :mydate; broken BOOLEAN := FALSE; BEGIN WHAT :mydate := next_date; IF broken THEN :b := 1; ELSE :b := 0; END IF; END; Ensure that you include the ; semi-colon with the statement. |
| next_date | DATE | IN | Next date when the job will be run. |
| interval | VARCHAR2 | IN | Date function that calculates the next time to run the job. The default is NULL . This must evaluate to a either a future point in time or NULL . |
| no_parse | BOOLEAN | IN | A flag. The default is FALSE . If this is set to FALSE , then Oracle parses the procedure associated with the job. If this is set to TRUE , then Oracle parses the procedure associated with the job the first time that the job is run. For example, if you want to submit a job before you have created the tables associated with the job, then set this to TRUE . |
| instance | BINARY_INTEGER | IN | When a job is submitted, specifies which instance can run the job. |
| force | BOOLEAN | IN | If this is TRUE , then any positive integer is acceptable as the job instance. If this is FALSE (the default), then the specified instance must be running; otherwise the routine raises an exception. |

## Usage Notes

Syntax DBMS_JOB.SUBMIT ( job OUT BINARY_INTEGER, what IN VARCHAR2, next_date IN DATE DEFAULT SYSDATE, interval IN VARCHAR2 DEFAULT 'null', no_parse IN BOOLEAN DEFAULT FALSE, instance IN BINARY_INTEGER DEFAULT any_instance, force IN BOOLEAN DEFAULT FALSE); Parameters Table 94-9 SUBMIT Procedure Parameters Parameter Description job System-assigned ID of the job being run. To find this ID, query the JOB column of the USER_JOBS or DBA_JOBS view what PL/SQL text o the job to be run. This must be a valid PL/SQL statement or block of code. For example, to run a stored procedure P , you could pass the string P ; (with the semi-colon) to this routine. The SQL that you submit in the what parameter is wrapped in the following PL/SQL block: DECLARE job BINARY_INTEGER := :job; next_date DATE := :mydate; broken BOOLEAN := FALSE; BEGIN WHAT :mydate := next_date; IF broken THEN :b := 1; ELSE :b := 0; END IF; END; Ensure that you include the ; semi-colon with the statement. next_date Next date when the job will be run. interval Date function that calculates the next time to run the job. The default is NULL . This must evaluate to a either a future point in time or NULL . no_parse A flag. The default is FALSE . If this is set to FALSE , then Oracle parses the procedure associated with the job. If this is set to TRUE , then Oracle parses the procedure associated with the job the first time that the job is run. For example, if you want to submit a job before you have created the tables associated with the job, then set this to TRUE . instance When a job is submitted, specifies which instance can run the job. force If this is TRUE , then any positive integer is acceptable as the job instance. If this is FALSE (the default), then the specified instance must be running; otherwise the routine raises an exception. Usage Notes Your job will not be available for processing by the job queue in the background until it is committed. The parameters instance and force are added for job queue affinity. Job queue affinity gives users the ability to indicate whether a particular instance or any instance can run a submitted job. Example This submits a new job to the job queue. The job calls the procedure DBMS_DDL . ANALYZE_OBJECT to generate optimizer statistics for the table DQUON . ACCOUNTS . The statistics are based on a sample of half the rows of the ACCOUNTS table. The job is run every 24 hours: VARIABLE jobno number; BEGIN DBMS_JOB.SUBMIT(:jobno, 'dbms_ddl.analyze_object(''TABLE'', ''DQUON'', ''ACCOUNTS'', ''ESTIMATE'', NULL, 50);' SYSDATE, 'SYSDATE + 1'); COMMIT; END; / Statement processed. print jobno JOBNO ---------- 14144