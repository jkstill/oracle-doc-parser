---
id: 19c__DBA_LOGMNR_LOG
name: DBA_LOGMNR_LOG
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dba]
source_file: DBA_LOGMNR_LOG.html
---

# DBA_LOGMNR_LOG

DBA_LOGMNR_LOG displays all archived logs registered with active LogMiner persistent sessions in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| LOGMNR_SESSION_ID | NUMBER | Unique identifier of the persistent session |
| NAME | VARCHAR2(513) | Name of the archived log |
| DBID | NUMBER | Database identifier that produced the archived log |
| RESETLOGS_SCN | NUMBER | SCN at which resetlogs operation was performed at the source database generating the archived log |
| RESETLOGS_TIME | NUMBER | Timestamp at which resetlogs operation was performed at the source database generating the archived log |
| MODIFIED_TIME | DATE | Time at which the archived log was registered with LogMiner |
| THREAD# | NUMBER | Redo thread at the source database that generated the archived log |
| SEQUENCE# | NUMBER | Logfile sequence number |
| FIRST_SCN | NUMBER | Lowest SCN of the redo record contained in the logfile |
| NEXT_SCN | NUMBER | Highest possible SCN of the redo record contained in the logfile |
| FIRST_TIME | DATE | Time of the first redo record contained in the logfile |
| NEXT_TIME | DATE | Time of the last redo record contained in the logfile |
| DICTIONARY_BEGIN | VARCHAR2(3) | Indicates whether the archived log contains the beginning of a LogMiner dictionary ( YES ) or not ( NO ) |
| DICTIONARY_END | VARCHAR2(3) | Indicates whether the archived log contains the end of a LogMiner dictionary ( YES ) or not ( NO ) |
| KEEP | VARCHAR2(3) | Indicates whether the logfile is still required for this LogMiner session ( YES ) or not ( NO ) |
| SUSPECT | VARCHAR2(3) | Indicates whether the archived log content was deemed to be corrupt or the archived log is partially filled ( YES ) or not ( NO ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content A persistent LogMiner session is created either by starting Data Guard SQL Apply on a logical standby database for the first time or by creating Replication capture.