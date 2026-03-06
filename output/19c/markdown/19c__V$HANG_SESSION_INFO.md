---
id: 19c__V$HANG_SESSION_INFO
name: V$HANG_SESSION_INFO
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-HANG_SESSION_INFO.html
---

# V$HANG_SESSION_INFO

V$HANG_SESSION_INFO displays information about sessions involved in hangs described by V$HANG_INFO .

## Columns

| Column | Type | Description |
|--------|------|-------------|
| HANG_ID | NUMBER |  |
| INSTANCE | NUMBER |  |
| SID | NUMBER |  |
| SERIAL# | NUMBER |  |
| OSPID | VARCHAR2(24) |  |
| FATAL_BACKGROUND | VARCHAR2(1) |  |
| ROOT | VARCHAR2(1) |  |
| PNAME | VARCHAR2(5) |  |
| WAIT_EVENT_TEXT | VARCHAR2(64) |  |
| QOS_PC_RANK | VARCHAR2(12) |  |
| QOS_PC_ITT | NUMBER |  |
| QOS_PC_RTT | NUMBER |  |
| QOS_PC_KEY | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Each row with the same HANG_ID describes a session that is in the hang wait chain described by the row with the same HANG_ID in V$HANG_INFO . This session is blocked by the victim or final blocker of that hang. See Also: " V$HANG_INFO " " V$HANG_STATISTICS " " DBA_HANG_MANAGER_PARAMETERS " See Also: " V$HANG_INFO " " V$HANG_STATISTICS " " DBA_HANG_MANAGER_PARAMETERS "