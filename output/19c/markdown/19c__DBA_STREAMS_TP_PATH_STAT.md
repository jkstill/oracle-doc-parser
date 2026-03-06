---
id: 19c__DBA_STREAMS_TP_PATH_STAT
name: DBA_STREAMS_TP_PATH_STAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_STREAMS_TP_PATH_STAT.html
---

# DBA_STREAMS_TP_PATH_STAT

DBA_STREAMS_TP_PATH_STAT displays temporary performance statistics about each stream path that exists in the Replication topology.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PATH_ID | NUMBER | ID of the stream path |
| STATISTIC_TIME | DATE | Time that the statistic was taken |
| STATISTIC_NAME | VARCHAR2(64) | Name of the statistic |
| STATISTIC_VALUE | NUMBER | Value of the statistic |
| STATISTIC_UNIT | VARCHAR2(64) | Unit of the statistic |
| ADVISOR_RUN_ID | NUMBER | Logical number (1-based) of the Advisor run |
| ADVISOR_RUN_TIME | DATE | Time that the Advisor was run |