---
id: 19c__V$SQL_MONITOR_STATNAME
name: V$SQL_MONITOR_STATNAME
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-SQL_MONITOR_STATNAME.html
---

# V$SQL_MONITOR_STATNAME

V$SQL_MONITOR_STATNAME provides information about the plan line statistics exposed in V$SQL_PLAN_MONITOR . A plan line statistic is identified by its group ID (column GROUP_ID ) and its ID (column ID ).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CON_ID | NUMBER |  |
| ID | NUMBER |  |
| GROUP_ID | NUMBER |  |
| NAME | VARCHAR2(40) |  |
| DESCRIPTION | VARCHAR2(200) |  |
| TYPE | NUMBER |  |
| FLAGS | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: " V$SQL_PLAN_MONITOR " See Also: " V$SQL_PLAN_MONITOR "