---
id: 19c__ALL_SYNC_CAPTURE
name: ALL_SYNC_CAPTURE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_SYNC_CAPTURE.html
---

# ALL_SYNC_CAPTURE

ALL_SYNC_CAPTURE displays information about the synchronous capture processes that store the captured changes in queues accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CAPTURE_NAME | VARCHAR2(128) | Name of the capture process |
| QUEUE_NAME | VARCHAR2(128) | Name of the queue used for holding captured changes |
| QUEUE_OWNER | VARCHAR2(128) | Owner of the queue used for holding captured changes |
| RULE_SET_NAME | VARCHAR2(128) | Rule set used by the capture process |
| RULE_SET_OWNER | VARCHAR2(128) | Owner of the rule set |
| CAPTURE_USER | VARCHAR2(128) | Current user who is enqueuing captured messages |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View DBA_SYNC_CAPTURE displays information about all synchronous capture processes in the database. See Also: " DBA_SYNC_CAPTURE " See Also: " DBA_SYNC_CAPTURE "