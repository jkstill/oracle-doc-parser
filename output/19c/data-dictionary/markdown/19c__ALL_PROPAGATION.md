---
id: 19c__ALL_PROPAGATION
name: ALL_PROPAGATION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_PROPAGATION.html
---

# ALL_PROPAGATION

ALL_PROPAGATION displays information about the propagations that have a source queue accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PROPAGATION_NAME | VARCHAR2(128) | Name of the propagation |
| SOURCE_QUEUE_OWNER | VARCHAR2(128) | Owner of the source queue of the propagation |
| SOURCE_QUEUE_NAME | VARCHAR2(128) | Name of the source queue of the propagation |
| DESTINATION_QUEUE_OWNER | VARCHAR2(128) | Owner of the destination queue of the propagation |
| DESTINATION_QUEUE_NAME | VARCHAR2(128) | Name of the destination queue of the propagation |
| DESTINATION_DBLINK | VARCHAR2(128) | Database link to propagate events from the source queue to the destination queue |
| RULE_SET_OWNER | VARCHAR2(128) | Owner of the propagation positive rule set |
| RULE_SET_NAME | VARCHAR2(128) | Name of the propagation positive rule set |
| NEGATIVE_RULE_SET_OWNER | VARCHAR2(128) | Owner of the propagation negative rule set |
| NEGATIVE_RULE_SET_NAME | VARCHAR2(128) | Name of the propagation negative rule set |
| QUEUE_TO_QUEUE | VARCHAR2(5) | Indicates whether the propagation is a queue-to-queue propagation ( TRUE ) or not ( FALSE ). A queue-to-queue propagation always has its own exclusive propagation job to propagate messages from the source queue to the destination queue. |
| STATUS | VARCHAR2(8) | Status of the propagation: DISABLED ENABLED ABORTED |
| ERROR_MESSAGE | VARCHAR2(4000) | Error message last encountered by propagation |
| ERROR_DATE | DATE | Time that propagation last encountered an error |
| ORIGINAL_PROPAGATION_NAME | VARCHAR2(128) | Original propagation from which the propagation is cloned |
| ORIGINAL_SOURCE_QUEUE_OWNER | VARCHAR2(128) | Source queue owner of the original propagation |
| ORIGINAL_SOURCE_QUEUE_NAME | VARCHAR2(128) | Source queue name of the original propagation |
| ACKED_SCN | NUMBER | Acknowledged SCN of the subscribers of captured messages in the destination queue for the propagation |
| AUTO_MERGE_THRESHOLD | NUMBER | Merge threshold value for merging the propagation back to the original source queue |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View DBA_PROPAGATION displays information about all propagations in the database. See Also: " DBA_PROPAGATION " See Also: " DBA_PROPAGATION "