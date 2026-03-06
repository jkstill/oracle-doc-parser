---
id: 19c__V$STATNAME
name: V$STATNAME
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-STATNAME.html
---

# V$STATNAME

V$STATNAME displays decoded statistic names for the statistics shown in the V$SESSTAT and V$SYSSTAT tables.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| STATISTIC# | NUMBER |  |
| NAME | VARCHAR2(64) |  |
| CLASS | NUMBER |  |
| STAT_ID | NUMBER |  |
| DISPLAY_NAME | VARCHAR2(64) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content On some platforms, the NAME and CLASS columns contain additional operating system-specific statistics. See Also: " V$SESSTAT " and " V$SYSSTAT " " Statistics Descriptions " for statistic descriptions Your operating system-specific Oracle documentation See Also: " V$SESSTAT " and " V$SYSSTAT " " Statistics Descriptions " for statistic descriptions Your operating system-specific Oracle documentation