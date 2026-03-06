---
id: 19c__DBA_STREAMS_TP_COMPONENT_STAT
name: DBA_STREAMS_TP_COMPONENT_STAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_STREAMS_TP_COMPONENT_STAT.html
---

# DBA_STREAMS_TP_COMPONENT_STAT

DBA_STREAMS_TP_COMPONENT_STAT displays temporary performance statistics and session statistics about each Replication component.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| COMPONENT_ID | NUMBER | ID of the Replication component |
| COMPONENT_NAME | VARCHAR2(4000) | Name of the Replication component |
| COMPONENT_DB | VARCHAR2(128) | Database where the Replication component resides |
| COMPONENT_TYPE | VARCHAR2(20) | Type of the Replication component: CAPTURE PROPAGATION SENDER PROPAGATION RECEIVER APPLY QUEUE |
| SUB_COMPONENT_TYPE | VARCHAR2(27) | Type of the Replication subcomponent: LOGMINER READER LOGMINER PREPARER LOGMINER BUILDER CAPTURE SESSION PROPAGATION SENDER+RECEIVER APPLY READER APPLY COORDINATOR APPLY SERVER |
| SESSION_ID | NUMBER | ID of the Replication session for the Replication component |
| SESSION_SERIAL# | NUMBER | Serial number of the Replication session for the Replication component |
| STATISTIC_TIME | DATE | Time that the statistic was taken |
| STATISTIC_NAME | VARCHAR2(64) | Name of the statistic |
| STATISTIC_VALUE | VARCHAR2(4000) | Value of the statistic |
| STATISTIC_UNIT | VARCHAR2(64) | Unit of the statistic |
| ADVISOR_RUN_ID | NUMBER | Logical number (1-based) of the Advisor run |
| ADVISOR_RUN_TIME | DATE | Time that the Advisor was run |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content