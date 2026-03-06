---
id: 19c__DBA_SQL_MANAGEMENT_CONFIG
name: DBA_SQL_MANAGEMENT_CONFIG
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dba]
source_file: DBA_SQL_MANAGEMENT_CONFIG.html
---

# DBA_SQL_MANAGEMENT_CONFIG

DBA_SQL_MANAGEMENT_CONFIG displays the configuration parameters of the SQL management base.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PARAMETER_NAME | VARCHAR2(128) | Name of the configuration parameter: SPACE_BUDGET_PERCENT PLAN_RETENTION_WEEKS AUTO_CAPTURE_SQL_TEXT AUTO_CAPTURE_PARSING_SCHEMA_NAME AUTO_CAPTURE_MODULE AUTO_CAPTURE_ACTION |
| PARAMETER_VALUE | VARCHAR2(4000) | Value of the configuration parameter |
| LAST_MODIFIED | TIMESTAMP(6) | Time the parameter value was last updated |
| MODIFIED_BY | VARCHAR2(128) | User who last updated the parameter value |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content You must have the DBA role in order to change the configuration parameter values.