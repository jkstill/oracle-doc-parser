---
id: 19c__DBA_WORKLOAD_FILTERS
name: DBA_WORKLOAD_FILTERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_WORKLOAD_FILTERS.html
---

# DBA_WORKLOAD_FILTERS

DBA_WORKLOAD_FILTERS displays all the workload filters that have been defined in the current database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TYPE | VARCHAR2(30) | Type of the workload filter ( CAPTURE or REPLAY ) |
| ID | VARCHAR2(40) | Sequence number of the workload filter |
| STATUS | VARCHAR2(6) | Status of the workload filter: NEW - This filter will be used by the next subsequent operation such as the next workload capture. IN USE - This filter is currently being used by an operation that is in progress such as an active workload capture. USED - This filter was used in the past by some operation such as a past workload capture. |
| SET_NAME | VARCHAR2(1000) | Name of the filter set to which the filter belongs |
| NAME | VARCHAR2(128) | Name of the workload filter |
| ATTRIBUTE | VARCHAR2(128) | Name of the attribute on which the filter is defined |
| VALUE | VARCHAR2(4000) | Value of the attribute on which the filter is defined. Wildcards such as % and _ are supported if the attribute is of string type. |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content In Oracle Database 11 g , only workload filters of type CAPTURE are supported. Starting with Oracle Database 11 g R2, filters of type REPLAY are supported.