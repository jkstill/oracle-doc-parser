---
id: 19c__V$IOSTAT_FILE
name: V$IOSTAT_FILE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-IOSTAT_FILE.html
---

# V$IOSTAT_FILE

V$IOSTAT_FILE displays information about disk I/O statistics of database files (including data files, temp files, and other types of database files).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FILE_NO | NUMBER |  |
| FILETYPE_ID | NUMBER |  |
| FILETYPE_NAME | VARCHAR2(28) |  |
| SMALL_READ_MEGABYTES | NUMBER |  |
| SMALL_WRITE_MEGABYTES | NUMBER |  |
| LARGE_READ_MEGABYTES | NUMBER |  |
| LARGE_WRITE_MEGABYTES | NUMBER |  |
| SMALL_READ_REQS | NUMBER |  |
| SMALL_WRITE_REQS | NUMBER |  |
| SMALL_SYNC_READ_REQS | NUMBER |  |
| LARGE_READ_REQS | NUMBER |  |
| LARGE_WRITE_REQS | NUMBER |  |
| SMALL_READ_SERVICETIME | NUMBER |  |
| SMALL_WRITE_SERVICETIME | NUMBER |  |
| SMALL_SYNC_READ_LATENCY | NUMBER |  |
| LARGE_READ_SERVICETIME | NUMBER |  |
| LARGE_WRITE_SERVICETIME | NUMBER |  |
| ASYNCH_IO | VARCHAR2(9) |  |
| ACCESS_METHOD | VARCHAR2(11) |  |
| RETRIES_ON_ERROR | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content I/O statistics for Data files and Temp files are provided for each file. All other file types (for example, control files, log files, archive logs, and so on) have their statistics consolidated into one entry in the view.