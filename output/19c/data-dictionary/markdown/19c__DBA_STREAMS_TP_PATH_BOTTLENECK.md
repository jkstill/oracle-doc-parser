---
id: 19c__DBA_STREAMS_TP_PATH_BOTTLENECK
name: DBA_STREAMS_TP_PATH_BOTTLENECK
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_STREAMS_TP_PATH_BOTTLENECK.html
---

# DBA_STREAMS_TP_PATH_BOTTLENECK

DBA_STREAMS_TP_PATH_BOTTLENECK displays temporary information about Replication components that might be slowing down the flow of messages in a stream path.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PATH_ID | NUMBER | ID of the stream path |
| COMPONENT_ID | NUMBER | ID of the bottleneck component |
| COMPONENT_NAME | VARCHAR2(4000) | Name of the bottleneck component |
| COMPONENT_DB | VARCHAR2(128) | Database where the bottleneck component resides |
| COMPONENT_TYPE | VARCHAR2(20) | Type of the bottleneck component: CAPTURE PROPAGATION SENDER PROPAGATION RECEIVER APPLY QUEUE |
| TOP_SESSION_ID | NUMBER | ID of the top session for the bottleneck component |
| TOP_SESSION_SERIAL# | NUMBER | Serial number of the top session for the bottleneck component |
| ACTION_NAME | VARCHAR2(64) | Action name for the bottleneck process |
| BOTTLENECK_IDENTIFIED | VARCHAR2(30) | Indicates whether the bottleneck was identified ( YES ) or not ( NO ) |
| ADVISOR_RUN_ID | NUMBER | Logical number (1-based) of the Advisor run |
| ADVISOR_RUN_TIME | DATE | Time that the Advisor was run |
| ADVISOR_RUN_REASON | VARCHAR2(4000) | Reason for the bottleneck analysis result.: NULL - Bottleneck is identified PRE-11.1 DATABASE EXISTS - A pre-release 11.1 database exists in the stream path DIAGNOSTIC PACK REQUIRED - A database in the stream path does not have the diagnostic package installed NO BOTTLENECK IDENTIFIED |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content