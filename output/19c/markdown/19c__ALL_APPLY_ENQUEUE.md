---
id: 19c__ALL_APPLY_ENQUEUE
name: ALL_APPLY_ENQUEUE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_APPLY_ENQUEUE.html
---

# ALL_APPLY_ENQUEUE

ALL_APPLY_ENQUEUE displays information about the apply enqueue actions for the rules where the destination queue exists and is accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RULE_OWNER | VARCHAR2(128) | Owner of the rule |
| RULE_NAME | VARCHAR2(128) | Name of the rule |
| DESTINATION_QUEUE_NAME | VARCHAR2(4000) | Name of the queue where events satisfying the rule will be enqueued |

## Usage Notes

Related View DBA_APPLY_ENQUEUE displays information about the apply enqueue actions for all rules in the database. See Also: " DBA_APPLY_ENQUEUE " See Also: " DBA_APPLY_ENQUEUE "