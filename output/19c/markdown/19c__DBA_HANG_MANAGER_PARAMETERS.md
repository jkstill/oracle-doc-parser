---
id: 19c__DBA_HANG_MANAGER_PARAMETERS
name: DBA_HANG_MANAGER_PARAMETERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: configuration
tags: [dba]
source_file: DBA_HANG_MANAGER_PARAMETERS.html
---

# DBA_HANG_MANAGER_PARAMETERS

DBA_HANG_MANAGER_PARAMETERS shows the available user tunable Hang Manager parameters and their values.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAME | VARCHAR2(40) | String representation of the parameter names |
| CURRENT_VALUE | VARCHAR2(20) | String representation of the parameter values |
| CURRENT_TIME | DATE | Time when the current value was set |
| PREVIOUS_VALUE | VARCHAR2(20) | String representation of the parameter value from the previous update |
| PREVIOUS_TIME | DATE | Time when the previous value was set |

## Usage Notes

Note: " V$HANG_INFO " " V$HANG_SESSION_INFO " " V$HANG_STATISTICS " Note: " V$HANG_INFO " " V$HANG_SESSION_INFO " " V$HANG_STATISTICS "