---
id: 19c__DBMS_LOGMNR.ADD_LOGFILE
name: DBMS_LOGMNR.ADD_LOGFILE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOGMNR
tags: [dbms_logmnr]
source_file: DBMS_LOGMNR.html
---

# DBMS_LOGMNR.ADD_LOGFILE

This procedure adds a file to an existing or newly created list of log files for LogMiner to process.

## Syntax

```sql
DBMS_LOGMNR.ADD_LOGFILE ( 
   LogFileName     IN VARCHAR2,
   options         IN BINARY_INTEGER default ADDFILE );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| LogFileName | VARCHAR2 | IN | Specifies the name of the redo log file to add to the list of redo log files to be analyzed during this session. |
| options | BINARY_INTEGER | IN | Does one of the following: Starts a new LogMiner session and a new list of redo log files for analysis ( DBMS_LOGMNR.NEW ) Adds a file to an existing list of redo log files for analysis ( DBMS_LOGMNR.ADDFILE ) See Table 101-1 . |

## Usage Notes

Note: The continuous_mine option for the dbms_logmnr.start_logmnr package is desupported in Oracle Database 19c (19.1), and is no longer available. In a CDB, the ADD_LOGFILE procedure must be called from the root database. You must have the LOGMINING administrative privilege to use this procedure. Note: The continuous_mine option for the dbms_logmnr.start_logmnr package is desupported in Oracle Database 19c (19.1), and is no longer available. Syntax DBMS_LOGMNR.ADD_LOGFILE ( LogFileName IN VARCHAR2, options IN BINARY_INTEGER default ADDFILE ); Parameters Table 101-4 ADD_LOGFILE Procedure Parameters Parameter Description LogFileName Specifies the name of the redo log file to add to the list of redo log files to be analyzed during this session. options Does one of the following: Starts a new LogMiner session and a new list of redo log files for analysis ( DBMS_LOGMNR.NEW ) Adds a file to an existing list of redo log files for analysis ( DBMS_LOGMNR.ADDFILE ) See Table 101-1 . Exceptions Table 101-5 ADD_LOGFILE Procedure Exceptions Exception Description ORA-01284 Specified file cannot be opened. ORA-01287 Specified file is from a different database incarnation. ORA-01289 Specified file has already been added to the list. Duplicate redo log files cannot be added. ORA-01290 Specified file is not in the current list and therefore cannot be removed from the list. ORA-01324 Specified file cannot be added to the list because there is a DB_ID mismatch.