---
id: 19c__V$GCR_ACTIONS
name: V$GCR_ACTIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-GCR_ACTIONS.html
---

# V$GCR_ACTIONS

V$GCR_ACTIONS displays information about the current status of the actions defined to the GCR component that runs under the LMHB background process to detect and mitigate potential issues in the cluster instances.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ACTION_ID | NUMBER |  |
| ACTION_NAME | VARCHAR2(40) |  |
| ENVIRONMENT | NUMBER |  |
| FLAGS | NUMBER |  |
| ACTIVE | VARCHAR2(9) |  |
| STATUS_CHANGE_TIME | TIMESTAMP(6) |  |
| LAST_RAN_ITERATION | NUMBER |  |
| LAST_RAN_TIME | TIMESTAMP(6) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content