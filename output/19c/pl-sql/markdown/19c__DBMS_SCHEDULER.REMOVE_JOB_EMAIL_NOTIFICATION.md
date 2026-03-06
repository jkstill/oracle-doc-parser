---
id: 19c__DBMS_SCHEDULER.REMOVE_JOB_EMAIL_NOTIFICATION
name: DBMS_SCHEDULER.REMOVE_JOB_EMAIL_NOTIFICATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.REMOVE_JOB_EMAIL_NOTIFICATION

This procedure removes e-mail notifications for a job. You can remove all e-mail notifications or remove notifications only for specified recipients or specified events.

## Syntax

```sql
DBMS_SCHEDULER.REMOVE_JOB_EMAIL_NOTIFICATION (
    job_name             IN VARCHAR2,
    recipients           IN VARCHAR2 DEFAULT NULL,
    events               IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| job_name | VARCHAR2 | IN | Name of the job to remove e-mail notifications for. Cannot be NULL . |
| recipients | VARCHAR2 | IN | E-mail address to remove e-mail notification for. Comma-separated list of e-mail addresses. |
| events | VARCHAR2 | IN | Job state event to remove e-mail notification for. Comma-separate list of job state events. |

## Usage Notes

Syntax DBMS_SCHEDULER.REMOVE_JOB_EMAIL_NOTIFICATION ( job_name IN VARCHAR2, recipients IN VARCHAR2 DEFAULT NULL, events IN VARCHAR2 DEFAULT NULL); Parameters Table 151-76 ADD_JOB_EMAIL_NOTIFICATION Procedure Parameters Parameter Description job_name Name of the job to remove e-mail notifications for. Cannot be NULL . recipients E-mail address to remove e-mail notification for. Comma-separated list of e-mail addresses. events Job state event to remove e-mail notification for. Comma-separate list of job state events. Usage Notes When you specify multiple recipients and multiple events, the notification for each specified event is removed for each specified recipient. The procedure ignores any recipients or events that are specified but that were not previously added. If recipients is NULL , e-mail notifications for the specified events are removed for all existing recipients. If events is NULL , notifications for all events are removed for the specified recipients. If both recipients and events are NULL , all e-mail notifications are removed for the job. For example, if recipients is ' jsmith@example.com,rjones@example.com ' and events is ' JOB_FAILED,JOB_BROKEN ', then notifications for both the JOB_FAILED and JOB_BROKEN events are removed for both jsmith and rjones. If recipients is NULL , then notifications for both the JOB_FAILED and JOB_BROKEN events are removed for jsmith, rjones, and any other previously defined recipients for these events. To call this procedure, you must be the job owner or a user with the CREATE ANY JOB system privilege or ALTER object privilege on the job. See Also: " ADD_JOB_EMAIL_NOTIFICATION Procedure " See Also: " ADD_JOB_EMAIL_NOTIFICATION Procedure "