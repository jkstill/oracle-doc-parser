---
id: 19c__ALL_STREAMS_MESSAGE_CONSUMERS
name: ALL_STREAMS_MESSAGE_CONSUMERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_STREAMS_MESSAGE_CONSUMERS.html
---

# ALL_STREAMS_MESSAGE_CONSUMERS

ALL_STREAMS_MESSAGE_CONSUMERS displays information about the Replication messaging clients accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| STREAMS_NAME | VARCHAR2(128) | Name of the messaging client |
| QUEUE_NAME | VARCHAR2(128) | Name of the queue |
| QUEUE_OWNER | VARCHAR2(128) | Owner of the queue |
| RULE_SET_NAME | VARCHAR2(128) | Name of the positive rule set |
| RULE_SET_OWNER | VARCHAR2(128) | Owner of the positive rule set |
| NEGATIVE_RULE_SET_NAME | VARCHAR2(128) | Name of the negative rule set |
| NEGATIVE_RULE_SET_OWNER | VARCHAR2(128) | Owner of the negative rule set |
| NOTIFICATION_TYPE | VARCHAR2(9) | Type of the notification action: PROCEDURE MAIL HTTP |
| NOTIFICATION_ACTION | VARCHAR2(256) | Notification action |
| NOTIFICATION_CONTEXT | ANYDATA | Context for the notification action |

## Usage Notes

Related View DBA_STREAMS_MESSAGE_CONSUMERS displays information about all Replication messaging clients in the database. See Also: " DBA_STREAMS_MESSAGE_CONSUMERS " See Also: " DBA_STREAMS_MESSAGE_CONSUMERS "