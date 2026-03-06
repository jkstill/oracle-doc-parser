---
id: 19c__V$QUEUE
name: V$QUEUE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-QUEUE.html
---

# V$QUEUE

V$QUEUE contains information on the shared server message queues.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PADDR | RAW(4 | 8) |  |
| TYPE | VARCHAR2(10) |  |
| QUEUED | NUMBER |  |
| WAIT | NUMBER |  |
| TOTALQ | NUMBER |  |
| CON_ID | NUMBER |  |