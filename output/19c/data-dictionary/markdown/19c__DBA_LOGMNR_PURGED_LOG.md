---
id: 19c__DBA_LOGMNR_PURGED_LOG
name: DBA_LOGMNR_PURGED_LOG
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dba]
source_file: DBA_LOGMNR_PURGED_LOG.html
---

# DBA_LOGMNR_PURGED_LOG

DBA_LOGMNR_PURGED_LOG displays archived redo log files that have been applied to the logical standby database and can be deleted because they are no longer needed.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FILE_NAME | VARCHAR2(513) | Fully qualified names of the archived redo log files that are no longer needed by SQL Apply and can be deleted from the operating system |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Files in this view are refreshed as a result of executing the DBMS_LOGSTDBY.PURGE_SESSION PL/SQL procedure for Oracle Data Guard SQL Apply: See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_LOGSTDBY.PURGE_SESSION procedure See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_LOGSTDBY.PURGE_SESSION procedure