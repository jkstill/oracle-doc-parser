---
id: 19c__V$CON_SYS_TIME_MODEL
name: V$CON_SYS_TIME_MODEL
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: internal
tags: [dynamic_performance]
source_file: V-CON_SYS_TIME_MODEL.html
---

# V$CON_SYS_TIME_MODEL

V$CON_SYS_TIME_MODEL displays the systemwide accumulated times for various operations for the container from which it is queried.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| STAT_ID | NUMBER |  |
| STAT_NAME | VARCHAR2(64) |  |
| VALUE | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content The time reported is the total elapsed or CPU time (in microseconds). Any timed operation will buffer at most 5 seconds of time data. Specifically, this means that if a timed operation (such as SQL execution) takes a long period of time to perform, the data published to this view is at most missing 5 seconds of the time accumulated for the operation. The time values are 8-byte integers and can therefore hold approximately 580,000 years worth of time before wrapping. Background process time is not included in a statistic value unless the statistic is specifically for background processes.