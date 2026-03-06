---
id: 19c__V$SESSION_EVENT
name: V$SESSION_EVENT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-SESSION_EVENT.html
---

# V$SESSION_EVENT

Name of the wait event; derived statistic name from V$EVENT_NAME

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SID | NUMBER |  |
| EVENT | VARCHAR2(64) |  |
| TOTAL_WAITS | NUMBER |  |
| TOTAL_TIMEOUTS | NUMBER |  |
| TIME_WAITED | NUMBER |  |
| AVERAGE_WAIT | NUMBER |  |
| MAX_WAIT | NUMBER |  |
| TIME_WAITED_MICRO | NUMBER |  |
| EVENT_ID | NUMBER |  |
| WAIT_CLASS_ID | NUMBER |  |
| WAIT_CLASS# | NUMBER |  |
| WAIT_CLASS | VARCHAR2(64) |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: " TIMED_STATISTICS " See Also: " TIMED_STATISTICS "