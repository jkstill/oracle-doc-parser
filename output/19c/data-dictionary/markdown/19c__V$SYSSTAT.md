---
id: 19c__V$SYSSTAT
name: V$SYSSTAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-SYSSTAT.html
---

# V$SYSSTAT

V$SYSSTAT displays system statistics. To find the name of the statistic associated with each statistic number ( STATISTIC# ), query the V$STATNAME view.

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

Previous Next JavaScript must be enabled to correctly display this content Note: This view returns instance-wide data and a value of 0 in the CON_ID column when queried from the root of a CDB. See Also: " V$STATNAME " and " Statistics Descriptions " Note: This view returns instance-wide data and a value of 0 in the CON_ID column when queried from the root of a CDB. See Also: " V$STATNAME " and " Statistics Descriptions "