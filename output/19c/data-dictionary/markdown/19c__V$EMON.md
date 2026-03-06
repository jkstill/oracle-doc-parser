---
id: 19c__V$EMON
name: V$EMON
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-EMON.html
---

# V$EMON

V$EMON displays performance statistics per event monitor (EMON) slave for diagnosability of notifications. All processing time and latency is in seconds.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| EMON# | NUMBER |  |
| SID | NUMBER |  |
| STARTUP_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| SERVER_TYPE | VARCHAR2(8) |  |
| STATUS | VARCHAR2(6) |  |
| STATUS_CHANGE_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| NUM_NTFNS | NUMBER |  |
| NUM_GROUPING_NTFNS | NUMBER |  |
| NUM_NTFNS_ALL_GROUPS | NUMBER |  |
| NUM_OCI_NTFNS | NUMBER |  |
| NUM_PLSQL_NTFNS | NUMBER |  |
| NUM_EMAIL_NTFNS | NUMBER |  |
| NUM_HTTP_NTFNS | NUMBER |  |
| NUM_EVENTS_PROCESSED | NUMBER |  |
| NUM_EVENTS_PENDING | NUMBER |  |
| NUM_ANONYMOUS_NTFNS | NUMBER |  |
| NUM_AQ_NTFNS | NUMBER |  |
| NUM_DBCHANGE_NTFNS | NUMBER |  |
| TOTAL_ANONYMOUS_NTFN_TIME | NUMBER |  |
| TOTAL_AQ_NTFN_TIME | NUMBER |  |
| TOTAL_DBCHANGE_NTFN_TIME | NUMBER |  |
| TOTAL_PLSQL_NTFN_TIME | NUMBER |  |
| TOTAL_OCI_NTFN_TIME | NUMBER |  |
| TOTAL_EMAIL_NTFN_TIME | NUMBER |  |
| TOTAL_HTTP_NTFN_TIME | NUMBER |  |
| TOTAL_EMON_LATENCY | NUMBER |  |
| REGISTRATIONS_EXPIRED | NUMBER |  |
| REGISTRATIONS_PURGED | NUMBER |  |
| REGISTRATIONS_INVALID | NUMBER |  |
| LAST_UPDATE_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content