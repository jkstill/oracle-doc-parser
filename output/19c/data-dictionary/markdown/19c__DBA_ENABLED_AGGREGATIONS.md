---
id: 19c__DBA_ENABLED_AGGREGATIONS
name: DBA_ENABLED_AGGREGATIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_ENABLED_AGGREGATIONS.html
---

# DBA_ENABLED_AGGREGATIONS

DBA_ENABLED_AGGREGATIONS displays information about enabled on-demand statistic aggregation.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| AGGREGATION_TYPE | VARCHAR2(21) | Type of the aggregation: CLIENT_ID SERVICE SERVICE_MODULE SERVICE_MODULE_ACTION |
| PRIMARY_ID | VARCHAR2(64) | Primary qualifier (specific client identifier or service name) |
| QUALIFIER_ID1 | VARCHAR2(48) | Secondary qualifier (specific module name) |
| QUALIFIER_ID2 | VARCHAR2(32) | Additional qualifier (specific action name) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content