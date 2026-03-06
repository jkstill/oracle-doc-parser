---
id: 19c__DBA_STREAMS_TP_COMPONENT
name: DBA_STREAMS_TP_COMPONENT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_STREAMS_TP_COMPONENT.html
---

# DBA_STREAMS_TP_COMPONENT

DBA_STREAMS_TP_COMPONENT displays information about each Replication component at each database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| COMPONENT_ID | NUMBER | ID of the Replication component |
| COMPONENT_NAME | VARCHAR2(4000) | Name of the Replication component |
| COMPONENT_DB | VARCHAR2(128) | Database where the Replication component resides |
| COMPONENT_TYPE | VARCHAR2(20) | Type of the Replication component: CAPTURE PROPAGATION SENDER PROPAGATION RECEIVER APPLY QUEUE |
| COMPONENT_CHANGED_TIME | DATE | Time that the Replication component was last changed |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content