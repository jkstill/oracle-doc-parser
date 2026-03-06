---
id: 19c__DBA_WORKLOAD_GROUP_ASSIGNMENTS
name: DBA_WORKLOAD_GROUP_ASSIGNMENTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_WORKLOAD_GROUP_ASSIGNMENTS.html
---

# DBA_WORKLOAD_GROUP_ASSIGNMENTS

DBA_WORKLOAD_GROUP_ASSIGNMENTS displays all the workload capture groups and their assigned instances. A workload capture group is a subset of the captured workload. Each group accesses its own set of recorded database objects.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| REPLAY_DIR_NUMBER | NUMBER(38) | The value that is associated with the subdirectory under the replay directory. See REPLAY_DIR_NUMBER in DBA_WORKLOAD_REPLAYS . |
| GROUP_ID | NUMBER(38) | The identifier of a workload capture group |
| INSTANCE_NUMBER | NUMBER(38) | The instance a given group is assigned to |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: " DBA_WORKLOAD_REPLAYS " See Also: " DBA_WORKLOAD_REPLAYS "