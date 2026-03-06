---
id: 19c__DBA_HIST_STREAMS_CAPTURE
name: DBA_HIST_STREAMS_CAPTURE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_STREAMS_CAPTURE.html
---

# DBA_HIST_STREAMS_CAPTURE

DBA_HIST_STREAMS_CAPTURE displays information about each capture process.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| CAPTURE_NAME | VARCHAR2(128) | Name of the capture process |
| STARTUP_TIME | DATE | Time that the capture process was last started |
| LAG | NUMBER | Delay (in seconds) between the creation and capture of the most recently captured message |
| TOTAL_MESSAGES_CAPTURED | NUMBER | Total changes captured since the capture process was last started |
| TOTAL_MESSAGES_ENQUEUED | NUMBER | Total number of messages enqueued since the capture process was last started |
| ELAPSED_RULE_TIME | NUMBER | Elapsed time (in hundredths of a second) evaluating rules since the capture process was last started |
| ELAPSED_ENQUEUE_TIME | NUMBER | Elapsed time (in hundredths of a second) enqueuing messages since the capture process was last started |
| ELAPSED_REDO_WAIT_TIME | NUMBER | Elapsed time (in hundredths of a second) spent by the capture process in the WAITING FOR REDO state |
| ELAPSED_PAUSE_TIME | NUMBER | Elapsed pause time |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

This view is intended for use with Automatic Workload Repository (AWR).