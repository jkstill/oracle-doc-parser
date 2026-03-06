---
id: 19c__DBA_ADDM_INSTANCES
name: DBA_ADDM_INSTANCES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_ADDM_INSTANCES.html
---

# DBA_ADDM_INSTANCES

DBA_ADDM_INSTANCES displays instance-level information for ADDM tasks that finished executing.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TASK_ID | NUMBER | The ID of the main ADDM task |
| INSTANCE_NUMBER | NUMBER | The number of the instance |
| INSTANCE_NAME | VARCHAR2(16) | The name of the instance |
| HOST_NAME | VARCHAR2(64) | The name of the system on which the instance was running |
| STATUS | VARCHAR2(10) | How information from this instance was used by the ADDM task. A value of ANALYZED means that the instance participated fully in the analysis. For the following remaining values, the instance was not used during task execution, for the stated reason: BOUNCED - the instance was shut down or started during the analysis period NO_SNAPS - there were either begin or end snapshots missing for the instance NO_STATS - there were key statistics missing for the instance NOT_FOUND - no mention of this instance could be found in AWR during the analysis period |
| DATABASE_TIME | NUMBER | The database time, in microseconds, accumulated by this instance during the analysis period |
| ACTIVE_SESSIONS | NUMBER | The average number of active sessions for the instance during the analysis period |
| PERC_ACTIVE_SESS | NUMBER | The percentage of active sessions for this instance, out of the total active sessions for the task |
| METER_LEVEL | VARCHAR2(6) | Reserved for future use |
| LOCAL_TASK_ID | NUMBER | The ID of a local ADDM task that contained an analysis of the instance for the same analysis period as that of the main task. If the main task is a local ADDM, then this value is the same as the TASK_ID value. |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content For each instance that was supposed to be analyzed (whether it was or not) there is one row describing information about it. Related View USER_ADDM_INSTANCES displays instance-level information for ADDM tasks that finished executing in all instances owned by the current user. See Also: " USER_ADDM_INSTANCES "