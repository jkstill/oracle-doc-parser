---
id: 19c__DBMS_MGWADM.ALTER_SUBSCRIBER
name: DBMS_MGWADM.ALTER_SUBSCRIBER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWADM
tags: [dbms_mgwadm]
source_file: DBMS_MGWADM.html
---

# DBMS_MGWADM.ALTER_SUBSCRIBER

This procedure alters the parameters of a subscriber used to consume messages from a source queue for propagation to a destination.

## Syntax

```sql
DBMS_MGWADM.ALTER_SUBSCRIBER (
   subscriber_id    IN VARCHAR2,
   rule             IN VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE,
   transformation   IN VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE,
   exception_queue  IN VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE,
   options          IN SYS.MGW_PROPERTIES DEFAULT NULL );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| subscriber_id | VARCHAR2 | IN | Identifies the subscriber to be altered |
| rule | VARCHAR2 | IN | Specifies an optional subscription rule used by the subscriber to dequeue messages from the source queue. The syntax and interpretation of this parameter depend on the subscriber propagation type. A NULL value indicates that no subscription rule is needed. If DBMS_MGWADM.NO_CHANGE, then the current value is unchanged. |
| transformation | VARCHAR2 | IN | Specifies the transformation needed to convert between the Oracle Database Advanced Queuing payload and an ADT defined by Messaging Gateway. The type of transformation needed depends on the subscriber propagation type. A NULL value indicates that no transformation is needed. If DBMS_MGWADM.NO_CHANGE, then the current value is unchanged. |
| exception_queue | VARCHAR2 | IN | Specifies a queue used for exception message logging. This queue must be on the same messaging system as the propagation source. If no exception queue is associated with the subscriber, then propagation stops if a problem occurs. The syntax and interpretation of this parameter depend on the subscriber propagation type. A NULL value indicates that no exception queue is used. If DBMS_MGWADM.NO_CHANGE, then the current value is unchanged. The source queue and exception queue cannot be the same queue. |
| options | SYS.MGW_PROPERTIES | IN | Optional subscriber properties. If NULL , then no options will be changed. If not NULL , then the properties specified in this list are combined with the current optional properties to form a new set of subscriber options. |

## Usage Notes

Note: This subprogram has been deprecated as a result of improved technology (see ALTER_JOB Procedure ), and is retained only for reasons of backward compatibility. Note: This subprogram has been deprecated as a result of improved technology (see ALTER_JOB Procedure ), and is retained only for reasons of backward compatibility. Syntax DBMS_MGWADM.ALTER_SUBSCRIBER ( subscriber_id IN VARCHAR2, rule IN VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE, transformation IN VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE, exception_queue IN VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE, options IN SYS.MGW_PROPERTIES DEFAULT NULL ); Parameters Table 110-26 ALTER_SUBSCRIBER Procedure Parameters Parameter Description subscriber_id Identifies the subscriber to be altered rule Specifies an optional subscription rule used by the subscriber to dequeue messages from the source queue. The syntax and interpretation of this parameter depend on the subscriber propagation type. A NULL value indicates that no subscription rule is needed. If DBMS_MGWADM.NO_CHANGE, then the current value is unchanged. transformation Specifies the transformation needed to convert between the Oracle Database Advanced Queuing payload and an ADT defined by Messaging Gateway. The type of transformation needed depends on the subscriber propagation type. A NULL value indicates that no transformation is needed. If DBMS_MGWADM.NO_CHANGE, then the current value is unchanged. exception_queue Specifies a queue used for exception message logging. This queue must be on the same messaging system as the propagation source. If no exception queue is associated with the subscriber, then propagation stops if a problem occurs. The syntax and interpretation of this parameter depend on the subscriber propagation type. A NULL value indicates that no exception queue is used. If DBMS_MGWADM.NO_CHANGE, then the current value is unchanged. The source queue and exception queue cannot be the same queue. options Optional subscriber properties. If NULL , then no options will be changed. If not NULL , then the properties specified in this list are combined with the current optional properties to form a new set of subscriber options. Usage Notes If the non-Oracle messaging link being accessed for the subscriber uses a JMS interface, then the Messaging Gateway agent will use the Oracle JMS interface to access the Oracle Database Advanced Queuing queues. Otherwise the native Oracle Database Advanced Queuing interface will be used. Parameters are interpreted differently when the Messaging Gateway agent uses Oracle JMS for JMS connections. When propagating from a JMS source, the subscriber rule cannot be altered. Instead, the subscriber must be removed and added with the new rule. For JMS, changing the message selector on a durable subscription is equivalent to deleting and re-creating the subscription. Transformations are not currently supported if the Oracle JMS interface is used for propagation. The transformation parameter must be DBMS_MGWADM.NO_CHANGE (the default value). The options parameter specifies a set of properties used to alter the current optional properties. Each property affects the current property list in a particular manner: add a new property, replace an existing property, remove an existing property, or remove all properties. See Also: SYS.MGW_PROPERTIES Object Type for more information on the options parameter "WebSphere MQ System Properties" in Oracle Database Advanced Queuing User's Guide for more information about WebSphere MQ subscriber options "TIB/Rendezvous System Properties" in Oracle Database Advanced Queuing User's Guide for more information about TIB/Rendezvous subscriber options " OUTBOUND_PROPAGATION Subscribers for outbound propagation parameter interpretation " INBOUND_PROPAGATION Subscribers for inbound propagation parameter interpretation