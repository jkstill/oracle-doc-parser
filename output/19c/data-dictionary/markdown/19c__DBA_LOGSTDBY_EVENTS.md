---
id: 19c__DBA_LOGSTDBY_EVENTS
name: DBA_LOGSTDBY_EVENTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dba]
source_file: DBA_LOGSTDBY_EVENTS.html
---

# DBA_LOGSTDBY_EVENTS

DBA_LOGSTDBY_EVENTS displays information about the activity of the logical standby database system.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| EVENT_TIME | DATE | Time when the event was logged |
| EVENT_TIMESTAMP | TIMESTAMP(6) | Timestamp when the event was logged |
| START_SCN | NUMBER | The SCN at which the associated transaction started at the primary database. This SCN refers to the system change number at the primary database. |
| CURRENT_SCN | NUMBER | SCN associated with the change at the primary database. If a failure occurred, then examine this column to determine which archived log file contains the source of the failure (for example, an unsupported record). |
| COMMIT_SCN | NUMBER | SCN value on which the change was committed at the primary database |
| XIDUSN | NUMBER | Transaction ID undo segment number at the primary database of the associated transaction |
| XIDSLT | NUMBER | Transaction ID slot number at the primary database of the associated transaction |
| XIDSQN | NUMBER | Transaction ID sequence number at the primary database of the associated transaction |
| EVENT | CLOB | Statement that was being processed when the failure occurred |
| STATUS_CODE | NUMBER | Status (or Oracle error code) belonging to the STATUS message |
| STATUS | VARCHAR2(2000) | Description of the current activity of the process or the reason why the apply operation stopped |
| SRC_CON_NAME | VARCHAR2(30) | Identifies the PDB name at the primary database where the transaction was executed |
| SRC_CON_ID | NUMBER | Contains the PDB ID (the PDB_ID column from the DBA_PDBS view) of the primary database where the associated change was generated. |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content It can be used to determine the cause of failures that occur when applying redo data to logical standby databases. This view is for logical standby databases only. Note: In a CDB, this view shows data only when queried in the root. Note: In a CDB, this view shows data only when queried in the root.