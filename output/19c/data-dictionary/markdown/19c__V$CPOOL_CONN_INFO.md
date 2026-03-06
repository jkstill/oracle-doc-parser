---
id: 19c__V$CPOOL_CONN_INFO
name: V$CPOOL_CONN_INFO
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-CPOOL_CONN_INFO.html
---

# V$CPOOL_CONN_INFO

V$CPOOL_CONN_INFO displays connection information about each connection to the connection broker.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CMON_ADDR | RAW(4 | 8) |  |
| SESSION_ADDR | RAW(4 | 8) |  |
| CONNECTION_ADDR | RAW(4 | 8) |  |
| USERNAME | VARCHAR2(1024) |  |
| PROXY_USER | VARCHAR2(1024) |  |
| CCLASS_NAME | VARCHAR2(1024) |  |
| PURITY | VARCHAR2(1024) |  |
| TAG | VARCHAR2(1024) |  |
| SERVICE | VARCHAR2(64) |  |
| PROCESS_ID | VARCHAR2(24) |  |
| PROGRAM | VARCHAR2(48) |  |
| MACHINE | VARCHAR2(64) |  |
| TERMINAL | VARCHAR2(30) |  |
| CONNECTION_MODE | VARCHAR2(1024) |  |
| CONNECTION_STATUS | VARCHAR2(10) |  |
| CLIENT_REGID | NUMBER |  |
| CURSTATUS_TIME | NUMBER |  |
| IDLE_TIME | NUMBER |  |
| ACTIVE_TIME | NUMBER |  |
| WAIT_TIME | NUMBER |  |
| THINK_TIME | NUMBER |  |
| LAST_IDLE_TIME | NUMBER |  |
| LAST_ACTIVE_TIME | NUMBER |  |
| LAST_WAIT_TIME | NUMBER |  |
| LAST_THINK_TIME | NUMBER |  |
| NUMGETS | NUMBER |  |
| NUMHITS | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content