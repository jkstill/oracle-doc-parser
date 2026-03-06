---
id: 19c__V$PQ_SLAVE
name: V$PQ_SLAVE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-PQ_SLAVE.html
---

# V$PQ_SLAVE

V$PQ_SLAVE lists statistics for each of the active parallel execution servers on an instance.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SLAVE_NAME | VARCHAR2(4) |  |
| STATUS | VARCHAR2(4) |  |
| SESSIONS | NUMBER |  |
| IDLE_TIME_CUR | NUMBER |  |
| BUSY_TIME_CUR | NUMBER |  |
| CPU_SECS_CUR | NUMBER |  |
| MSGS_SENT_CUR | NUMBER |  |
| MSGS_RCVD_CUR | NUMBER |  |
| IDLE_TIME_TOTAL | NUMBER |  |
| BUSY_TIME_TOTAL | NUMBER |  |
| CPU_SECS_TOTAL | NUMBER |  |
| MSGS_SENT_TOTAL | NUMBER |  |
| MSGS_RCVD_TOTAL | NUMBER |  |
| CON_ID | NUMBER |  |