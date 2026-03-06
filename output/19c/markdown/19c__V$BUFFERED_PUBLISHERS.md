---
id: 19c__V$BUFFERED_PUBLISHERS
name: V$BUFFERED_PUBLISHERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-BUFFERED_PUBLISHERS.html
---

# V$BUFFERED_PUBLISHERS

V$BUFFERED_PUBLISHERS displays information about all buffered publishers in the instance.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| QUEUE_ID | NUMBER |  |
| QUEUE_SCHEMA | VARCHAR2(128) |  |
| QUEUE_NAME | VARCHAR2(128) |  |
| SENDER_NAME | VARCHAR2(128) |  |
| SENDER_ADDRESS | VARCHAR2(1024) |  |
| SENDER_PROTOCOL | NUMBER |  |
| NUM_MSGS | NUMBER |  |
| CNUM_MSGS | NUMBER |  |
| LAST_ENQUEUED_MSG | NUMBER |  |
| UNBROWSED_MSGS | NUMBER |  |
| OVERSPILLED_MSGS | NUMBER |  |
| MEMORY_USAGE | NUMBER |  |
| ELAPSED_ENQUEUE_TIME | NUMBER |  |
| ENQUEUE_CPU_TIME | NUMBER |  |
| LAST_ENQUEUE_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| PUBLISHER_STATE | VARCHAR2(59) |  |
| CON_ID | NUMBER |  |

## Usage Notes

There is one row per queue per sender. The values are reset to zero when the database (or instance in an Oracle RAC environment) restarts.