---
id: 19c__V$SYSMETRIC
name: V$SYSMETRIC
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: internal
tags: [dynamic_performance]
source_file: V-SYSMETRIC.html
---

# V$SYSMETRIC

V$SYSMETRIC displays the system metric values captured for the most current time interval for both the long duration (60-second) and short duration (15-second) system metrics.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| BEGIN_TIME | DATE |  |
| END_TIME | DATE |  |
| INTSIZE_CSEC | NUMBER |  |
| GROUP_ID | NUMBER |  |
| METRIC_ID | NUMBER |  |
| METRIC_NAME | VARCHAR2(64) |  |
| VALUE | NUMBER |  |
| METRIC_UNIT | VARCHAR2(64) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: " DBA_HIST_SYS_TIME_MODEL " " V$CON_SYSMETRIC " " DBA_HIST_CON_SYS_TIME_MODEL " See Also: " DBA_HIST_SYS_TIME_MODEL " " V$CON_SYSMETRIC " " DBA_HIST_CON_SYS_TIME_MODEL "