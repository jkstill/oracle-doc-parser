---
id: 19c__DBMS_JOB.RUN
name: DBMS_JOB.RUN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_JOB
tags: [dbms_job]
source_file: DBMS_JOB.html
---

# DBMS_JOB.RUN

This procedure runs job JOB now. It runs it even if it is broken.

## Syntax

```sql
DBMS_JOB.RUN ( 
   job       IN  BINARY_INTEGER,
   force     IN  BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| job | BINARY_INTEGER | IN | System-assigned ID of the job being run. To find this ID, query the JOB column of the USER_JOBS or DBA_JOBS view. |
| force | BOOLEAN | IN | If this is TRUE , then instance affinity is irrelevant for running jobs in the foreground process. If this is FALSE , then the job can be run in the foreground only in the specified instance. |

## Usage Notes

Running the job recomputes next_date . See data dictionary view USER_JOBS or DBA_JOBS . Syntax DBMS_JOB.RUN ( job IN BINARY_INTEGER, force IN BOOLEAN DEFAULT FALSE); Parameters Table 94-8 RUN Procedure Parameters Parameter Description job System-assigned ID of the job being run. To find this ID, query the JOB column of the USER_JOBS or DBA_JOBS view. force If this is TRUE , then instance affinity is irrelevant for running jobs in the foreground process. If this is FALSE , then the job can be run in the foreground only in the specified instance. Example EXECUTE DBMS_JOB.RUN(14144); WARNING: This re-initializes the current session's packages. WARNING: This re-initializes the current session's packages.