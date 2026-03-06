---
id: 19c__DBA_HIST_LOG
name: DBA_HIST_LOG
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dba]
source_file: DBA_HIST_LOG.html
---

# DBA_HIST_LOG

DBA_HIST_LOG displays historical log file information from the control file. This view contains snapshots of V$LOG .

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| GROUP# | NUMBER | Log group number |
| THREAD# | NUMBER | Log thread number |
| SEQUENCE# | NUMBER | Log sequence number |
| BYTES | NUMBER | Size of the log (in bytes) |
| MEMBERS | NUMBER | Number of members in the log group |
| ARCHIVED | VARCHAR2(3) | Archive status ( YES ) or NO ) |
| STATUS | VARCHAR2(16) | Log status: UNUSED - Online redo log has never been written to. This is the state of a redo log that was just added, or just after a RESETLOGS , when it is not the current redo log. CURRENT - Current redo log. This implies that the redo log is active. The redo log could be open or closed. ACTIVE - Log is active but is not the current log. It is needed for crash recovery. It may be in use for block recovery. It may or may not be archived. CLEARING - Log is being re-created as an empty log after an ALTER DATABASE CLEAR LOGFILE statement. After the log is cleared, the status changes to UNUSED . CLEARING_CURRENT - Current log is being cleared of a closed thread. The log can stay in this status if there is some failure in the switch such as an I/O error writing the new log header. INACTIVE - Log is no longer needed for instance recovery. It may be in use for media recovery. It may or may not be archived. INVALIDATED - Archived the current redo log without a log switch. |
| FIRST_CHANGE# | NUMBER | Lowest system change number (SCN) in the log |
| FIRST_TIME | DATE | Time of the first SCN in the log |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: " V$LOG " See Also: " V$LOG "