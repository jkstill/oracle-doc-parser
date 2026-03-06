---
id: 19c__DBMS_PCLXUTIL
name: DBMS_PCLXUTIL
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PCLXUTIL
tags: [dbms_pclxutil]
source_file: DBMS_PCLXUTIL.html
---

# DBMS_PCLXUTIL

Because DBMS_PCLXUTIL uses the DBMS_JOB package, you must be aware of the following limitations pertaining to DBMS_JOB :

## Syntax

```sql
job_queue_processes=n   #the number of background processes = n
```

## Usage Notes

You must decide appropriate values for the job_queue_processes initialization parameter. Clearly, if the job processes are not started before calling BUILD_PART_INDEX (), then the package will not function properly. The background processes are specified by the following init . ora parameters: job_queue_processes=n #the number of background processes = n Failure conditions are reported only in the trace files (a DBMS_JOB limitation), making it impossible to give interactive feedback to the user. This package prints a failure message, removes unfinished jobs from the queue, and requests the user to take a look at the j*.trc trace files. Note: For range partitioning, the minimum compatibility mode is 8.0; for range-hash composite partitioning, the minimum compatibility mode is 8 i . Note: For range partitioning, the minimum compatibility mode is 8.0; for range-hash composite partitioning, the minimum compatibility mode is 8 i .