---
id: 19c__DBMS_MGWADM.REMOVE_JOB
name: DBMS_MGWADM.REMOVE_JOB
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWADM
tags: [dbms_mgwadm]
source_file: DBMS_MGWADM.html
---

# DBMS_MGWADM.REMOVE_JOB

This procedure removes a propagation job.

## Syntax

```sql
DBMS_MGWADM.REMOVE_JOB(
   job_name   IN   VARCHAR2,   force      IN   PLS_INTEGER DEFAULT DBMS_MGWADM.NO_FORCE);
```

## Usage Notes

Syntax DBMS_MGWADM.REMOVE_JOB( job_name IN VARCHAR2, force IN PLS_INTEGER DEFAULT DBMS_MGWADM.NO_FORCE); Parameters Table 110-39 REMOVE_JOB Procedure Parameters Parameters Description job_name Identifies the propagation job force Specifies whether the procedure should succeed even if Messaging Gateway is not able to perform all cleanup actions pertaining to this propagation job. Values: DBMS_MGWADM . NO_FORCE , DBMS_MGWADM . FORCE NO_FORCE (default) means the job is not removed if Messaging Gateway is unable to clean up successfully FORCE means the job is removed even though all cleanup actions may not be done Usage Notes The Messaging Gateway agent uses various resources of the Oracle Database and the non-Oracle messaging system for its propagation work. These resources need to be released when the job is removed. For example, Messaging Gateway may create a durable subscriber on the source queue that should be removed when the job is removed. Therefore, this procedure should normally be called when the Messaging Gateway agent is running and able to access the non-Oracle messaging system associated with this job. For outbound propagation, a local subscriber is removed from the Oracle Streams AQ queue when the propagation source is a multiple consumer queue.