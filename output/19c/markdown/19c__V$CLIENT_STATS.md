---
id: 19c__V$CLIENT_STATS
name: V$CLIENT_STATS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-CLIENT_STATS.html
---

# V$CLIENT_STATS

V$CLIENT_STATS displays measures for all sessions that are active for the client identifier per instance.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CLIENT_IDENTIFIER | VARCHAR2(64) |  |
| STAT_ID | NUMBER |  |
| STAT_NAME | VARCHAR2(64) |  |
| VALUE | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

The statistics available in this view are a subset of those available in V$SESSTAT and V$SESS_TIME_MODEL . See Also: " V$SESSTAT " " V$SESS_TIME_MODEL " See Also: " V$SESSTAT " " V$SESS_TIME_MODEL "