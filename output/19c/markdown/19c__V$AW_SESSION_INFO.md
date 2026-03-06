---
id: 19c__V$AW_SESSION_INFO
name: V$AW_SESSION_INFO
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-AW_SESSION_INFO.html
---

# V$AW_SESSION_INFO

V$AW_SESSION_INFO provides information about each active session.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SESSION_ID | NUMBER |  |
| CLIENT_TYPE | VARCHAR2(64) |  |
| SESSION_STATE | VARCHAR2(64) |  |
| SESSION_HANDLE | NUMBER |  |
| USERID | VARCHAR2(64) |  |
| TOTAL_TRANSACTION | NUMBER |  |
| TRANSACTION_TIME | NUMBER |  |
| TOTAL_TRANSACTION_TIME | NUMBER |  |
| AVERAGE_TRANSACTION_TIME | NUMBER |  |
| TRANSACTION_CPU_TIME | NUMBER |  |
| TOTAL_TRANSACTION_CPU_TIME | NUMBER |  |
| AVERAGE_TRANSACTION_CPU_TIME | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

A transaction is a single exchange between a client session and Oracle OLAP. Multiple commands can execute within a single transaction.