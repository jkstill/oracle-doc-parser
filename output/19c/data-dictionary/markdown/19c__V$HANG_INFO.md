---
id: 19c__V$HANG_INFO
name: V$HANG_INFO
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-HANG_INFO.html
---

# V$HANG_INFO

V$HANG_INFO displays information about hangs found on the cluster.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| HANG_ID | NUMBER |  |
| HANG_CHAIN_SESSIONS | NUMBER |  |
| TOTAL_HUNG_SESSIONS | NUMBER |  |
| HANG_TYPE | VARCHAR2(18) |  |
| HANG_CREATE_TIME | VARCHAR2(20) |  |
| HANG_RESOLVE_TIME | VARCHAR2(20) |  |
| IGNORED_HANG | VARCHAR2(1) |  |
| RESOLUTION_ATTEMPTED | VARCHAR2(1) |  |
| GLOBAL_HANG | VARCHAR2(1) |  |
| ESCALATED_HANG | VARCHAR2(1) |  |
| RESOLUTION_STATUS | VARCHAR2(45) |  |
| VICTIM_INSTANCE | NUMBER |  |
| VICTIM_SESSION_ID | NUMBER |  |
| VICTIM_SERIAL# | NUMBER |  |
| VICTIM_OSPID | VARCHAR2(24) |  |
| FATAL_BACKGROUND | VARCHAR2(1) |  |
| PNAME | VARCHAR2(5) |  |
| WAIT_EVENT_TEXT | VARCHAR2(64) |  |
| VICTIM_QOS_PC_RANK | VARCHAR2(12) |  |
| VICTIM_QOS_PC_ITT | NUMBER |  |
| VICTIM_QOS_PC_RTT | NUMBER |  |
| VICTIM_QOS_PC_KEY | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content A hang can be an open wait chain or closed wait chain (cycle or deadlock). A wait chain is a series of sessions that are blocking one another. Each row represents a hang and describes how severe the hang is. This view also includes the victim or final blocker of the hang. See Also: " V$HANG_SESSION_INFO " " V$HANG_STATISTICS " " DBA_HANG_MANAGER_PARAMETERS " See Also: " V$HANG_SESSION_INFO " " V$HANG_STATISTICS " " DBA_HANG_MANAGER_PARAMETERS "