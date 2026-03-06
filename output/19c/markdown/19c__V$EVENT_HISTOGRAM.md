---
id: 19c__V$EVENT_HISTOGRAM
name: V$EVENT_HISTOGRAM
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-EVENT_HISTOGRAM.html
---

# V$EVENT_HISTOGRAM

V$EVENT_HISTOGRAM displays a histogram of the number of waits, the maximum wait, and total wait time on an event basis, in milliseconds. The histogram has buckets of time intervals from < 1 ms, < 2 ms, < 4 ms, < 8 ms, ... < 2 21 ms, < 2 22 ms, and >= 2 22 ms.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| EVENT# | NUMBER |  |
| EVENT | VARCHAR2(64) |  |
| WAIT_TIME_MILLI | NUMBER |  |
| WAIT_COUNT | NUMBER |  |
| LAST_UPDATE_TIME | VARCHAR2(64) |  |
| CON_ID | NUMBER |  |

## Usage Notes

The histogram will not be filled unless the TIMED_STATISTICS initialization parameter is set to true . See Also: " TIMED_STATISTICS " See Also: " TIMED_STATISTICS "