---
id: 19c__ALL_DEQUEUE_QUEUES
name: ALL_DEQUEUE_QUEUES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_DEQUEUE_QUEUES.html
---

# ALL_DEQUEUE_QUEUES

OWNER

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the queue |
| NAME | VARCHAR2(128) | Name of the queue |
| QUEUE_TABLE | VARCHAR2(128) | Name of the table in which the queue data resides |
| QID | NUMBER | Object number of the queue |
| QUEUE_TYPE | VARCHAR2(20) | Type of the queue: EXCEPTION_QUEUE NORMAL_QUEUE |
| MAX_RETRIES | NUMBER | Maximum number of retries allowed when dequeuing from the queue |
| RETRY_DELAY | NUMBER | Time interval between retries |
| ENQUEUE_ENABLED | VARCHAR2(7) | Indicates whether the queue is enabled for enqueue ( YES ) or not ( NO ) |
| DEQUEUE_ENABLED | VARCHAR2(7) | Indicates whether the queue is enabled for dequeue ( YES ) or not ( NO ) |
| RETENTION | VARCHAR2(40) | Time interval that processed messages are retained in the queue, or FOREVER |
| USER_COMMENT | VARCHAR2(50) | User-specified comment |
| NETWORK_NAME | VARCHAR2(512) | Network name of the queue service |
| SHARDED | VARCHAR2(5) | TRUE if the queue is sharded, FALSE otherwise |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content