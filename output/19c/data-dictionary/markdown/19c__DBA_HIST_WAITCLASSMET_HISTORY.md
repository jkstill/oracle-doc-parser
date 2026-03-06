---
id: 19c__DBA_HIST_WAITCLASSMET_HISTORY
name: DBA_HIST_WAITCLASSMET_HISTORY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_HIST_WAITCLASSMET_HISTORY.html
---

# DBA_HIST_WAITCLASSMET_HISTORY

DBA_HIST_WAITCLASSMET_HISTORY displays the history of the wait event class metric data kept by the Workload Repository.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID of the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number of the snapshot |
| WAIT_CLASS_ID | NUMBER | Identifier of the class of the wait event |
| WAIT_CLASS | VARCHAR2(64) | Name of the class of the wait event |
| BEGIN_TIME | DATE | Begin time of the interval |
| END_TIME | DATE | End time of the interval |
| INTSIZE | NUMBER | Interval size (in hundredths of a second) |
| GROUP_ID | NUMBER | Metric group ID |
| AVERAGE_WAITER_COUNT | NUMBER | Average waiter count |
| DBTIME_IN_WAIT | NUMBER | Percent of database time spent in the wait |
| TIME_WAITED | NUMBER | Time waited during the interval (in microseconds) |
| WAIT_COUNT | NUMBER | Number of times waited |
| TIME_WAITED_FG | NUMBER | Time waited (in hundredths of a second), from foreground sessions |
| WAIT_COUNT_FG | NUMBER | Number of times waited, from foreground sessions |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content