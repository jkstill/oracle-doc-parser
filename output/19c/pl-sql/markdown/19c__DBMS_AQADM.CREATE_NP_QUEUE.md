---
id: 19c__DBMS_AQADM.CREATE_NP_QUEUE
name: DBMS_AQADM.CREATE_NP_QUEUE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.CREATE_NP_QUEUE

This procedure creates a nonpersistent RAW queue.

## Syntax

```sql
DBMS_AQADM.CREATE_NP_QUEUE ( 
   queue_name              IN        VARCHAR2, 
   multiple_consumers      IN        BOOLEAN  DEFAULT FALSE, 
   comment                 IN        VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| queue_name | VARCHAR2 | IN | Name of the nonpersistent queue that is to be created. The name must be unique within a schema and must follow object name guidelines in Oracle Database SQL Language Reference. |
| multiple_consumers | BOOLEAN | IN | FALSE means queues created in the table can only have one consumer for each message. This is the default. TRUE means queues created in the table can have multiple consumers for each message. Note that this parameter is distinguished at the queue level, because a nonpersistent queue does not inherit this characteristic from any user-created queue table. |
| comment | VARCHAR2 | IN | User-specified description of the queue. This user comment is added to the queue catalog. |

## Usage Notes

Note: Nonpersistent queues are deprecated as of Release 10gR2. Oracle recommends using buffered messaging. Note: Nonpersistent queues are deprecated as of Release 10gR2. Oracle recommends using buffered messaging. Syntax DBMS_AQADM.CREATE_NP_QUEUE ( queue_name IN VARCHAR2, multiple_consumers IN BOOLEAN DEFAULT FALSE, comment IN VARCHAR2 DEFAULT NULL); Parameters Table 23-20 CREATE_NP_QUEUE Procedure Parameters Parameter Description queue_name Name of the nonpersistent queue that is to be created. The name must be unique within a schema and must follow object name guidelines in Oracle Database SQL Language Reference. multiple_consumers FALSE means queues created in the table can only have one consumer for each message. This is the default. TRUE means queues created in the table can have multiple consumers for each message. Note that this parameter is distinguished at the queue level, because a nonpersistent queue does not inherit this characteristic from any user-created queue table. comment User-specified description of the queue. This user comment is added to the queue catalog. Usage Notes The queue may be either single-consumer or multiconsumer queue. All queue names must be unique within a schema. The queues are created in a 8.1-compatible or higher system-created queue table ( AQ$_MEM_SC or AQ$_MEM_MC ) in the same schema as that specified by the queue name. If the queue name does not specify a schema name, the queue is created in the login user's schema. After a queue is created with CREATE_NP_QUEUE , it can be enabled by calling START_QUEUE . By default, the queue is created with both enqueue and dequeue disabled. You cannot dequeue from a nonpersistent queue. The only way to retrieve a message from a nonpersistent queue is by using the OCI notification mechanism. You cannot invoke the LISTEN call on a nonpersistent queue.