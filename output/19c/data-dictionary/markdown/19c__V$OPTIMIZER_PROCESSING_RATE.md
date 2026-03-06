---
id: 19c__V$OPTIMIZER_PROCESSING_RATE
name: V$OPTIMIZER_PROCESSING_RATE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-OPTIMIZER_PROCESSING_RATE.html
---

# V$OPTIMIZER_PROCESSING_RATE

V$OPTIMIZER_PROCESSING_RATE displays the processing rates used by the optimizer to compute degree of parallelism.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ADDRESS | RAW(4| 8) |  |
| OPERATION_NAME | VARCHAR2(64) |  |
| MANUAL_VALUE | VARCHAR2(10) |  |
| CALIBRATION_VALUE | VARCHAR2(10) |  |
| DEFAULT_VALUE | VARCHAR2(10) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: You can manipulate these rates using these procedures for the DBMS_STATS package: SET_PROCESSING_RATE DELETE_PROCESSING_RATE GATHER_PROCESSING_RATE See Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_STATS package. Note: You can manipulate these rates using these procedures for the DBMS_STATS package: SET_PROCESSING_RATE DELETE_PROCESSING_RATE GATHER_PROCESSING_RATE See Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_STATS package.