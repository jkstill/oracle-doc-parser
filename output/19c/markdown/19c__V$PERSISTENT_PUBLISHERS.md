---
id: 19c__V$PERSISTENT_PUBLISHERS
name: V$PERSISTENT_PUBLISHERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-PERSISTENT_PUBLISHERS.html
---

# V$PERSISTENT_PUBLISHERS

Identifier for the queue

## Columns

| Column | Type | Description |
|--------|------|-------------|
| QUEUE_ID | NUMBER |  |
| QUEUE_SCHEMA | VARCHAR2(128) |  |
| QUEUE_NAME | VARCHAR2(128) |  |
| PUBLISHER_NAME | VARCHAR2(128) |  |
| PUBLISHER_ADDRESS | VARCHAR2(1024) |  |
| PROTOCOL | NUMBER |  |
| ENQUEUED_MSGS | NUMBER |  |
| ELAPSED_ENQUEUE_TIME | NUMBER |  |
| ENQUEUE_CPU_TIME | NUMBER |  |
| LAST_ENQUEUE_TIME | TIMESTAMP(6) |  |
| ENQUEUE_TRANSACTIONS | NUMBER |  |
| CON_ID | NUMBER |  |