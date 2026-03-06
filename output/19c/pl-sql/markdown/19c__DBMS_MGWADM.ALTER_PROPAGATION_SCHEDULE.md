---
id: 19c__DBMS_MGWADM.ALTER_PROPAGATION_SCHEDULE
name: DBMS_MGWADM.ALTER_PROPAGATION_SCHEDULE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWADM
tags: [dbms_mgwadm]
source_file: DBMS_MGWADM.html
---

# DBMS_MGWADM.ALTER_PROPAGATION_SCHEDULE

This procedure alters a propagation schedule.

## Syntax

```sql
DBMS_MGWADM.ALTER_PROPAGATION_SCHEDULE (
   schedule_id  IN VARCHAR2,
   duration     IN NUMBER DEFAULT NULL,
   next_time    IN VARCHAR2 DEFAULT NULL,
   latency      IN NUMBER DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schedule_id | VARCHAR2 | IN | Identifies the propagation schedule to be altered |
| duration | NUMBER | IN | Reserved for future use |
| next_time | VARCHAR2 | IN | Reserved for future use |
| latency | NUMBER | IN | Specifies the polling interval, in seconds, used by the Messaging Gateway agent when checking for messages in the source queue. If no messages are available in the source queue, then the agent will not poll again until the polling interval has passed. Once the agent detects a message it will continue propagating messages as long as any are available. Values: NULL or value > 0. If latency is NULL , then the Messaging Gateway agent default polling interval will be used. The default polling interval is 5 seconds, but it can be overridden by the Messaging Gateway initialization file. |

## Usage Notes

Note: This subprogram has been deprecated as a result of improved technology (see ALTER_JOB Procedure ), and is retained only for reasons of backward compatibility. Note: This subprogram has been deprecated as a result of improved technology (see ALTER_JOB Procedure ), and is retained only for reasons of backward compatibility. Syntax DBMS_MGWADM.ALTER_PROPAGATION_SCHEDULE ( schedule_id IN VARCHAR2, duration IN NUMBER DEFAULT NULL, next_time IN VARCHAR2 DEFAULT NULL, latency IN NUMBER DEFAULT NULL); Parameters Table 110-25 ALTER_PROPAGATION_SCHEDULE Procedure Parameters Parameter Description schedule_id Identifies the propagation schedule to be altered duration Reserved for future use next_time Reserved for future use latency Specifies the polling interval, in seconds, used by the Messaging Gateway agent when checking for messages in the source queue. If no messages are available in the source queue, then the agent will not poll again until the polling interval has passed. Once the agent detects a message it will continue propagating messages as long as any are available. Values: NULL or value > 0. If latency is NULL , then the Messaging Gateway agent default polling interval will be used. The default polling interval is 5 seconds, but it can be overridden by the Messaging Gateway initialization file. Usage Notes This procedure always overwrites the existing value for each parameter. If a given parameter is not specified, then the existing values are overwritten with the default value.