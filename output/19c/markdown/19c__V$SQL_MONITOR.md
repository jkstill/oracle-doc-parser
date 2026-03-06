---
id: 19c__V$SQL_MONITOR
name: V$SQL_MONITOR
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dynamic_performance]
source_file: V-SQL_MONITOR.html
---

# V$SQL_MONITOR

V$SQL_MONITOR displays SQL statements whose execution have been (or are being) monitored by Oracle.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| KEY | NUMBER |  |
| REPORT_ID | NUMBER |  |
| STATUS | VARCHAR2(19) |  |
| USER# | NUMBER |  |
| USERNAME | VARCHAR2(128) |  |
| MODULE | VARCHAR2(64) |  |
| ACTION | VARCHAR2(64) |  |
| SERVICE_NAME | VARCHAR2(64) |  |
| CLIENT_IDENTIFIER | VARCHAR2(64) |  |
| CLIENT_INFO | VARCHAR2(64) |  |
| PROGRAM | VARCHAR2(48) |  |
| PLSQL_ENTRY_OBJECT_ID | NUMBER |  |
| PLSQL_ENTRY_SUBPROGRAM_ID | NUMBER |  |
| PLSQL_OBJECT_ID | NUMBER |  |
| PLSQL_SUBPROGRAM_ID | NUMBER |  |
| FIRST_REFRESH_TIME | DATE |  |
| LAST_REFRESH_TIME | DATE |  |
| REFRESH_COUNT | NUMBER |  |
| DBOP_EXEC_ID | NUMBER |  |
| DBOP_NAME | VARCHAR2(30) |  |
| SID | NUMBER |  |
| PROCESS_NAME | VARCHAR2(5) |  |
| SQL_ID | VARCHAR2(13) |  |
| SQL_TEXT | VARCHAR2(2000) |  |
| IS_FULL_SQLTEXT | VARCHAR2(1) |  |
| SQL_EXEC_START | DATE |  |
| SQL_EXEC_ID | NUMBER |  |
| SQL_PLAN_HASH_VALUE | NUMBER |  |
| SQL_FULL_PLAN_HASH_VALUE | NUMBER |  |
| EXACT_MATCHING_SIGNATURE | NUMBER |  |
| FORCE_MATCHING_SIGNATURE | NUMBER |  |
| SQL_CHILD_ADDRESS | RAW(4 | 8) |  |
| SESSION_SERIAL# | NUMBER |  |
| PX_IS_CROSS_INSTANCE | VARCHAR2(1) |  |
| PX_MAXDOP | NUMBER |  |
| PX_MAXDOP_INSTANCES | NUMBER |  |
| PX_SERVERS_REQUESTED | NUMBER |  |
| PX_SERVERS_ALLOCATED | NUMBER |  |
| PX_SERVER# | NUMBER |  |
| PX_SERVER_GROUP | NUMBER |  |
| PX_SERVER_SET | NUMBER |  |
| PX_QCINST_ID | NUMBER |  |
| PX_QCSID | NUMBER |  |
| ERROR_NUMBER | VARCHAR2(40) |  |
| ERROR_FACILITY | VARCHAR2(4) |  |
| ERROR_MESSAGE | VARCHAR2(256) |  |
| BINDS_XML | CLOB |  |
| OTHER_XML | CLOB |  |
| ELAPSED_TIME | NUMBER |  |
| QUEUING_TIME | NUMBER |  |
| CPU_TIME | NUMBER |  |
| FETCHES | NUMBER |  |
| BUFFER_GETS | NUMBER |  |
| DISK_READS | NUMBER |  |
| DIRECT_WRITES | NUMBER |  |
| IO_INTERCONNECT_BYTES | NUMBER |  |
| PHYSICAL_READ_REQUESTS | NUMBER |  |
| PHYSICAL_READ_BYTES | NUMBER |  |
| PHYSICAL_WRITE_REQUESTS | NUMBER |  |
| PHYSICAL_WRITE_BYTES | NUMBER |  |
| APPLICATION_WAIT_TIME | NUMBER |  |
| CONCURRENCY_WAIT_TIME | NUMBER |  |
| CLUSTER_WAIT_TIME | NUMBER |  |
| USER_IO_WAIT_TIME | NUMBER |  |
| PLSQL_EXEC_TIME | NUMBER |  |
| JAVA_EXEC_TIME | NUMBER |  |
| RM_LAST_ACTION | VARCHAR2(48) |  |
| RM_LAST_ACTION_REASON | VARCHAR2(128) |  |
| RM_LAST_ACTION_TIME | DATE |  |
| RM_CONSUMER_GROUP | VARCHAR2(128) |  |
| CON_ID | NUMBER |  |
| CON_NAME | VARCHAR2(128) |  |
| ECID | VARCHAR2(64) |  |
| IS_ADAPTIVE_PLAN | VARCHAR2(1) |  |
| IS_FINAL_PLAN | VARCHAR2(1) |  |
| IN_DBOP_NAME | VARCHAR2(30) |  |
| IN_DBOP_EXEC_ID | NUMBER |  |
| IO_CELL_UNCOMPRESSED_BYTES | NUMBER |  |
| IO_CELL_OFFLOAD_ELIGIBLE_BYTES | NUMBER |  |
| IO_CELL_OFFLOAD_RETURNED_BYTES | NUMBER |  |
| CURRENT_USER# Foot 1 | NUMBER |  |
| CURRENT_USERNAME Foot 1 | VARCHAR2(128) |  |

