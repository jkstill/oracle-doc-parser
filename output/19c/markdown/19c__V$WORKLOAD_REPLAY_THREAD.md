---
id: 19c__V$WORKLOAD_REPLAY_THREAD
name: V$WORKLOAD_REPLAY_THREAD
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-WORKLOAD_REPLAY_THREAD.html
---

# V$WORKLOAD_REPLAY_THREAD

V$WORKLOAD_REPLAY_THREAD displays information for all the different types of replay sessions.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CLOCK | NUMBER |  |
| NEXT_TICKER | NUMBER |  |
| SID | NUMBER |  |
| SERIAL# | NUMBER |  |
| SPID | VARCHAR2(24) |  |
| LOGON_USER | VARCHAR2(128) |  |
| LOGON_TIME | DATE |  |
| EVENT | VARCHAR2(64) |  |
| EVENT_ID | NUMBER |  |
| EVENT# | NUMBER |  |
| P1TEXT | VARCHAR2(64) |  |
| P1 | NUMBER |  |
| P2TEXT | VARCHAR2(64) |  |
| P2 | NUMBER |  |
| P3TEXT | VARCHAR2(64) |  |
| P3 | NUMBER |  |
| WAIT_FOR_SCN | NUMBER |  |
| FILE_ID | NUMBER |  |
| CALL_COUNTER | NUMBER |  |
| DEPENDENT_SCN | NUMBER |  |
| STATEMENT_SCN | NUMBER |  |
| COMMIT_WAIT_SCN | NUMBER |  |
| POST_COMMIT_SCN | NUMBER |  |
| ACTION_TYPE | NUMBER |  |
| SESSION_TYPE | VARCHAR2(13) |  |
| WRC_ID | NUMBER |  |
| SCHEDULE_CAP_ID | NUMBER |  |
| FILE_NAME | VARCHAR2(51) |  |
| SKIP_IT | VARCHAR2(1) |  |
| DIRTY_BUFFERS | VARCHAR2(1) |  |
| DBTIME | NUMBER |  |
| NETWORK_TIME | NUMBER |  |
| THINK_TIME | NUMBER |  |
| TIME_GAIN | NUMBER |  |
| TIME_LOSS | NUMBER |  |
| USER_CALLS | NUMBER |  |
| PLSQL_CALLS | NUMBER |  |
| PLSQL_SUBCALLS | NUMBER |  |
| PLSQL_DBTIME | NUMBER |  |
| CLIENT_OS_USER | VARCHAR2(15) |  |
| CLIENT_HOST | VARCHAR2(64) |  |
| CLIENT_PID | VARCHAR2(24) |  |
| PROGRAM | VARCHAR2(48) |  |
| CAPTURE_ELAPSED_TIME | NUMBER |  |
| REPLAY_ELAPSED_TIME | NUMBER |  |
| CON_ID | NUMBER |  |