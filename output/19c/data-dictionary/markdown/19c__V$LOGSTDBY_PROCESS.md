---
id: 19c__V$LOGSTDBY_PROCESS
name: V$LOGSTDBY_PROCESS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-LOGSTDBY_PROCESS.html
---

# V$LOGSTDBY_PROCESS

V$LOGSTDBY_PROCESS displays dynamic information about what is happening to the Data Guard log apply services.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SID | NUMBER |  |
| SERIAL# | NUMBER |  |
| LOGSTDBY_ID | NUMBER |  |
| SPID | VARCHAR2(24) |  |
| TYPE | VARCHAR2(128) |  |
| STATUS_CODE | NUMBER |  |
| STATUS | VARCHAR2(256) |  |
| HIGH_SCN | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view is helpful when diagnosing performance problems during the logical application of archived redo logs to the standby database, and it can be helpful for other problems. This view is for logical standby databases only.