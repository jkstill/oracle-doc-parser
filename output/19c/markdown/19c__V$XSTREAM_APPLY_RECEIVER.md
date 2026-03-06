---
id: 19c__V$XSTREAM_APPLY_RECEIVER
name: V$XSTREAM_APPLY_RECEIVER
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-XSTREAM_APPLY_RECEIVER.html
---

# V$XSTREAM_APPLY_RECEIVER

Session ID of the apply receiver

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
| STATE | VARCHAR2(44) |  |
| LAST_RECEIVED_MSG_POSITION | RAW(64) |  |
| ACKNOWLEDGEMENT_POSITION | RAW(64) |  |
| CON_ID | NUMBER |  |