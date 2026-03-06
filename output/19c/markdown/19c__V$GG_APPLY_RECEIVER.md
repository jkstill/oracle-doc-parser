---
id: 19c__V$GG_APPLY_RECEIVER
name: V$GG_APPLY_RECEIVER
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-GG_APPLY_RECEIVER.html
---

# V$GG_APPLY_RECEIVER

V$GG_APPLY_RECEIVER displays information about the message receiver of the Replicat process.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SID | NUMBER |  |
| SERIAL# | NUMBER |  |
| APPLY_NAME | VARCHAR2(128) |  |
| STARTUP_TIME | DATE |  |
| SOURCE_DATABASE_NAME | VARCHAR2(128) |  |
| ACKNOWLEDGEMENT | NUMBER |  |
| LAST_RECEIVED_MSG | NUMBER |  |
| TOTAL_MESSAGES_RECEIVED | NUMBER |  |
| TOTAL_AVAILABLE_MESSAGES | NUMBER |  |
| STATE | VARCHAR2(46) |  |
| LAST_RECEIVED_MSG_POSITION | VARCHAR2(64) |  |
| ACKNOWLEDGEMENT_POSITION | VARCHAR2(64) |  |
| CON_ID | NUMBER |  |
| OS_PROCESS_ID Foot 1 | VARCHAR2(12) |  |
| CURRENT_POSITION Foot 1 | VARCHAR2(81) |  |
| TOTAL_TRANSACTIONS Foot 1 | NUMBER |  |
| TOTAL_COMMITS Foot 1 | NUMBER |  |
| TOTAL_ERRORS Foot 1 | NUMBER |  |

## Usage Notes

The values are reset to zero when the database (or instance in an Oracle Real Application Clusters (Oracle RAC) environment) restarts and when the Replicat process is stopped.