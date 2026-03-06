---
id: 19c__DBMS_SCHEDULER.DROP_JOB_CLASS
name: DBMS_SCHEDULER.DROP_JOB_CLASS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.DROP_JOB_CLASS

This procedure drops a job class. Dropping a job class means that all the metadata about the job class is removed from the database.

## Syntax

```sql
DBMS_SCHEDULER.DROP_JOB_CLASS (
   job_class_name          IN VARCHAR2,
   force                   IN BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| job_class_name | VARCHAR2 | IN | The name of the job class. Can be a comma-delimited list. |
| force | BOOLEAN | IN | If force is set to FALSE , a class being dropped must not be referenced by any jobs, otherwise an error occurs. If force is set to TRUE , jobs belonging to the class are disabled and their class is set to the default class. Only if this is successful is the class dropped. Running jobs that belong to the job class are not affected. |

## Usage Notes

Syntax DBMS_SCHEDULER.DROP_JOB_CLASS ( job_class_name IN VARCHAR2, force IN BOOLEAN DEFAULT FALSE); Parameters Table 151-53 DROP_JOB_CLASS Procedure Parameters Parameter Description job_class_name The name of the job class. Can be a comma-delimited list. force If force is set to FALSE , a class being dropped must not be referenced by any jobs, otherwise an error occurs. If force is set to TRUE , jobs belonging to the class are disabled and their class is set to the default class. Only if this is successful is the class dropped. Running jobs that belong to the job class are not affected. Usage Notes Dropping a job class requires the MANAGE SCHEDULER system privilege.