---
id: 19c__V$CON_SYSMETRIC
name: V$CON_SYSMETRIC
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: internal
tags: [dynamic_performance]
source_file: V-CON_SYSMETRIC.html
---

# V$CON_SYSMETRIC

V$CON_SYSMETRIC displays the system metric values captured for the most current time interval for the PDB long duration (60-second) system metrics.

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

Previous Next JavaScript must be enabled to correctly display this content See Also: " DBA_HIST_CON_SYS_TIME_MODEL " " DBA_HIST_SYS_TIME_MODEL " " V$SYSMETRIC " See Also: " DBA_HIST_CON_SYS_TIME_MODEL " " DBA_HIST_SYS_TIME_MODEL " " V$SYSMETRIC "