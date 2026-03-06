---
id: 19c__V$LOGMNR_PROCESS
name: V$LOGMNR_PROCESS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-LOGMNR_PROCESS.html
---

# V$LOGMNR_PROCESS

V$LOGMNR_PROCESS identifies all processes attached to an active LogMiner persistent session.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SESSION_ID | NUMBER |  |
| PID | NUMBER |  |
| SPID | VARCHAR2(24) |  |
| ROLE | VARCHAR2(32) |  |
| USERNAME | VARCHAR2(15) |  |
| SID | NUMBER |  |
| SERIAL# | NUMBER |  |
| LATCHWAIT | VARCHAR2(16) |  |
| LATCHSPIN | VARCHAR2(16) |  |
| WORK_MICROSEC | VARCHAR2(21) |  |
| OVERHEAD_MICROSEC | VARCHAR2(21) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content (A persistent LogMiner session is created either by starting Data Guard SQL Apply on a logical standby database for the first time or by creating Replication capture.) This view can be joined with either the V$SESSION view or the V$PROCESS view to gather process-specific information. See Also: " V$SESSION " " V$PROCESS " See Also: " V$SESSION " " V$PROCESS "