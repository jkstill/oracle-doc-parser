---
id: 19c__V$SERV_MOD_ACT_STATS
name: V$SERV_MOD_ACT_STATS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-SERV_MOD_ACT_STATS.html
---

# V$SERV_MOD_ACT_STATS

V$SERV_MOD_ACT_STATS displays the same set of performance statistics as V$SERVICE_STATS except for a specific combination of service/module/action names.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| AGGREGATION_TYPE | VARCHAR2(21) |  |
| SERVICE_NAME | VARCHAR2(64) |  |
| MODULE | VARCHAR2(65) |  |
| ACTION | VARCHAR2(65) |  |
| STAT_ID | NUMBER |  |
| STAT_NAME | VARCHAR2(64) |  |
| VALUE | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

When aggregation is enabled for the service name, module, and action name, then this view provides the timing and work done for calls issued for the business transaction. See Also: " V$SERVICE_STATS " " V$STATNAME " " V$SESS_TIME_MODEL " See Also: " V$SERVICE_STATS " " V$STATNAME " " V$SESS_TIME_MODEL "