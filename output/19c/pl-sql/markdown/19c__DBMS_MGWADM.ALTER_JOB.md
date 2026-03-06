---
id: 19c__DBMS_MGWADM.ALTER_JOB
name: DBMS_MGWADM.ALTER_JOB
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWADM
tags: [dbms_mgwadm]
source_file: DBMS_MGWADM.html
---

# DBMS_MGWADM.ALTER_JOB

This procedure alters the properties of a propagation job.

## Syntax

```sql
DBMS_MGWADM.ALTER_JOB (
   job_name          IN   VARCHAR2,
   rule              IN   VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE,
   transformation    IN   VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE,
   exception_queue   IN   VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE,
   poll_interval     IN   PLS_INTEGER DEFAULT 0,
   options           IN   SYS.MGW_PROPERTIES DEFAULT NULL,
   comments          IN   VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| job_name | VARCHAR2 | IN | Identifies the propagation job |
| rule | VARCHAR2 | IN | Specifies an optional subscription rule used to dequeue messages from the propagation source. The syntax and interpretation of this parameter depend on the propagation type. A NULL value indicates that no subscription rule is needed. If DBMS_MGWADM . NO_CHANGE , then the current value is unchanged. |
| transformation | VARCHAR2 | IN | Specifies the transformation needed to convert between the Oracle Streams AQ payload and an ADT defined by Messaging Gateway. The type of transformation needed depends on the value specified for propagation_type . A NULL value indicates that no transformation is needed. If DBMS_MGWADM . NO_CHANGE , the current value is unchanged. |
| exception_queue | VARCHAR2 | IN | Specifies a queue used for exception message logging purposes. This queue must be on the same messaging system as the propagation source. In cases in which no exception queue is associated with the job, propagation stops if a problem occurs. The syntax and interpretation of this parameter depend on the propagation type. A NULL value indicates that no exception queue is used. If DBMS_MGWADM . NO_CHANGE , the current value is unchanged. |
| poll_interval | PLS_INTEGER | IN | Specifies the polling interval, in seconds, used by the Messaging Gateway agent when checking for messages in the source queue. If no messages are available the agent will not poll again until the polling interval has passed. Once the agent detects a message it will continue propagating messages as long as any are available. Values: NULL , 0, or value > 0: If zero (default), the current value will not be changed. If NULL , the current value will be reset and the Messaging Gateway default polling interval will be used. The default polling interval is 5 seconds and can be overridden by the Messaging Gateway initialization file. |
| options | SYS.MGW_PROPERTIES | IN | Optional job properties. If NULL , no options will be changed. If not NULL , then the properties specified in this list are combined with the current optional properties to form a new set of job options. |
| comments | VARCHAR2 | IN | An optional comment for this agent, or NULL if one is not desired. If DBMS_MGWADM . NO_CHANGE , the current value will not be changed. |

## Usage Notes

Syntax DBMS_MGWADM.ALTER_JOB ( job_name IN VARCHAR2, rule IN VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE, transformation IN VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE, exception_queue IN VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE, poll_interval IN PLS_INTEGER DEFAULT 0, options IN SYS.MGW_PROPERTIES DEFAULT NULL, comments IN VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE ); Parameters Table 110-22 ALTER_JOB Procedure Parameters Parameter Description job_name Identifies the propagation job rule Specifies an optional subscription rule used to dequeue messages from the propagation source. The syntax and interpretation of this parameter depend on the propagation type. A NULL value indicates that no subscription rule is needed. If DBMS_MGWADM . NO_CHANGE , then the current value is unchanged. transformation Specifies the transformation needed to convert between the Oracle Streams AQ payload and an ADT defined by Messaging Gateway. The type of transformation needed depends on the value specified for propagation_type . A NULL value indicates that no transformation is needed. If DBMS_MGWADM . NO_CHANGE , the current value is unchanged. exception_queue Specifies a queue used for exception message logging purposes. This queue must be on the same messaging system as the propagation source. In cases in which no exception queue is associated with the job, propagation stops if a problem occurs. The syntax and interpretation of this parameter depend on the propagation type. A NULL value indicates that no exception queue is used. If DBMS_MGWADM . NO_CHANGE , the current value is unchanged. poll_interval Specifies the polling interval, in seconds, used by the Messaging Gateway agent when checking for messages in the source queue. If no messages are available the agent will not poll again until the polling interval has passed. Once the agent detects a message it will continue propagating messages as long as any are available. Values: NULL , 0, or value > 0: If zero (default), the current value will not be changed. If NULL , the current value will be reset and the Messaging Gateway default polling interval will be used. The default polling interval is 5 seconds and can be overridden by the Messaging Gateway initialization file. options Optional job properties. If NULL , no options will be changed. If not NULL , then the properties specified in this list are combined with the current optional properties to form a new set of job options. comments An optional comment for this agent, or NULL if one is not desired. If DBMS_MGWADM . NO_CHANGE , the current value will not be changed. Usage Notes If the non-Oracle messaging link being accessed for the propagation job uses a JMS interface, then the Messaging Gateway agent will use the Oracle JMS interface to access the Oracle Streams AQ queues. Otherwise the native Oracle Streams AQ interface will be used. Parameters are interpreted differently when the Messaging Gateway agent uses Oracle JMS for JMS connections. The subscriber rule cannot be altered when propagating from a JMS source. Instead, the propagation job must be dropped and re-created with the new rule. For JMS, changing the message selector on a durable subscription is equivalent to deleting and re-creating the subscription. Transformations are not currently supported if the Oracle JMS interface is used for propagation. The transformation parameter must be DBMS_MGWADM . NO_CHANGE (the default value). The options parameter specifies a set of properties used to alter the current optional properties. Each property affects the current property list in a particular manner; add a new property, replace an existing property, remove an existing property or remove all properties. Note: SYS.MGW_PROPERTY Object Type for more information about the options parameter OUTBOUND_PROPAGATION Jobs for outbound propagation parameter interpretation INBOUND_PROPAGATION Jobs for inbound propagation parameter interpretation Note: SYS.MGW_PROPERTY Object Type for more information about the options parameter OUTBOUND_PROPAGATION Jobs for outbound propagation parameter interpretation INBOUND_PROPAGATION Jobs for inbound propagation parameter interpretation