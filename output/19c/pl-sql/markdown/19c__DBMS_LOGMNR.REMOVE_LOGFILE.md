---
id: 19c__DBMS_LOGMNR.REMOVE_LOGFILE
name: DBMS_LOGMNR.REMOVE_LOGFILE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOGMNR
tags: [dbms_logmnr]
source_file: DBMS_LOGMNR.html
---

# DBMS_LOGMNR.REMOVE_LOGFILE

This procedure removes a redo log file from an existing list of redo log files for LogMiner to process.

## Syntax

```sql
DBMS_LOGMNR.REMOVE_LOGFILE ( 
   LogFileName     IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| LogFileName | VARCHAR2) | IN | Specifies the name of the redo log file to be removed from the list of redo log files to be analyzed during this session. |

## Usage Notes

In a CDB, the REMOVE_LOGFILE procedure must be called from the root database. You must have the LOGMINING administrative privilege to use this procedure. Syntax DBMS_LOGMNR.REMOVE_LOGFILE ( LogFileName IN VARCHAR2); Parameters Table 101-13 REMOVE_LOGFILE Procedure Parameters Parameter Description LogFileName Specifies the name of the redo log file to be removed from the list of redo log files to be analyzed during this session. Exceptions Table 101-14 REMOVE_LOGFILE Procedure Exception Exception Description ORA-01290 Cannot remove unlisted log file Usage Notes Before querying the V$LOGMNR_CONTENTS view, you must make a successful call to the DBMS_LOGMNR.START_LOGMNR procedure (within the current LogMiner session). You can use this procedure to remove a redo log file from the list of redo log files for LogMiner to process if you know that redo log file does not contain any data of interest. Multiple redo log files can be removed by calling this procedure repeatedly. The redo log files do not need to be removed in any particular order. To start a new list of redo log files for analysis, use the END_LOGMNR procedure to end the current LogMiner session, and then build a new list using the ADD_LOGFILE procedure. Even if you remove all redo log files from the list, any subsequent calls you make to the ADD_LOGFILE procedure must match the database ID and RESETLOGS SCN of the removed redo log files. Therefore, to analyze the redo log files from a different database (or a database incarnation with a different database RESETLOGS SCN ) than that with which the current list of redo log files is associated, use the END_LOGMNR procedure to end the current LogMiner session, and then build a new list using the ADD_LOGFILE procedure.