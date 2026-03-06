---
id: 19c__DBMS_MGWADM.REGISTER_FOREIGN_QUEUE
name: DBMS_MGWADM.REGISTER_FOREIGN_QUEUE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWADM
tags: [dbms_mgwadm]
source_file: DBMS_MGWADM.html
---

# DBMS_MGWADM.REGISTER_FOREIGN_QUEUE

This procedure registers a non-Oracle queue entity in Messaging Gateway.

## Syntax

```sql
DBMS_MGWADM.REGISTER_FOREIGN_QUEUE(
   name            IN VARCHAR2,
   linkname        IN VARCHAR2,
   provider_queue  IN VARCHAR2 DEFAULT NULL,
   domain          IN INTEGER DEFAULT NULL,
   options         IN SYS.MGW_PROPERTIES DEFAULT NULL,
   comment         IN VARCHAR2 DEFAULT NULL);
```

## Usage Notes

Syntax DBMS_MGWADM.REGISTER_FOREIGN_QUEUE( name IN VARCHAR2, linkname IN VARCHAR2, provider_queue IN VARCHAR2 DEFAULT NULL, domain IN INTEGER DEFAULT NULL, options IN SYS.MGW_PROPERTIES DEFAULT NULL, comment IN VARCHAR2 DEFAULT NULL); Parameters Table 110-37 REGISTER_FOREIGN_QUEUE Procedure Parameters Parameters Description name The registered queue name. This name identifies the foreign queue within Messaging Gateway and need not match the name of the queue in the foreign messaging system. linkname The link name for the messaging system on which this queue exists provider_queue The message provider (native) queue name. If NULL, then the value provided for the name parameter is used as the provider queue name. domain The domain type of the queue. NULL means the domain type is automatically determined based on the messaging system of the queue. DBMS_MGWADM.DOMAIN_QUEUE is for a queue (point-to-point model). DBMS_MGWADM.DOMAIN_TOPIC is for a topic (publish-subscribe model). options Optional queue properties comment A user-specified description. Can be NULL . Usage Notes This procedure does not create the physical queue in the non-Oracle messaging system. The non-Oracle queue must be created using the administration tools for that messaging system. See Also: For more information when registering queues for the WebSphere MQ messaging system or the TIB/Rendezvous messaging system, specifically "Optional Foreign Queue Configuration Properties" in Oracle Database Advanced Queuing User's Guide . See Also: For more information when registering queues for the WebSphere MQ messaging system or the TIB/Rendezvous messaging system, specifically "Optional Foreign Queue Configuration Properties" in Oracle Database Advanced Queuing User's Guide .