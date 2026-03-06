---
id: 19c__DBMS_MGWADM.SCHEDULE_PROPAGATION
name: DBMS_MGWADM.SCHEDULE_PROPAGATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWADM
tags: [dbms_mgwadm]
source_file: DBMS_MGWADM.html
---

# DBMS_MGWADM.SCHEDULE_PROPAGATION

This procedure schedules message propagation from a source to a destination.

## Syntax

```sql
DBMS_MGWADM.SCHEDULE_PROPAGATION (
   schedule_id       IN VARCHAR2,
   propagation_type  IN BINARY_INTEGER,
   source            IN VARCHAR2,
   destination       IN VARCHAR2,
   start_time        IN DATE DEFAULT SYSDATE,
   duration          IN NUMBER DEFAULT NULL,
   next_time         IN VARCHAR2 DEFAULT NULL,
   latency           IN NUMBER DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schedule_id | VARCHAR2 | IN | Specifies a user-defined name that identifies the schedule |
| propagation_type | BINARY_INTEGER | IN | Specifies the type of message propagation. DBMS_MGWADM.OUTBOUND_PROPAGATION is for Oracle Database Advanced Queuing to non-Oracle propagation. DBMS_MGWADM.INBOUND_PROPAGATION is for non-Oracle to Oracle Database Advanced Queuing propagation. |
| source | VARCHAR2 | IN | Specifies the source queue whose messages are to be propagated. The syntax and interpretation of this parameter depend on the value specified for propagation_type . |
| destination | VARCHAR2 | IN | Specifies the destination queue to which messages are propagated. The syntax and interpretation of this parameter depend on the value specified for propagation_type . |
| start_time | DATE | IN | Reserved for future use |
| duration | NUMBER | IN | Reserved for future use |
| next_time | VARCHAR2 | IN | Reserved for future use |
| latency | NUMBER | IN | Specifies the polling interval, in seconds, used by the Messaging Gateway agent when checking for messages in the source queue. If no messages are available in the source queue, then the agent will not poll again until the polling interval has passed. Once the agent detects a message it will continue propagating messages as long as any are available. Values: NULL or value > 0. If latency is NULL , then the Messaging Gateway agent default polling interval will be used. The default polling interval is 5 seconds but it can be overridden by the Messaging Gateway initialization file. |

## Usage Notes

The schedule must be enabled and Messaging Gateway started in order for messages to be propagated. Note: This subprogram has been deprecated as a result of improved technology (see CREATE_JOB Procedure ), and is retained only for reasons of backward compatibility. Note: This subprogram has been deprecated as a result of improved technology (see CREATE_JOB Procedure ), and is retained only for reasons of backward compatibility. Syntax DBMS_MGWADM.SCHEDULE_PROPAGATION ( schedule_id IN VARCHAR2, propagation_type IN BINARY_INTEGER, source IN VARCHAR2, destination IN VARCHAR2, start_time IN DATE DEFAULT SYSDATE, duration IN NUMBER DEFAULT NULL, next_time IN VARCHAR2 DEFAULT NULL, latency IN NUMBER DEFAULT NULL); Parameters Table 110-45 SCHEDULE_PROPAGATION Procedure Parameters Parameter Description schedule_id Specifies a user-defined name that identifies the schedule propagation_type Specifies the type of message propagation. DBMS_MGWADM.OUTBOUND_PROPAGATION is for Oracle Database Advanced Queuing to non-Oracle propagation. DBMS_MGWADM.INBOUND_PROPAGATION is for non-Oracle to Oracle Database Advanced Queuing propagation. source Specifies the source queue whose messages are to be propagated. The syntax and interpretation of this parameter depend on the value specified for propagation_type . destination Specifies the destination queue to which messages are propagated. The syntax and interpretation of this parameter depend on the value specified for propagation_type . start_time Reserved for future use duration Reserved for future use next_time Reserved for future use latency Specifies the polling interval, in seconds, used by the Messaging Gateway agent when checking for messages in the source queue. If no messages are available in the source queue, then the agent will not poll again until the polling interval has passed. Once the agent detects a message it will continue propagating messages as long as any are available. Values: NULL or value > 0. If latency is NULL , then the Messaging Gateway agent default polling interval will be used. The default polling interval is 5 seconds but it can be overridden by the Messaging Gateway initialization file. Usage Notes For outbound propagation, parameters are interpreted as follows: source specifies the local Oracle Database Advanced Queuing queue from which messages are propagated. This must have a syntax of schema.queue . destination specifies the foreign queue to which messages are propagated. This must have a syntax of registered_queue@message_link . For inbound propagation, parameters are interpreted as follows: source specifies the foreign queue from which messages are propagated. This must have a syntax of registered_queue@message_link . destination specifies the local Oracle Database Advanced Queuing queue to which messages are propagated. This must have a syntax of schema.queue . The schedule is set to an enabled state when it is created.