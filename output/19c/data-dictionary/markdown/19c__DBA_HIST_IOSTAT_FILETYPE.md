---
id: 19c__DBA_HIST_IOSTAT_FILETYPE
name: DBA_HIST_IOSTAT_FILETYPE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_HIST_IOSTAT_FILETYPE.html
---

# DBA_HIST_IOSTAT_FILETYPE

DBA_HIST_IOSTAT_FILETYPE displays historical I/O statistics by file type.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| FILETYPE_ID | NUMBER | Type of file (for example, log file, data file, and so on) |
| FILETYPE_NAME | VARCHAR2(30) | Name of the file, in the case of a data file or temp file. For all other files, a corresponding string to be displayed (for example, ARCHIVELOG ). |
| SMALL_READ_MEGABYTES | NUMBER | Number of single block megabytes read |
| SMALL_WRITE_MEGABYTES | NUMBER | Number of single block megabytes written |
| LARGE_READ_MEGABYTES | NUMBER | Number of multiblock megabytes read |
| LARGE_WRITE_MEGABYTES | NUMBER | Number of multiblock megabytes written |
| SMALL_READ_REQS | NUMBER | Number of single block read requests |
| SMALL_WRITE_REQS | NUMBER | Number of single block write requests |
| SMALL_SYNC_READ_REQS | NUMBER | Number of synchronous single block read requests |
| LARGE_READ_REQS | NUMBER | Number of multiblock read requests |
| LARGE_WRITE_REQS | NUMBER | Number of multiblock write requests |
| SMALL_READ_SERVICETIME | NUMBER | Total service time (in milliseconds) for single block read requests |
| SMALL_WRITE_SERVICETIME | NUMBER | Total service time (in milliseconds) for single block write requests |
| SMALL_SYNC_READ_LATENCY | NUMBER | Latency for single block synchronous reads (in milliseconds) |
| LARGE_READ_SERVICETIME | NUMBER | Total service time (in milliseconds) for multiblock read requests |
| LARGE_WRITE_SERVICETIME | NUMBER | Total service time (in milliseconds) for multiblock write requests |
| RETRIES_ON_ERROR | NUMBER | Number of read retries on error |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view contains snapshots of V$IOSTAT_FILE . See Also: " V$IOSTAT_FILE " See Also: " V$IOSTAT_FILE "