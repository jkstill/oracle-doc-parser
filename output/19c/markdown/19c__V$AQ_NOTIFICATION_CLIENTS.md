---
id: 19c__V$AQ_NOTIFICATION_CLIENTS
name: V$AQ_NOTIFICATION_CLIENTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-AQ_NOTIFICATION_CLIENTS.html
---

# V$AQ_NOTIFICATION_CLIENTS

V$AQ_NOTIFICATION_CLIENTS displays performance statistics for secure OCI client connections.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CLIENT_ID | VARCHAR2(29) |  |
| EMON_ID | NUMBER |  |
| NOTIFICATION_STATE | NUMBER |  |
| NUM_MESSAGE_SENT | NUMBER |  |
| NUM_BYTES_SENT | NUMBER |  |
| NUM_MESSAGE_RECEIVED | NUMBER |  |
| LAST_SEND_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| LAST_RECEIVE_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| CONNECT_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| DISCONNECT_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| LAST_ERROR | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: Oracle Database Advanced Queuing User's Guide for more information about Oracle Database Advanced Queueing See Also: Oracle Database Advanced Queuing User's Guide for more information about Oracle Database Advanced Queueing