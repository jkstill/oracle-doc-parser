---
id: 19c__DBA_TSM_DESTINATION
name: DBA_TSM_DESTINATION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_TSM_DESTINATION.html
---

# DBA_TSM_DESTINATION

DBA_TSM_DESTINATION lists transparent session migration (TSM) destination session statistics.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SOURCE_DATABASE_NAME | VARCHAR2(4000) | Database name of source session |
| DESTINATION_DATABASE_NAME | VARCHAR2(4000) | Database name of destination session |
| DESTINATION_INSTANCE_NAME | VARCHAR2(4000) | Instance name of destination session |
| DESTINATION_INSTANCE_ID | VARCHAR2(4000) | Instance ID of destination session |
| DESTINATION_INST_START_TIME | TIMESTAMP(6) WITH TIME ZONE | Instance start time of destination session |
| SEQUENCE# | NUMBER | Migration sequence number |
| DESTINATION_SID | NUMBER | Session ID of destination session |
| DESTINATION_SERIAL# | NUMBER | Session serial number of destination session |
| DESTINATION_START_TIME | TIMESTAMP(6) WITH TIME ZONE | Start time for migration on destination session |
| DESTINATION_END_TIME | TIMESTAMP(6) WITH TIME ZONE | End time for migration on destination session |
| DESTINATION_USER_NAME | VARCHAR2(128) | User associated with the destination session |
| DESTINATION_SCHEMA_NAME | VARCHAR2(128) | Schema associated with the destination session |
| DESTINATION_STATE | VARCHAR2(24) | Migration state of destination session |