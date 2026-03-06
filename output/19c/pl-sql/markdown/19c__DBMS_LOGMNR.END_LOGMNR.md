---
id: 19c__DBMS_LOGMNR.END_LOGMNR
name: DBMS_LOGMNR.END_LOGMNR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOGMNR
tags: [dbms_logmnr]
source_file: DBMS_LOGMNR.html
---

# DBMS_LOGMNR.END_LOGMNR

This procedure finishes a LogMiner session. Because this procedure performs cleanup operations that may not otherwise be done, you must use it to properly end a LogMiner session. This procedure is called automatically when you log out of a database session or when you call DBMS_LOGMNR.ADD_LOGFILE and specify the NEW option.

## Syntax

```sql
DBMS_LOGMNR.END_LOGMNR;
```

## Usage Notes

Syntax DBMS_LOGMNR.END_LOGMNR; Exceptions Table 101-9 END_LOGMNR Procedure Exception Exception Description ORA-01307 No LogMiner session is currently active. The END_LOGMNR procedure was called without adding any log files or before the START_LOGMNR procedure was called