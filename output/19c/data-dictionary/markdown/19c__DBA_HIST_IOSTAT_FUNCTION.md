---
id: 19c__DBA_HIST_IOSTAT_FUNCTION
name: DBA_HIST_IOSTAT_FUNCTION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_HIST_IOSTAT_FUNCTION.html
---

# DBA_HIST_IOSTAT_FUNCTION

DBA_HIST_IOSTAT_FUNCTION displays historical I/O statistics by function.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| FUNCTION_ID | NUMBER | Function ID |
| FUNCTION_NAME | VARCHAR2(128) | Function name |
| SMALL_READ_MEGABYTES | NUMBER | Number of single block megabytes read |
| SMALL_WRITE_MEGABYTES | NUMBER | Number of single block megabytes written |
| LARGE_READ_MEGABYTES | NUMBER | Number of multiblock megabytes read |
| LARGE_WRITE_MEGABYTES | NUMBER | Number of multiblock megabytes written |
| SMALL_READ_REQS | NUMBER | Number of single block read requests |
| SMALL_WRITE_REQS | NUMBER | Number of single block write requests |
| LARGE_READ_REQS | NUMBER | Number of multiblock read requests |
| LARGE_WRITE_REQS | NUMBER | Number of multiblock write requests |
| NUMBER_OF_WAITS | NUMBER | Number of I/O waits by functionality |
| WAIT_TIME | NUMBER | Total wait time (in milliseconds) |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view contains snapshots of V$IOSTAT_FUNCTION . See Also: " V$IOSTAT_FUNCTION " See Also: " V$IOSTAT_FUNCTION "