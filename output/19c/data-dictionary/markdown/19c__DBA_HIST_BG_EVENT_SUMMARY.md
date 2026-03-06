---
id: 19c__DBA_HIST_BG_EVENT_SUMMARY
name: DBA_HIST_BG_EVENT_SUMMARY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_BG_EVENT_SUMMARY.html
---

# DBA_HIST_BG_EVENT_SUMMARY

DBA_HIST_BG_EVENT_SUMMARY displays the historical summary background event activity.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| EVENT_ID | NUMBER | Identifier of the wait event |
| EVENT_NAME | VARCHAR2(64) | Name of the wait event |
| WAIT_CLASS_ID | NUMBER | Identifier of the class of the wait event |
| WAIT_CLASS | VARCHAR2(64) | Name of the class of the wait event |
| TOTAL_WAITS | NUMBER | Total number of waits for the event |
| TOTAL_TIMEOUTS | NUMBER | Total number of timeouts for the event |
| TIME_WAITED_MICRO | NUMBER | Total amount of time waited for the event (in microseconds) |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view contains snapshots from V$SESSION_EVENT . See Also: " V$SESSION_EVENT " See Also: " V$SESSION_EVENT "