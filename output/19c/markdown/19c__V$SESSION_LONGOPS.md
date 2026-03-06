---
id: 19c__V$SESSION_LONGOPS
name: V$SESSION_LONGOPS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-SESSION_LONGOPS.html
---

# V$SESSION_LONGOPS

To monitor query execution progress, you must be using the cost-based optimizer and you must:

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SID | NUMBER |  |
| SERIAL# | NUMBER |  |
| OPNAME | VARCHAR2(64) |  |
| TARGET | VARCHAR2(64) |  |
| TARGET_DESC | VARCHAR2(32) |  |
| SOFAR | NUMBER |  |
| TOTALWORK | NUMBER |  |
| UNITS | VARCHAR2(32) |  |
| START_TIME | DATE |  |
| LAST_UPDATE_TIME | DATE |  |
| TIMESTAMP | DATE |  |
| TIME_REMAINING | NUMBER |  |
| ELAPSED_SECONDS | NUMBER |  |
| CONTEXT | NUMBER |  |
| MESSAGE | VARCHAR2(512) |  |
| USERNAME | VARCHAR2(30) |  |
| SQL_ADDRESS | RAW(4 | 8) |  |
| SQL_HASH_VALUE | NUMBER |  |
| SQL_ID | VARCHAR2(13) |  |
| SQL_PLAN_HASH_VALUE | NUMBER |  |
| SQL_EXEC_START | DATE |  |
| SQL_EXEC_ID | NUMBER |  |
| SQL_PLAN_LINE_ID | NUMBER |  |
| SQL_PLAN_OPERATION | VARCHAR2(30) |  |
| SQL_PLAN_OPTIONS | VARCHAR2(30) |  |
| QCSID | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

To monitor query execution progress, you must be using the cost-based optimizer and you must: Set the TIMED_STATISTICS or SQL_TRACE parameters to true Gather statistics for your objects with the DBMS_STATS package You can add information to this view about application-specific long-running operations by using the DBMS_APPLICATION_INFO.SET_SESSION_LONGOPS procedure. See Also: " TIMED_STATISTICS " " SQL_TRACE " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_APPLICATION_INFO.SET_SESSION_LONGOPS procedure Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_STATS package See Also: " TIMED_STATISTICS " " SQL_TRACE " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_APPLICATION_INFO.SET_SESSION_LONGOPS procedure Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_STATS package