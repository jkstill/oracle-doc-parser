---
id: 19c__V$PROPAGATION_RECEIVER
name: V$PROPAGATION_RECEIVER
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-PROPAGATION_RECEIVER.html
---

# V$PROPAGATION_RECEIVER

Name of the source schema

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SRC_QUEUE_SCHEMA | VARCHAR2(128) |  |
| SRC_QUEUE_NAME | VARCHAR2(128) |  |
| SRC_DBNAME | VARCHAR2(395) |  |
| DST_QUEUE_SCHEMA | VARCHAR2(128) |  |
| DST_QUEUE_NAME | VARCHAR2(128) |  |
| STARTUP_TIME | DATE |  |
| HIGH_WATER_MARK | NUMBER |  |
| ACKNOWLEDGEMENT | NUMBER |  |
| LAST_RECEIVED_MSG | NUMBER |  |
| TOTAL_MSGS | NUMBER |  |
| ELAPSED_UNPICKLE_TIME | NUMBER |  |
| ELAPSED_RULE_TIME | NUMBER |  |
| ELAPSED_ENQUEUE_TIME | NUMBER |  |
| SESSION_ID | NUMBER |  |
| SERIAL# | NUMBER |  |
| SPID | VARCHAR2(24) |  |
| PROPAGATION_NAME | VARCHAR2(128) |  |
| STATE | VARCHAR2(43) |  |
| LAST_RECEIVED_MSG_POSITION | RAW(64) |  |
| ACKNOWLEDGEMENT_POSITION | RAW(64) |  |
| CON_ID | NUMBER |  |