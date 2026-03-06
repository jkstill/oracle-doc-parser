---
id: 19c__V$BACKUP_ASYNC_IO
name: V$BACKUP_ASYNC_IO
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-BACKUP_ASYNC_IO.html
---

# V$BACKUP_ASYNC_IO

V$BACKUP_ASYNC_IO displays performance information about ongoing and recently completed RMAN backups and restores.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SID | NUMBER |  |
| SERIAL | NUMBER |  |
| USE_COUNT | NUMBER |  |
| RMAN_STATUS_RECID | NUMBER |  |
| RMAN_STATUS_STAMP | NUMBER |  |
| DEVICE_TYPE | VARCHAR2(17) |  |
| TYPE | VARCHAR2(9) |  |
| STATUS | VARCHAR2(11) |  |
| FILENAME | VARCHAR2(513) |  |
| SET_COUNT | NUMBER |  |
| SET_STAMP | NUMBER |  |
| BUFFER_SIZE | NUMBER |  |
| BUFFER_COUNT | NUMBER |  |
| TOTAL_BYTES | NUMBER |  |
| OPEN_TIME | DATE |  |
| CLOSE_TIME | DATE |  |
| ELAPSED_TIME | NUMBER |  |
| MAXOPENFILES | NUMBER |  |
| BYTES | NUMBER |  |
| EFFECTIVE_BYTES_PER_SECOND | NUMBER |  |
| IO_COUNT | NUMBER |  |
| READY | NUMBER |  |
| SHORT_WAITS | NUMBER |  |
| SHORT_WAIT_TIME_TOTAL | NUMBER |  |
| SHORT_WAIT_TIME_MAX | NUMBER |  |
| LONG_WAITS | NUMBER |  |
| LONG_WAIT_TIME_TOTAL | NUMBER |  |
| LONG_WAIT_TIME_MAX | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

For each backup, it contains one row for each input data file, one row for the aggregate total performance of all data files, and one row for the output backup piece. This data is not stored persistently, and is not preserved when the instance is re-started.