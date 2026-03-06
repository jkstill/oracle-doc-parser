---
id: 19c__DBMS_AQADM.DISABLE_PROPAGATION_SCHEDULE
name: DBMS_AQADM.DISABLE_PROPAGATION_SCHEDULE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.DISABLE_PROPAGATION_SCHEDULE

This procedure disables a propagation schedule.

## Syntax

```sql
DBMS_AQADM.DISABLE_PROPAGATION_SCHEDULE ( 
   queue_name            IN   VARCHAR2, 
   destination           IN   VARCHAR2 DEFAULT NULL,
   destination_queue  IN  VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| queue_name | VARCHAR2 | IN | Name of the source queue whose messages are to be propagated, including the schema name. If the schema name is not specified, then it defaults to the schema name of the user. |
| destination | VARCHAR2 | IN | Destination database link. Messages in the source queue for recipients at this destination are propagated. If it is NULL , then the destination is the local database and messages are propagated to other queues in the local database. The length of this field is currently limited to 128 bytes, and if the name is not fully qualified, then the default domain name is used. |
| destination_queue | VARCHAR2 | IN | Name of the target queue to which messages are to be propagated in the form of a dblink |

## Usage Notes

Syntax DBMS_AQADM.DISABLE_PROPAGATION_SCHEDULE ( queue_name IN VARCHAR2, destination IN VARCHAR2 DEFAULT NULL, destination_queue IN VARCHAR2 DEFAULT NULL); Parameters Table 23-27 DISABLE_PROPAGATION_SCHEDULE Procedure Parameters Parameter Description queue_name Name of the source queue whose messages are to be propagated, including the schema name. If the schema name is not specified, then it defaults to the schema name of the user. destination Destination database link. Messages in the source queue for recipients at this destination are propagated. If it is NULL , then the destination is the local database and messages are propagated to other queues in the local database. The length of this field is currently limited to 128 bytes, and if the name is not fully qualified, then the default domain name is used. destination_queue Name of the target queue to which messages are to be propagated in the form of a dblink