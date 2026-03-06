---
id: 19c__V$SERVICE_EVENT
name: V$SERVICE_EVENT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-SERVICE_EVENT.html
---

# V$SERVICE_EVENT

V$SERVICE_EVENT displays aggregated wait counts and wait times for each wait statistic.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SERVICE_NAME | VARCHAR2(64) |  |
| SERVICE_NAME_HASH | NUMBER |  |
| EVENT | VARCHAR2(64) |  |
| EVENT_ID | NUMBER |  |
| TOTAL_WAITS | NUMBER |  |
| TOTAL_TIMEOUTS | NUMBER |  |
| TIME_WAITED | NUMBER |  |
| AVERAGE_WAIT | NUMBER |  |
| MAX_WAIT | NUMBER |  |
| TIME_WAITED_MICRO | NUMBER |  |
| CON_ID | NUMBER |  |