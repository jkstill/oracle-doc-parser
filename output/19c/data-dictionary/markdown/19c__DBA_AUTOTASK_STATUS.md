---
id: 19c__DBA_AUTOTASK_STATUS
name: DBA_AUTOTASK_STATUS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_AUTOTASK_STATUS.html
---

# DBA_AUTOTASK_STATUS

DBA_AUTOTASK_STATUS displays status information for automated maintenance.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| STATUS | VARCHAR2(8) | Shows the status of automated maintenance. Possible values are: ENABLED DISABLED ALLOWED INVALID |
| LAST_CHANGE | TIMESTAMP(6) WITH TIME ZONE | Timestamp of last status change |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content