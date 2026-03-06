---
id: 19c__DBA_TSM_SOURCE
name: DBA_TSM_SOURCE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_TSM_SOURCE.html
---

# DBA_TSM_SOURCE

DBA_TSM_SOURCE lists transparent session migration (TSM) source session statistics.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SOURCE_DATABASE_NAME | VARCHAR2(4000) | Database name of source session |
| SOURCE_INSTANCE_NAME | VARCHAR2(4000) | Instance name of source session |
| SOURCE_INSTANCE_ID | VARCHAR2(4000) | Instance ID of source session |
| SOURCE_INSTANCE_START_TIME | TIMESTAMP(6) WITH TIME ZONE | Instance start time of source session |
| SEQUENCE# | NUMBER | Migration sequence number |
| SOURCE_SID | NUMBER | Session ID of source session |
| SOURCE_SERIAL# | NUMBER | Source serial number of source session |
| SOURCE_STATE | VARCHAR2(24) | Migration state of source session |
| CONNECT_STRING | VARCHAR2(4000) | Connect string specified for migration |
| SOURCE_START_TIME | TIMESTAMP(6) WITH TIME ZONE | Start time for migration on source session |
| COST | NUMBER | Estimate of migration cost |
| FAILURE_REASON | VARCHAR2(34) | Reason for migration failure, if any |
| SOURCE_END_TIME | TIMESTAMP(6) WITH TIME ZONE | End time for migration on source session |
| ROUNDTRIPS | NUMBER | Number of client/server round trips during migration |
| SOURCE_USER_NAME | VARCHAR2(128) | User associated with the source session |
| SOURCE_SCHEMA_NAME | VARCHAR2(128) | Schema associated with the source session |
| DESTINATION_DATABASE_NAME | VARCHAR2(4000) | Database name of the destination session |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content