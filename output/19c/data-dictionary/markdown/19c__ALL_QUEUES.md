---
id: 19c__ALL_QUEUES
name: ALL_QUEUES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_QUEUES.html
---

# ALL_QUEUES

Related Views

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the queue |
| NAME | VARCHAR2(128) | Name of the queue |
| QUEUE_TABLE | VARCHAR2(128) | Name of the table the queue data resides in |
| QID | NUMBER | Object number of the queue |
| QUEUE_TYPE | VARCHAR2(20) | Type of the queue: EXCEPTION_QUEUE NON_PERSISTENT_QUEUE NORMAL_QUEUE |
| MAX_RETRIES | NUMBER | Maximum number of retries allowed when dequeuing from the queue |
| RETRY_DELAY | NUMBER | Time interval between retries |
| ENQUEUE_ENABLED | VARCHAR2(7) | Indicates whether the queue is enabled for enqueue ( YES ) or not ( NO ) |
| DEQUEUE_ENABLED | VARCHAR2(7) | Indicates whether the queue is enabled for dequeue ( YES ) or not ( NO ) |
| RETENTION | VARCHAR2(40) | Time interval (in seconds) processed messages are retained in the queue, or FOREVER |
| USER_COMMENT | VARCHAR2(50) | User specified comment |
| NETWORK_NAME | VARCHAR2(512) | Network name |
| SHARDED | VARCHAR2(5) | TRUE if queue is sharded, FALSE otherwise |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content DBA_QUEUES describes all queues in the database. USER_QUEUES describes the operational characteristics of every queue owned by the current user. This view does not display the OWNER column. See Also: " DBA_QUEUES " " USER_QUEUES " Oracle Database Advanced Queuing User's Guide for more information Advanced Queuing See Also: " DBA_QUEUES " " USER_QUEUES " Oracle Database Advanced Queuing User's Guide for more information Advanced Queuing