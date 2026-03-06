---
id: 19c__V$SQL_PLAN_MONITOR
name: V$SQL_PLAN_MONITOR
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dynamic_performance]
source_file: V-SQL_PLAN_MONITOR.html
---

# V$SQL_PLAN_MONITOR

To eliminate the overhead of SQL plan monitoring, statistics collected for each operation of the plan do not record timing information such as elapsed time, CPU time, or I/O time. Instead, this timing information can be estimated quite accurately by joining V$SQL_PLAN_MONITOR with V$ACTIVE_SESSION_HISTORY on SQL_ID , SQL_EXEC_START , SQL_EXEC_ID , and SQL_PLAN_LINE_ID (simply named PLAN_LINE_ID in V$SQL_PLAN_MONITOR ). The result of that join is a sample of the activity performed by each operation in the plan, from which an estimate of CPU time and wait time can be derived. This can be achieved by breaking statement level monitoring time statistics found in V$SQL_MONITOR in proportion to the number of samples found in V$ACTIVE_SESSION_HISTORY for the corresponding activity type.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CON_ID | NUMBER |  |
| KEY | NUMBER |  |
| STATUS | VARCHAR2(19) |  |
| FIRST_REFRESH_TIME | DATE |  |
| LAST_REFRESH_TIME | DATE |  |
| FIRST_CHANGE_TIME | DATE |  |
| LAST_CHANGE_TIME | DATE |  |
| REFRESH_COUNT | NUMBER |  |
| SID | NUMBER |  |
| PROCESS_NAME | VARCHAR2(5) |  |
| SQL_ID | VARCHAR2(13) |  |
| SQL_EXEC_START | DATE |  |
| SQL_EXEC_ID | NUMBER |  |
| SQL_PLAN_HASH_VALUE | NUMBER |  |
| SQL_CHILD_ADDRESS | RAW(4 | 8) |  |
| PLAN_PARENT_ID | NUMBER |  |
| PLAN_LINE_ID | NUMBER |  |
| PLAN_OPERATION | VARCHAR2(30) |  |
| PLAN_OPTIONS | VARCHAR2(30) |  |
| PLAN_OBJECT_OWNER | VARCHAR2(128) |  |
| PLAN_OBJECT_NAME | VARCHAR2(128) |  |
| PLAN_OBJECT_TYPE | VARCHAR2(80) |  |
| PLAN_DEPTH | NUMBER |  |
| PLAN_POSITION | NUMBER |  |
| PLAN_COST | NUMBER |  |
| PLAN_CARDINALITY | NUMBER |  |
| PLAN_BYTES | NUMBER |  |
| PLAN_TIME | NUMBER |  |
| PLAN_PARTITION_START | VARCHAR2(256) |  |
| PLAN_PARTITION_STOP | VARCHAR2(256) |  |
| PLAN_CPU_COST | NUMBER |  |
| PLAN_IO_COST | NUMBER |  |
| PLAN_TEMP_SPACE | NUMBER |  |
| STARTS | NUMBER |  |
| OUTPUT_ROWS | NUMBER |  |
| IO_INTERCONNECT_BYTES | NUMBER |  |
| PHYSICAL_READ_REQUESTS | NUMBER |  |
| PHYSICAL_READ_BYTES | NUMBER |  |
| PHYSICAL_WRITE_REQUESTS | NUMBER |  |
| PHYSICAL_WRITE_BYTES | NUMBER |  |
| WORKAREA_MEM | NUMBER |  |
| WORKAREA_MAX_MEM | NUMBER |  |
| WORKAREA_TEMPSEG | NUMBER |  |
| WORKAREA_MAX_TEMPSEG | NUMBER |  |
| OTHERSTAT_GROUP_ID | NUMBER |  |
| OTHERSTAT_1_ID | NUMBER |  |
| OTHERSTAT_1_TYPE | NUMBER |  |
| OTHERSTAT_1_VALUE | NUMBER |  |
| OTHERSTAT_2_ID | NUMBER |  |
| OTHERSTAT_2_TYPE | NUMBER |  |
| OTHERSTAT_2_VALUE | NUMBER |  |
| OTHERSTAT_3_ID | NUMBER |  |
| OTHERSTAT_3_TYPE | NUMBER |  |
| OTHERSTAT_3_VALUE | NUMBER |  |
| OTHERSTAT_4_ID | NUMBER |  |
| OTHERSTAT_4_TYPE | NUMBER |  |
| OTHERSTAT_4_VALUE | NUMBER |  |
| OTHERSTAT_5_ID | NUMBER |  |
| OTHERSTAT_5_TYPE | NUMBER |  |
| OTHERSTAT_5_VALUE | NUMBER |  |
| OTHERSTAT_6_ID | NUMBER |  |
| OTHERSTAT_6_TYPE | NUMBER |  |
| OTHERSTAT_6_VALUE | NUMBER |  |
| OTHERSTAT_7_ID | NUMBER |  |
| OTHERSTAT_7_TYPE | NUMBER |  |
| OTHERSTAT_7_VALUE | NUMBER |  |
| OTHERSTAT_8_ID | NUMBER |  |
| OTHERSTAT_8_TYPE | NUMBER |  |
| OTHERSTAT_8_VALUE | NUMBER |  |
| OTHERSTAT_9_ID | NUMBER |  |
| OTHERSTAT_9_TYPE | NUMBER |  |
| OTHERSTAT_9_VALUE | NUMBER |  |
| OTHERSTAT_10_ID | NUMBER |  |
| OTHERSTAT_10_TYPE | NUMBER |  |
| OTHERSTAT_10_VALUE | NUMBER |  |
| OTHER_XML | CLOB |  |
| PLAN_OPERATION_INACTIVE | NUMBER |  |

## Usage Notes

See Also: " V$SQL_MONITOR_STATNAME " See Also: " V$SQL_MONITOR_STATNAME "