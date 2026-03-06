---
id: 19c__DBA_STREAMS_TP_COMPONENT_LINK
name: DBA_STREAMS_TP_COMPONENT_LINK
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_STREAMS_TP_COMPONENT_LINK.html
---

# DBA_STREAMS_TP_COMPONENT_LINK

DBA_STREAMS_TP_COMPONENT_LINK displays information about how messages flow between Replication components.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SOURCE_COMPONENT_ID | NUMBER | ID of the source Replication component |
| SOURCE_COMPONENT_NAME | VARCHAR2(4000) | Name of the source Replication component |
| SOURCE_COMPONENT_DB | VARCHAR2(128) | Database where the source Replication component resides |
| SOURCE_COMPONENT_TYPE | VARCHAR2(20) | Type of the source Replication component: CAPTURE PROPAGATION SENDER PROPAGATION RECEIVER APPLY QUEUE |
| DESTINATION_COMPONENT_ID | NUMBER | ID of the destination Replication component |
| DESTINATION_COMPONENT_NAME | VARCHAR2(4000) | Name of the destination Replication component |
| DESTINATION_COMPONENT_DB | VARCHAR2(128) | Database where the destination Replication component resides |
| DESTINATION_COMPONENT_TYPE | VARCHAR2(20) | Type of the destination Replication component: CAPTURE PROPAGATION SENDER PROPAGATION RECEIVER APPLY QUEUE |
| PATH_ID | NUMBER | ID of the stream path |
| POSITION | NUMBER | Position of the link within the stream path |