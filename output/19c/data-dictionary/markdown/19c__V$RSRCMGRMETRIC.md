---
id: 19c__V$RSRCMGRMETRIC
name: V$RSRCMGRMETRIC
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-RSRCMGRMETRIC.html
---

# V$RSRCMGRMETRIC

V$RSRCMGRMETRIC displays information about resources consumed and wait times per consumer group.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| BEGIN_TIME | DATE |  |
| END_TIME | DATE |  |
| INTSIZE_CSEC | NUMBER |  |
| SEQUENCE# | NUMBER |  |
| CONSUMER_GROUP_ID | NUMBER |  |
| CONSUMER_GROUP_NAME | VARCHAR2(30) |  |
| CPU_CONSUMED_TIME | NUMBER |  |
| CPU_WAIT_TIME | NUMBER |  |
| NUM_CPUS | NUMBER |  |
| RUNNING_SESSIONS_LIMIT | NUMBER |  |
| AVG_RUNNING_SESSIONS | NUMBER |  |
| AVG_WAITING_SESSIONS | NUMBER |  |
| CPU_UTILIZATION_LIMIT | NUMBER |  |
| AVG_CPU_UTILIZATION | NUMBER |  |
| CPU_DECISIONS | NUMBER |  |
| CPU_DECISIONS_EXCLUSIVE | NUMBER |  |
| CPU_DECISIONS_WON | NUMBER |  |
| IO_REQUESTS | NUMBER |  |
| IO_MEGABYTES | NUMBER |  |
| AVG_ACTIVE_PARALLEL_STMTS | NUMBER |  |
| AVG_QUEUED_PARALLEL_STMTS | NUMBER |  |
| AVG_ACTIVE_PARALLEL_SERVERS | NUMBER |  |
| AVG_QUEUED_PARALLEL_SERVERS | NUMBER |  |
| PARALLEL_SERVERS_LIMIT | NUMBER |  |
| PLAN_NAME | VARCHAR2(30) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content When the STATISTICS_LEVEL is set to TYPICAL or ALL , this view contains information about CPU utilization and wait times even when no Resource Manager plan is set or when the Resource Manager plan does not monitor CPU or session resources. Metrics are collected and stored every minute when CPU utilization is not being monitored. See Also: " STATISTICS_LEVEL " See Also: " STATISTICS_LEVEL "