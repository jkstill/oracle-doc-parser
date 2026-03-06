---
id: 19c__V$XSTREAM_CAPTURE
name: V$XSTREAM_CAPTURE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-XSTREAM_CAPTURE.html
---

# V$XSTREAM_CAPTURE

V$XSTREAM_CAPTURE displays information about each capture process that sends LCRs to an XStream outbound server.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SID | NUMBER |  |
| SERIAL# | NUMBER |  |
| CAPTURE# | NUMBER |  |
| CAPTURE_NAME | VARCHAR2(128) |  |
| LOGMINER_ID | NUMBER |  |
| STARTUP_TIME | DATE |  |
| STATE | VARCHAR2(551) |  |
| TOTAL_PREFILTER_DISCARDED | NUMBER |  |
| TOTAL_PREFILTER_KEPT | NUMBER |  |
| TOTAL_PREFILTER_EVALUATIONS | NUMBER |  |
| TOTAL_MESSAGES_CAPTURED | NUMBER |  |
| CAPTURE_TIME | DATE |  |
| CAPTURE_MESSAGE_NUMBER | NUMBER |  |
| CAPTURE_MESSAGE_CREATE_TIME | DATE |  |
| TOTAL_MESSAGES_CREATED | NUMBER |  |
| TOTAL_FULL_EVALUATIONS | NUMBER |  |
| TOTAL_MESSAGES_ENQUEUED | NUMBER |  |
| ENQUEUE_TIME | DATE |  |
| ENQUEUE_MESSAGE_NUMBER | NUMBER |  |
| ENQUEUE_MESSAGE_CREATE_TIME | DATE |  |
| AVAILABLE_MESSAGE_NUMBER | NUMBER |  |
| AVAILABLE_MESSAGE_CREATE_TIME | DATE |  |
| ELAPSED_CAPTURE_TIME | NUMBER |  |
| ELAPSED_RULE_TIME | NUMBER |  |
| ELAPSED_ENQUEUE_TIME | NUMBER |  |
| ELAPSED_LCR_TIME | NUMBER |  |
| ELAPSED_REDO_WAIT_TIME | NUMBER |  |
| ELAPSED_PAUSE_TIME | NUMBER |  |
| STATE_CHANGED_TIME | DATE |  |
| SGA_USED | NUMBER |  |
| SGA_ALLOCATED | NUMBER |  |
| BYTES_OF_REDO_MINED | VARCHAR2(64) |  |
| SESSION_RESTART_SCN | VARCHAR2(64) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Note: The ELAPSED_CAPTURE_TIME , ELAPSED_RULE_TIME , ELAPSED_ENQUEUE_TIME , ELAPSED_LCR_TIME , and ELAPSED_REDO_WAIT_TIME columns are only populated if the TIMED_STATISTICS initialization parameter is set to true , or if the STATISTICS_LEVEL initialization parameter is set to TYPICAL or ALL . See Also: " TIMED_STATISTICS " " STATISTICS_LEVEL " Note: The ELAPSED_CAPTURE_TIME , ELAPSED_RULE_TIME , ELAPSED_ENQUEUE_TIME , ELAPSED_LCR_TIME , and ELAPSED_REDO_WAIT_TIME columns are only populated if the TIMED_STATISTICS initialization parameter is set to true , or if the STATISTICS_LEVEL initialization parameter is set to TYPICAL or ALL . See Also: " TIMED_STATISTICS " " STATISTICS_LEVEL "