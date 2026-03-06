---
id: 19c__DBMS_SCHEDULER.GENERATE_JOB_NAME
name: DBMS_SCHEDULER.GENERATE_JOB_NAME
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.GENERATE_JOB_NAME

This function returns a unique name for a job.

## Syntax

```sql
DBMS_SCHEDULER.GENERATE_JOB_NAME (
   prefix        IN VARCHAR2 DEFAULT 'JOB$_') RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| prefix | VARCHAR2 | IN | The prefix to use when generating the job name |

**Returns:** `VARCHAR2`

## Usage Notes

The name will be of the form {prefix}N where N is a number from a sequence. If no prefix is specified, the generated name will, by default, be JOB$_1 , JOB$_2 , JOB$_3 , and so on. If 'SCOTT' is specified as the prefix, the name will be SCOTT1 , SCOTT2 , and so on. Syntax DBMS_SCHEDULER.GENERATE_JOB_NAME ( prefix IN VARCHAR2 DEFAULT 'JOB$_') RETURN VARCHAR2; Parameters Table 151-63 GENERATE_JOB_NAME Function Parameter Parameter Description prefix The prefix to use when generating the job name Usage Notes If the prefix is explicitly set to NULL , the name is just the sequence number. In order to successfully use such numeric names, they must be surrounded by double quotes throughout the DBMS_SCHEDULER calls. A prefix cannot be longer than 18 characters and cannot end with a digit. Note that, even though the GENERATE_JOB_NAME function never returns the same job name twice, there is a small chance that the returned name matches an already existing database object. No specific Scheduler privileges are required to use this function.