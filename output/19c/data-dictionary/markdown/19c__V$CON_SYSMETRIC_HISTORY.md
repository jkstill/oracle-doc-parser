---
id: 19c__V$CON_SYSMETRIC_HISTORY
name: V$CON_SYSMETRIC_HISTORY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: internal
tags: [dynamic_performance]
source_file: V-CON_SYSMETRIC_HISTORY.html
---

# V$CON_SYSMETRIC_HISTORY

V$CON_SYSMETRIC_HISTORY displays all PDB long duration (60-second with 1 hour history) system metric values available in the database.

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

Previous Next JavaScript must be enabled to correctly display this content See Also: " DBA_HIST_CON_SYSMETRIC_HIST " " DBA_HIST_SYSMETRIC_HISTORY " " V$SYSMETRIC_HISTORY " See Also: " DBA_HIST_CON_SYSMETRIC_HIST " " DBA_HIST_SYSMETRIC_HISTORY " " V$SYSMETRIC_HISTORY "