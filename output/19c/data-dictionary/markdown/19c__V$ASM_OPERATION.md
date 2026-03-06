---
id: 19c__V$ASM_OPERATION
name: V$ASM_OPERATION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ASM_OPERATION.html
---

# V$ASM_OPERATION

In an Oracle Automatic Storage Management (Oracle ASM) instance, V$ASM_OPERATION displays one row for every active Oracle ASM long running operation executing in the Oracle ASM instance.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| GROUP_NUMBER | NUMBER |  |
| OPERATION | CHAR(5) |  |
| PASS | VARCHAR2(9) |  |
| STATE | VARCHAR2(4) |  |
| POWER | NUMBER |  |
| ACTUAL | NUMBER |  |
| SOFAR | NUMBER |  |
| EST_WORK | NUMBER |  |
| EST_RATE | NUMBER |  |
| EST_MINUTES | NUMBER |  |
| ERROR_CODE | VARCHAR2(44) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information See Also: Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information