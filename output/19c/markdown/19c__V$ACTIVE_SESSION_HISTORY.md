---
id: 19c__V$ACTIVE_SESSION_HISTORY
name: V$ACTIVE_SESSION_HISTORY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-ACTIVE_SESSION_HISTORY.html
---

# V$ACTIVE_SESSION_HISTORY

V$ACTIVE_SESSION_HISTORY displays sampled session activity in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SAMPLE_ID | NUMBER |  |
| SAMPLE_TIME | TIMESTAMP(3) |  |
| IS_AWR_SAMPLE | VARCHAR2(1) |  |
| SESSION_ID | NUMBER |  |
| SESSION_SERIAL# | NUMBER |  |
| SESSION_TYPE | VARCHAR2(10) |  |
| FLAGS | NUMBER |  |
| USER_ID | NUMBER |  |
| SQL_ID | VARCHAR2(13) |  |
| IS_SQLID_CURRENT | VARCHAR2(1) |  |
| SQL_CHILD_NUMBER | NUMBER |  |
| SQL_OPCODE | NUMBER |  |
| SQL_OPNAME | VARCHAR2(64) |  |
| FORCE_MATCHING_SIGNATURE | NUMBER |  |
| TOP_LEVEL_SQL_ID | VARCHAR2(13) |  |
| TOP_LEVEL_SQL_OPCODE | NUMBER |  |
| SQL_ADAPTIVE_PLAN_RESOLVED | NUMBER |  |
| SQL_FULL_PLAN_HASH_VALUE | NUMBER |  |
| SQL_PLAN_HASH_VALUE | NUMBER |  |
| SQL_PLAN_LINE_ID | NUMBER |  |
| SQL_PLAN_OPERATION | VARCHAR2(30) |  |
| SQL_PLAN_OPTIONS | VARCHAR2(30) |  |
| SQL_EXEC_ID | NUMBER |  |
| SQL_EXEC_START | DATE |  |
| PLSQL_ENTRY_OBJECT_ID | NUMBER |  |
| PLSQL_ENTRY_SUBPROGRAM_ID | NUMBER |  |
| PLSQL_OBJECT_ID | NUMBER |  |
| PLSQL_SUBPROGRAM_ID | NUMBER |  |
| QC_INSTANCE_ID | NUMBER |  |
| QC_SESSION_ID | NUMBER |  |
| QC_SESSION_SERIAL# | NUMBER |  |
| PX_FLAGS | NUMBER |  |
| EVENT | VARCHAR2(64) |  |
| EVENT_ID | NUMBER |  |
| EVENT# | NUMBER |  |
| SEQ# | NUMBER |  |
| P1TEXT | VARCHAR2(64) |  |
| P1 | NUMBER |  |
| P2TEXT | VARCHAR2(64) |  |
| P2 | NUMBER |  |
| P3TEXT | VARCHAR2(64) |  |
| P3 | NUMBER |  |
| WAIT_CLASS | VARCHAR2(64) |  |
| WAIT_CLASS_ID | NUMBER |  |
| WAIT_TIME | NUMBER |  |
| SESSION_STATE | VARCHAR2(7) |  |
| TIME_WAITED | NUMBER |  |
| BLOCKING_SESSION_STATUS | VARCHAR2(11) |  |
| BLOCKING_SESSION | NUMBER |  |
| BLOCKING_SESSION_SERIAL# | NUMBER |  |
| BLOCKING_INST_ID | NUMBER |  |
| BLOCKING_HANGCHAIN_INFO | VARCHAR2(1) |  |
| CURRENT_OBJ# | NUMBER |  |
| CURRENT_FILE# | NUMBER |  |
| CURRENT_BLOCK# | NUMBER |  |
| CURRENT_ROW# | NUMBER |  |
| TOP_LEVEL_CALL# | NUMBER |  |
| TOP_LEVEL_CALL_NAME | VARCHAR2(64) |  |
| CONSUMER_GROUP_ID | NUMBER |  |
| XID | RAW(8) |  |
| REMOTE_INSTANCE# | NUMBER |  |
| TIME_MODEL | NUMBER |  |
| IN_CONNECTION_MGMT | VARCHAR2(1) |  |
| IN_PARSE | VARCHAR2(1) |  |
| IN_HARD_PARSE | VARCHAR2(1) |  |
| IN_SQL_EXECUTION | VARCHAR2(1) |  |
| IN_PLSQL_EXECUTION | VARCHAR2(1) |  |
| IN_PLSQL_RPC | VARCHAR2(1) |  |
| IN_PLSQL_COMPILATION | VARCHAR2(1) |  |
| IN_JAVA_EXECUTION | VARCHAR2(1) |  |
| IN_BIND | VARCHAR2(1) |  |
| IN_CURSOR_CLOSE | VARCHAR2(1) |  |
| IN_SEQUENCE_LOAD | VARCHAR2(1) |  |
| IN_INMEMORY_QUERY | VARCHAR2(1) |  |
| IN_INMEMORY_POPULATE | VARCHAR2(1) |  |
| IN_INMEMORY_PREPOPULATE | VARCHAR2(1) |  |
| IN_INMEMORY_REPOPULATE | VARCHAR2(1) |  |
| IN_INMEMORY_TREPOPULATE | VARCHAR2(1) |  |
| IN_TABLESPACE_ENCRYPTION | VARCHAR2(1) |  |
| CAPTURE_OVERHEAD | VARCHAR2(1) |  |
| REPLAY_OVERHEAD | VARCHAR2(1) |  |
| IS_CAPTURED | VARCHAR2(1) |  |
| IS_REPLAYED | VARCHAR2(1) |  |
| IS_REPLAY_SYNC_TOKEN_HOLDER | VARCHAR2(1) |  |
| SERVICE_HASH | NUMBER |  |
| PROGRAM | VARCHAR2(48) |  |
| MODULE | VARCHAR2(64) |  |
| ACTION | VARCHAR2(64) |  |
| CLIENT_ID | VARCHAR2(64) |  |
| MACHINE | VARCHAR2(64) |  |
| PORT | NUMBER |  |
| ECID | VARCHAR2(64) |  |
| DBREPLAY_FILE_ID | NUMBER |  |
| DBREPLAY_CALL_COUNTER | NUMBER |  |
| TM_DELTA_TIME | NUMBER |  |
| TM_DELTA_CPU_TIME | NUMBER |  |
| TM_DELTA_DB_TIME | NUMBER |  |
| DELTA_TIME | NUMBER |  |
| DELTA_READ_IO_REQUESTS | NUMBER |  |
| DELTA_WRITE_IO_REQUESTS | NUMBER |  |
| DELTA_READ_IO_BYTES | NUMBER |  |
| DELTA_WRITE_IO_BYTES | NUMBER |  |
| DELTA_INTERCONNECT_IO_BYTES | NUMBER |  |
| DELTA_READ_MEM_BYTES | NUMBER |  |
| PGA_ALLOCATED | NUMBER |  |
| TEMP_SPACE_ALLOCATED | NUMBER |  |
| CON_DBID | NUMBER |  |
| CON_ID | NUMBER |  |
| DBOP_NAME | VARCHAR2(30) |  |
| DBOP_EXEC_ID | NUMBER |  |

## Usage Notes

It contains snapshots of active database sessions taken once a second. A database session is considered active if it was on the CPU or was waiting for an event that didn't belong to the Idle wait class. Refer to the V$EVENT_NAME view for more information on wait classes. This view contains one row for each active session per sample and returns the latest session sample rows first. A majority of the columns describing the session in the active session history are present in the V$SESSION view. See Also: " V$SESSION " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_APPLICATION_INFO.SET_MODULE procedure Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_APPLICATION_INFO.SET_ACTION procedure See Also: " V$SESSION " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_APPLICATION_INFO.SET_MODULE procedure Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_APPLICATION_INFO.SET_ACTION procedure