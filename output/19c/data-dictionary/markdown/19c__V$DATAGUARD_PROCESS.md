---
id: 19c__V$DATAGUARD_PROCESS
name: V$DATAGUARD_PROCESS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-DATAGUARD_PROCESS.html
---

# V$DATAGUARD_PROCESS

V$DATAGUARD_PROCESS displays one row for each Oracle Data Guard process that is currently running.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAME | VARCHAR2(5) |  |
| PID | VARCHAR2(24) |  |
| TYPE | VARCHAR2(3) |  |
| ROLE | VARCHAR2(24) |  |
| PROC_TIME | TIMESTAMP(0) |  |
| TASK_TIME | TIMESTAMP(0) |  |
| TASK_DONE | VARCHAR2(1) |  |
| ACTION | VARCHAR2(12) |  |
| CLIENT_PID | NUMBER |  |
| CLIENT_ROLE | VARCHAR2(16) |  |
| GROUP# | NUMBER |  |
| RESETLOG_ID | NUMBER |  |
| THREAD# | NUMBER |  |
| SEQUENCE# | NUMBER |  |
| BLOCK# | NUMBER |  |
| BLOCK_COUNT | NUMBER |  |
| DELAY_MINS | NUMBER |  |
| DEST_ID | NUMBER |  |
| DEST_MASK | NUMBER |  |
| DBID | NUMBER |  |
| DGID | NUMBER |  |
| INSTANCE | NUMBER |  |
| STOP_STATE | VARCHAR2(7) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: Oracle recommends that you use this view instead of V$MANAGED_STANDBY . Note: Oracle recommends that you use this view instead of V$MANAGED_STANDBY .