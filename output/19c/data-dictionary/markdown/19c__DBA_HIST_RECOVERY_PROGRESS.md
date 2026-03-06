---
id: 19c__DBA_HIST_RECOVERY_PROGRESS
name: DBA_HIST_RECOVERY_PROGRESS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_RECOVERY_PROGRESS.html
---

# DBA_HIST_RECOVERY_PROGRESS

DBA_HIST_RECOVERY_PROGRESS displays database recovery progress information for an instance.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| START_TIME | DATE | Start time of the recovery operation |
| TYPE | VARCHAR2(64) | Type of recovery operation being performed: CRASH RECOVERY INSTANCE RECOVERY MEDIA RECOVERY |
| ITEM | VARCHAR2(32) | Item being measured. When TYPE is CRASH RECOVERY or INSTANCE RECOVERY , the possible values are: Log Files Redo Blocks When TYPE is MEDIA RECOVERY , the possible values are: Active Apply Rate Average Apply Rate Maximum Apply Rate Redo Applied Log Files Last Applied Redo Active Time Elapsed Time Apply Time per Log Checkpoint Time per Log Standby Apply Lag Recovery ID |
| UNITS | VARCHAR2(32) | The units of measurement for each item |
| SOFAR | NUMBER | Amount of work done so far |
| TOTAL | NUMBER | Total amount of work expected |
| TIMESTAMP | DATE | Timestamp of the last redo record applied |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root. n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content