---
id: 19c__DBMS_SCHEDULER.SET_AGENT_REGISTRATION_PASS
name: DBMS_SCHEDULER.SET_AGENT_REGISTRATION_PASS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.SET_AGENT_REGISTRATION_PASS

This procedure sets the agent registration password for a database.

## Syntax

```sql
DBMS_SCHEDULER.SET_AGENT_REGISTRATION_PASS (
   registration_password   IN VARCHAR2,
   expiration_date         IN TIMESTAMP WITH TIME ZONE DEFAULT NULL,
   max_uses                IN NUMBER DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| registration_password | VARCHAR2 | IN | This is the password that remote agents must specify in order to successfully register with the database. If this is NULL , then no agents will be able to register with the database. |
| expiration_date | TIMESTAMP | IN | If this is set to a non- NULL value, then the registration_password is not valid after this date. After this date, no agents can register with the database. This cannot be set to a date in the past. |
| max_uses | NUMBER | IN | This is the maximum number of successful registrations that can be performed with this password. After the number of successful registrations has been performed with this password, then no agents can register with the database. This cannot be set to 0 or a negative value. If this is set to NULL , then there will be no limit on the number of successful registrations. |

## Usage Notes

A Scheduler agent must register with the database before the database can submit jobs to the agent. The agent must provide this password when registering. Syntax DBMS_SCHEDULER.SET_AGENT_REGISTRATION_PASS ( registration_password IN VARCHAR2, expiration_date IN TIMESTAMP WITH TIME ZONE DEFAULT NULL, max_uses IN NUMBER DEFAULT NULL); Parameters Table 151-80 SET_AGENT_REGISTRATION_PASS Procedure Parameters Parameter Description registration_password This is the password that remote agents must specify in order to successfully register with the database. If this is NULL , then no agents will be able to register with the database. expiration_date If this is set to a non- NULL value, then the registration_password is not valid after this date. After this date, no agents can register with the database. This cannot be set to a date in the past. max_uses This is the maximum number of successful registrations that can be performed with this password. After the number of successful registrations has been performed with this password, then no agents can register with the database. This cannot be set to 0 or a negative value. If this is set to NULL , then there will be no limit on the number of successful registrations. Usage Notes To prevent abuse, this password can be set to expire after a given date or a maximum number of successful registrations. This procedure will overwrite any password already set. This requires the MANAGE SCHEDULER system privilege. By default, max_uses is set to NULL , which means that there is no limit to the number of successful registrations. Oracle recommends that an agent registration password be reset after every agent registration or every known set of agent registrations. Furthermore, Oracle recommends that this password be set to NULL if no new agents are being registered.