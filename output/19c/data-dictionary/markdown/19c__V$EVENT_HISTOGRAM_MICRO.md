---
id: 19c__V$EVENT_HISTOGRAM_MICRO
name: V$EVENT_HISTOGRAM_MICRO
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-EVENT_HISTOGRAM_MICRO.html
---

# V$EVENT_HISTOGRAM_MICRO

V$EVENT_HISTOGRAM_MICRO displays a histogram of the number of waits, the maximum wait, and total wait time on an event basis, in microseconds. The histogram has buckets of time intervals from < 1 us, < 2 us, < 4 us, < 8 us, ... < 2 31 us, < 2 32 us, and >= 2 32 us.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| EVENT# | NUMBER |  |
| EVENT | VARCHAR2(64) |  |
| WAIT_TIME_FORMAT | VARCHAR2(30) |  |
| WAIT_TIME_MICRO | NUMBER |  |
| WAIT_COUNT | NUMBER |  |
| LAST_UPDATE_TIME | VARCHAR2(64) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content The histogram will not be filled unless the TIMED_STATISTICS initialization parameter is set to true .