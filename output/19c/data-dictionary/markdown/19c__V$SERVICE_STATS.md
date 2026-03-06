---
id: 19c__V$SERVICE_STATS
name: V$SERVICE_STATS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-SERVICE_STATS.html
---

# V$SERVICE_STATS

When aggregation is enabled for the Service Name, then this view provides the timing and work done for calls issued for the whole service.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SERVICE_NAME_HASH | NUMBER |  |
| SERVICE_NAME | VARCHAR2(64) |  |
| STAT_ID | NUMBER |  |
| STAT_NAME | VARCHAR2(64) |  |
| VALUE | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: " V$SERVICES " " V$STATNAME " " V$SESS_TIME_MODEL " Oracle Database Performance Tuning Guide for more information about using database statistics to manage the performance of Oracle Database See Also: " V$SERVICES " " V$STATNAME " " V$SESS_TIME_MODEL " Oracle Database Performance Tuning Guide for more information about using database statistics to manage the performance of Oracle Database