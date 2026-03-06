---
id: 19c__ALL_QUEUE_SUBSCRIBERS
name: ALL_QUEUE_SUBSCRIBERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_QUEUE_SUBSCRIBERS.html
---

# ALL_QUEUE_SUBSCRIBERS

ALL_QUEUE_SUBSCRIBERS displays the list of subscribers that the current user has privilege to dequeue from.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the queue |
| QUEUE_NAME | VARCHAR2(128) | Name of the queue |
| QUEUE_TABLE | VARCHAR2(128) | Name of the queue table on which the queue is defined |
| CONSUMER_NAME | VARCHAR2(512) | Name of the subscriber |
| ADDRESS | VARCHAR2(1024) | Address of the subscriber |
| PROTOCOL | NUMBER | Protocol of the subscriber |
| TRANSFORMATION | VARCHAR2(61) | Transformation for the subscriber |
| RULE | CLOB | Rule condition for the subscriber |
| DELIVERY_MODE | VARCHAR2(22) | Message delivery mode for the subscriber: PERSISTENT BUFFERED PERSISTENT_OR_BUFFERED |
| IF_NONDURABLE_SUBSCRIBER | VARCHAR2(3) | Indicates whether the subscriber is a non-durable subscriber ( YES ) or not ( NO ) |
| QUEUE_TO_QUEUE | VARCHAR2(5) | Indicates whether the subscriber is a queue-to-queue subscriber ( TRUE ) or not ( FALSE ) |
| SUBSCRIBER_ID | NUMBER | ID of the subscriber |
| POS_BITMAP | NUMBER | Position of the subscriber in the bitmap |

## Usage Notes

Related Views DBA_QUEUE_SUBSCRIBERS displays the list of subscribers on all queues in the database. USER_QUEUE_SUBSCRIBERS displays the list of subscribers on queues that are under the current user's schema. This view does not display the OWNER column. See Also: " DBA_QUEUE_SUBSCRIBERS " " USER_QUEUE_SUBSCRIBERS " See Also: " DBA_QUEUE_SUBSCRIBERS " " USER_QUEUE_SUBSCRIBERS "