---
id: 19c__DBA_ADDM_FDG_BREAKDOWN
name: DBA_ADDM_FDG_BREAKDOWN
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_ADDM_FDG_BREAKDOWN.html
---

# DBA_ADDM_FDG_BREAKDOWN

DBA_ADDM_FDG_BREAKDOWN describes the contribution for each finding from the different instances.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TASK_ID | NUMBER | Identifies the task to which this finding belongs (see DBA_ADVISOR_TASKS) |
| FINDING_ID | NUMBER | Identifies the finding (see DBA_ADVISOR_FINDINGS ) |
| INSTANCE_NUMBER | NUMBER | The number of the instance contributing to the finding |
| DATABASE_TIME | NUMBER | The database time, in microseconds, accumulated by this instance during the analysis period |
| ACTIVE_SESSIONS | NUMBER | The average number of active sessions of the finding in this instance |
| PERC_ACTIVE_SESSIONS | NUMBER | The percentage of contribution from this instance compared to the total impact of the finding |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content There is one row for each finding and for each instance participating in the analysis. Rows are omitted if the impact from that instance is not sufficient to register a finding in a local ADDM analysis. Related View USER_ADDM_FDG_BREAKDOWN describes the contribution for each finding from the different instances owned by the current user. See Also: " USER_ADDM_FDG_BREAKDOWN "