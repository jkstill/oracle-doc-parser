---
id: 19c__DBMS_AQADM.CREATE_SHARDED_QUEUE
name: DBMS_AQADM.CREATE_SHARDED_QUEUE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.CREATE_SHARDED_QUEUE

The CREATE_SHARDED_QUEUE API creates a queue and its queue table as appropriate for a sharded queue. This API cannot be used to create unsharded queues. Sharded queues must be created using this single integrated API that will automatically set AQ properties as needed.

## Syntax

```sql
PROCEDURE CREATE_SHARDED_QUEUE (
	queue_name             IN VARCHAR2,
	storage_clause         IN VARCHAR2       DEFAULT NULL,
	multiple_consumers     IN BOOLEAN        DEFAULT FALSE,
	max_retries            IN NUMBER         DEFAULT NULL,
	comment                IN VARCHAR2       DEFAULT NULL, 
	queue_payload_type     IN VARCHAR2       DEFAULT JMS_TYPE,
	queue_properties       IN QUEUE_PROPS_T  DEFAULT NULL,
	replication_mode       IN BINARY_INTEGER DEFAULT NONE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| queue_name | VARCHAR2 | IN | This required parameter specifies the name of the new queue. Maximum of 128 characters allowed. |
| storage_clause | VARCHAR2 | IN | The storage parameter is included in the CREATE TABLE statement when the queue table is created. The storage_clause argument can take any text that can be used in a standard CREATE TABLE storage_clause argument. The storage parameter can be made up of any combinations of the following parameters: PCTFREE , PCTUSED , INITRANS , MAXTRANS , TABLESPACE , LOB , and a table storage clause. If a tablespace is not specified here, then the queue table and all its related objects are created in the default user tablespace. If a tablespace is specified here, then the queue table and all its related objects are created in the tablespace specified in the storage clause. See Oracle Database SQL Language Reference for the usage of these parameters. |
| multiple_consumers | BOOLEAN | IN | FALSE means queues can only have one consumer for each message. This is the default. TRUE means queues created in the table can have multiple consumers for each message. |
| max_retries | NUMBER | IN | This optional parameter limits the number of times that a dequeue can reattempted on a message after a failure. The maximum value of max_retries is 2**31 -1 . After the retry limit has been exceeded, the message will be purged from the queue. RETRY_COUNT is incremented when the application issues a rollback after executing the dequeue. If a dequeue transaction fails because the server process dies (including ALTER SYSTEM KILL SESSION ) or SHUTDOWN ABORT on the instance, then RETRY_COUNT is not incremented. |
| comment | VARCHAR2 | IN | This optional parameter is a user-specified description of the queue table. This user comment is added to the queue catalog. |
| queue_payload_type | VARCHAR2 | IN | Payload can be RAW , DBMS_AQADM.JMS_TYPE , or an object type. Default is DBMS_AQADM.JMS_TYPE . |
| queue_properties | QUEUE_PROPS_T | IN | Properties such as Normal or Exception Queue, Retry delay, retention time, sort list and cache hint. Refer to QUEUE_PROPS_T Type for ore information about queue_properties . |
| replication_mode | BINARY_INTEGER | IN | Reserved for future use. DBMS_AQADM.REPLICATION_MODE if Queue is being created in the Replication Mode or else DBMS_AQADM.NONE . Default is DBMS_AQADM.NONE . |

## Usage Notes

Sharded queues may be either a single consumer or a multi-consumer queue. Syntax PROCEDURE CREATE_SHARDED_QUEUE ( queue_name IN VARCHAR2, storage_clause IN VARCHAR2 DEFAULT NULL, multiple_consumers IN BOOLEAN DEFAULT FALSE, max_retries IN NUMBER DEFAULT NULL, comment IN VARCHAR2 DEFAULT NULL, queue_payload_type IN VARCHAR2 DEFAULT JMS_TYPE, queue_properties IN QUEUE_PROPS_T DEFAULT NULL, replication_mode IN BINARY_INTEGER DEFAULT NONE); Parameters Table 23-23 CREATE_SHARDED_QUEUE Procedure Parameters Parameter Description queue_name This required parameter specifies the name of the new queue. Maximum of 128 characters allowed. storage_clause The storage parameter is included in the CREATE TABLE statement when the queue table is created. The storage_clause argument can take any text that can be used in a standard CREATE TABLE storage_clause argument. The storage parameter can be made up of any combinations of the following parameters: PCTFREE , PCTUSED , INITRANS , MAXTRANS , TABLESPACE , LOB , and a table storage clause. If a tablespace is not specified here, then the queue table and all its related objects are created in the default user tablespace. If a tablespace is specified here, then the queue table and all its related objects are created in the tablespace specified in the storage clause. See Oracle Database SQL Language Reference for the usage of these parameters. multiple_consumers FALSE means queues can only have one consumer for each message. This is the default. TRUE means queues created in the table can have multiple consumers for each message. max_retries This optional parameter limits the number of times that a dequeue can reattempted on a message after a failure. The maximum value of max_retries is 2**31 -1 . After the retry limit has been exceeded, the message will be purged from the queue. RETRY_COUNT is incremented when the application issues a rollback after executing the dequeue. If a dequeue transaction fails because the server process dies (including ALTER SYSTEM KILL SESSION ) or SHUTDOWN ABORT on the instance, then RETRY_COUNT is not incremented. comment This optional parameter is a user-specified description of the queue table. This user comment is added to the queue catalog. queue_payload_type Payload can be RAW , DBMS_AQADM.JMS_TYPE , or an object type. Default is DBMS_AQADM.JMS_TYPE . queue_properties Properties such as Normal or Exception Queue, Retry delay, retention time, sort list and cache hint. Refer to QUEUE_PROPS_T Type for ore information about queue_properties . replication_mode Reserved for future use. DBMS_AQADM.REPLICATION_MODE if Queue is being created in the Replication Mode or else DBMS_AQADM.NONE . Default is DBMS_AQADM.NONE .