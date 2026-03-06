---
id: 19c__DBA_LOGSTDBY_LOG
name: DBA_LOGSTDBY_LOG
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dba]
source_file: DBA_LOGSTDBY_LOG.html
---

# DBA_LOGSTDBY_LOG

DBA_LOGSTDBY_LOG displays information about the logs registered for a logical standby database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| THREAD# | NUMBER | Thread ID of the archive log. The THREAD number is 1 for a single instance. For Real Application Clusters, this column will contain different numbers. |
| RESETLOGS_CHANGE# | NUMBER | Start SCN of the branch |
| RESETLOGS_ID | NUMBER | Resetlogs identifier (a numeric form of the timestamp of the branch) |
| SEQUENCE# | NUMBER | Sequence number of the archive log file |
| FIRST_CHANGE# | NUMBER | System change number (SCN) of the current archive log |
| NEXT_CHANGE# | NUMBER | SCN of the next archive log |
| FIRST_TIME | DATE | Date of the current archive log |
| NEXT_TIME | DATE | Date of the next archive log |
| FILE_NAME | VARCHAR2(513) | Name of the archive log |
| TIMESTAMP | DATE | Time when the archive log was registered |
| DICT_BEGIN | VARCHAR2(3) | Indicates whether the beginning of the dictionary build is in this archive log ( YES ) or not ( NO ) |
| DICT_END | VARCHAR2(3) | Indicates whether the end of the dictionary build is in this archive log ( YES ) or not ( NO ) |
| APPLIED | VARCHAR2(8) | Indicates primarily whether a given foreign archived log has been applied fully by SQL Apply: YES - SQL Apply has fully applied the foreign archived log and no longer needs it CURRENT - SQL Apply is currently applying changes contained in the foreign archived log NO - SQL Apply has not started applying any changes contained in the foreign archived log FETCHING - SQL Apply encountered a corruption while reading redo records from this foreign archived log, and is currently using the automatic gap resolution to refetch a new copy of the log from the primary database CORRUPT - SQL Apply encountered a corruption while reading redo records from this foreign archived log, and refetching a new copy of the archived log did not resolve the problem. SQL Apply will not refetch a new copy of this archived log automatically, and will require user intervention to manually register a new copy of the foreign archived log. |
| BLOCKS | NUMBER | Number of blocks in the log |
| BLOCK_SIZE | NUMBER | Size of each block in the log |

## Usage Notes

This view is for logical standby databases only. Note: The SCN values in this view correlate to the SCN values shown in the DBA_LOGSTDBY_PROGRESS view. Note: In a CDB, this view shows data only when queried in the root. Note: The SCN values in this view correlate to the SCN values shown in the DBA_LOGSTDBY_PROGRESS view. Note: In a CDB, this view shows data only when queried in the root.