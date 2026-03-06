---
id: 19c__DBA_MVREF_STATS_SYS_DEFAULTS
name: DBA_MVREF_STATS_SYS_DEFAULTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_MVREF_STATS_SYS_DEFAULTS.html
---

# DBA_MVREF_STATS_SYS_DEFAULTS

DBA_MVREF_STATS_SYS_DEFAULTS displays the system-wide defaults for the refresh history statistics properties for materialized views. These values can be altered with the SET_SYSTEM_DEFAULTS procedure by a database administrator.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PARAMETER_NAME | CHAR(16) | Value of the parameter_name parameter: COLLECTION_LEVEL RETENTION_PERIOD |
| VALUE | VARCHAR2(40) | The system-wide default value for the parameter |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View This view contains exactly two rows corresponding to the collection-level and retention-period properties; their initial values are TYPICAL and 31 respectively. USER_MVREF_STATS_SYS_DEFAULTS displays the system-wide defaults for the refresh history statistics properties for materialized views accessible to the current user. These values can be altered with the SET_SYSTEM_DEFAULTS procedure by a database administrator. See Also: " USER_MVREF_STATS_SYS_DEFAULTS " See Also: " USER_MVREF_STATS_SYS_DEFAULTS "