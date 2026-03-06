---
id: 19c__V$LOGSTDBY_STATE
name: V$LOGSTDBY_STATE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-LOGSTDBY_STATE.html
---

# V$LOGSTDBY_STATE

V$LOGSTDBY_STATE provides consolidated information from V$LOGSTDBY and V$LOGSTDBY_STATS about the running state of Logical Standby.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PRIMARY_DBID | NUMBER |  |
| PRIMARY_CON_DBID | NUMBER |  |
| SESSION_ID | NUMBER |  |
| REALTIME_APPLY | VARCHAR2(64) |  |
| STATE | VARCHAR2(64) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: " V$LOGSTDBY " " V$LOGSTDBY_STATS " See Also: " V$LOGSTDBY " " V$LOGSTDBY_STATS "