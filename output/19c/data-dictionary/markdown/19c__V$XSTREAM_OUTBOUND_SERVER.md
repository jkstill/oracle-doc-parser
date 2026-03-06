---
id: 19c__V$XSTREAM_OUTBOUND_SERVER
name: V$XSTREAM_OUTBOUND_SERVER
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-XSTREAM_OUTBOUND_SERVER.html
---

# V$XSTREAM_OUTBOUND_SERVER

V$XSTREAM_OUTBOUND_SERVER displays statistics about an outbound server. An outbound server sends LCRs to the XStream client application.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SID | NUMBER |  |
| SERIAL# | NUMBER |  |
| SPID | VARCHAR2(12) |  |
| SERVER_NAME | VARCHAR2(128) |  |
| STARTUP_TIME | DATE |  |
| STATE | VARCHAR2(19) |  |
| XIDUSN | NUMBER |  |
| XIDSLT | NUMBER |  |
| XIDSQN | NUMBER |  |
| COMMITSCN | NUMBER |  |
| TOTAL_TRANSACTIONS_SENT | NUMBER |  |
| MESSAGE_SEQUENCE | NUMBER |  |
| TOTAL_MESSAGES_SENT | NUMBER |  |
| SEND_TIME | DATE |  |
| LAST_SENT_MESSAGE_NUMBER | NUMBER |  |
| LAST_SENT_MESSAGE_CREATE_TIME | DATE |  |
| ELAPSED_SEND_TIME | NUMBER |  |
| COMMIT_POSITION | RAW(64) |  |
| LAST_SENT_POSITION | RAW(64) |  |
| BYTES_SENT | NUMBER |  |
| COMMITTED_DATA_ONLY | CHAR(3) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: When the COMMITTED_DATA_ONLY column is YES in the V$XSTREAM_OUTBOUND_SERVER view, the V$STREAMS_APPLY_SERVER view provides additional information about the outbound server process, and information about the apply server background processes used by the outbound server. Note: When the COMMITTED_DATA_ONLY column is YES in the V$XSTREAM_OUTBOUND_SERVER view, the V$STREAMS_APPLY_SERVER view provides additional information about the outbound server process, and information about the apply server background processes used by the outbound server. See Also: " V$STREAMS_APPLY_SERVER " See Also: " V$STREAMS_APPLY_SERVER "