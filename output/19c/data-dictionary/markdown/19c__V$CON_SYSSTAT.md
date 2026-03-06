---
id: 19c__V$CON_SYSSTAT
name: V$CON_SYSSTAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-CON_SYSSTAT.html
---

# V$CON_SYSSTAT

V$CON_SYSSTAT displays system statistics, including OLAP kernel statistics for the container from which it is queried. To find the name of the statistic associated with each statistic number ( STATISTIC# ), query the V$STATNAME view.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| STATISTIC# | NUMBER |  |
| NAME | VARCHAR2(64) |  |
| CLASS | NUMBER |  |
| VALUE | NUMBER |  |
| STAT_ID | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: " V$STATNAME " and " Statistics Descriptions " See Also: " V$STATNAME " and " Statistics Descriptions "