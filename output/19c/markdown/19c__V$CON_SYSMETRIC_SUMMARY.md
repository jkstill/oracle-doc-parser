---
id: 19c__V$CON_SYSMETRIC_SUMMARY
name: V$CON_SYSMETRIC_SUMMARY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: internal
tags: [dynamic_performance]
source_file: V-CON_SYSMETRIC_SUMMARY.html
---

# V$CON_SYSMETRIC_SUMMARY

V$CON_SYSMETRIC_SUMMARY displays a summary of all system metric values for the PDB long-duration system metrics. The average, maximum value, minimum value, and the value of one standard deviation for the last hour are displayed for each metric item.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| BEGIN_TIME | DATE |  |
| END_TIME | DATE |  |
| INTSIZE_CSEC | NUMBER |  |
| GROUP_ID | NUMBER |  |
| METRIC_ID | NUMBER |  |
| METRIC_NAME | VARCHAR2(64) |  |
| NUM_INTERVAL | NUMBER |  |
| MAXVAL | NUMBER |  |
| MINVAL | NUMBER |  |
| AVERAGE | NUMBER |  |
| STANDARD_DEVIATION | NUMBER |  |
| METRIC_UNIT | VARCHAR2(64) |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: " V$SYSMETRIC_HISTORY " " DBA_HIST_SYSMETRIC_SUMMARY " " V$SYSMETRIC_SUMMARY " See Also: " V$SYSMETRIC_HISTORY " " DBA_HIST_SYSMETRIC_SUMMARY " " V$SYSMETRIC_SUMMARY "