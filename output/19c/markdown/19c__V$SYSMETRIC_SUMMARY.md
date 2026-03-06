---
id: 19c__V$SYSMETRIC_SUMMARY
name: V$SYSMETRIC_SUMMARY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: internal
tags: [dynamic_performance]
source_file: V-SYSMETRIC_SUMMARY.html
---

# V$SYSMETRIC_SUMMARY

Begin time of the interval

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

See Also: " DBA_HIST_SYSMETRIC_SUMMARY " " V$CON_SYSMETRIC_SUMMARY " " DBA_HIST_CON_SYSMETRIC_SUMM " See Also: " DBA_HIST_SYSMETRIC_SUMMARY " " V$CON_SYSMETRIC_SUMMARY " " DBA_HIST_CON_SYSMETRIC_SUMM "