## Usage Notes

This view contains global, high-level information about simple and composite database operations. Oracle Database monitors simple database operations, which are top SQL statements and PL/SQL subprograms, when any of the following conditions is true: The operations run in parallel. The operations have consumed at least 5 seconds of CPU or I/O time in a single execution. Tracking for the operations is forced by the /*+ MONITOR */ hint. For simple database operations, monitoring statistics are not cumulative over several executions. In this case, one entry in V$SQL_MONITOR is dedicated to a single execution of a SQL statement. If the database monitors two executions of the same SQL statement, then each execution has a separate entry in V$SQL_MONITOR . For simple database operations, V$SQL_MONITOR has one entry for the parallel execution coordinator process and one entry for each parallel execution server process. Each entry has corresponding entries in V$SQL_PLAN_MONITOR . Because the processes allocated for the parallel execution of a SQL statement are cooperating for the same execution, these entries share the same execution key (the combination of SQL_ID , SQL_EXEC_START , and SQL_EXEC_ID ). Oracle Database monitors composite database operations when either of the following conditions is true: A database operation was started with DBMS_SQL_MONITOR.BEGIN_OPERATION and the operation has consumed at least 5 seconds of CPU or I/O time. Tracking for the operation is forced by setting FORCE_TRACKING to Y in DBMS_SQL_MONITOR.BEGIN_OPERATION . For composite database operations, each row contains an operation whose statistics are accumulated over the SQL statements and PL/SQL subprograms that run in the same session as part of the operation. The V$SQL_MONITOR view contains a subset of the statistics available in V$SQL . However, unlike V$SQL , monitoring statistics are not cumulative over several executions. Instead, one entry in V$SQL_MONITOR is dedicated to a single execution of a SQL statement. If the database monitors two executions of the same SQL statement, then each execution has a separate entry in V$SQL_MONITOR . The primary key is the combination of the columns SQL_ID , SQL_EXEC_START , and SQL_EXEC_ID . V$SQL_MONITOR has one entry for the parallel execution coordinator process, and one entry for each parallel execution server process. Each entry has corresponding entries in V$SQL_PLAN_MONITOR . Because the processes allocated for the parallel execution of a SQL statement are cooperating for the same execution, these entries share the same execution key (the composite SQL_ID , SQL_EXEC_START , and SQL_EXEC_ID ). You can aggregate the execution key to determine the overall statistics for a parallel execution. When the SQL statement being monitored is executing, statistics in V$SQL_MONITOR are generally refreshed in near real time, once every second. Once the execution ends, monitoring information is not deleted immediately. Instead, it is kept in V$SQL_MONITOR for at least one minute. The entry will eventually be deleted to reclaim its space as new statements are monitored. See Also: " V$SQL_PLAN_MONITOR " Oracle Database SQL Tuning Guide for more information about monitoring database operations Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_APPLICATION_INFO.SET_MODULE procedure Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_APPLICATION_INFO.SET_ACTION procedure See Also: " V$SQL_PLAN_MONITOR " Oracle Database SQL Tuning Guide for more information about monitoring database operations Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_APPLICATION_INFO.SET_MODULE procedure Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_APPLICATION_INFO.SET_ACTION procedure