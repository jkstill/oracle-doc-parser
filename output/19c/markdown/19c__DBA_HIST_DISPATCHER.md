---
id: 19c__DBA_HIST_DISPATCHER
name: DBA_HIST_DISPATCHER
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_DISPATCHER.html
---

# DBA_HIST_DISPATCHER

DBA_HIST_DISPATCHER displays historical information for each dispatcher process present at the time of the snapshot.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| NAME | VARCHAR2(4) | Name of the dispatcher process |
| SERIAL# | NUMBER | Serial number of the dispatcher process |
| IDLE | NUMBER | Total idle time for the dispatcher (in hundredths of a second) |
| BUSY | NUMBER | Total busy time for the dispatcher (in hundredths of a second) |
| WAIT | NUMBER | Total time that all items in the dispatcher queue have waited (in hundredths of a second). Divide by TOTALQ for average wait per item. |
| TOTALQ | NUMBER | Total number of items that have ever been in the dispatcher queue |
| SAMPLED_TOTAL_CONN | NUMBER | Cumulative sum of total number of connections to the dispatcher over all samples. To determine the average number of connections to the dispatcher between two snapshots, divide the difference in SAMPLED_TOTAL_CONN by the difference in NUM_SAMPLES (obtained from DBA_HIST_SHARED_SERVER_SUMMARY ). |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

This view contains snapshots of information from V$DISPATCHER and V$QUEUE . See Also: " V$DISPATCHER " " V$QUEUE " See Also: " V$DISPATCHER " " V$QUEUE "