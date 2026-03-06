---
id: 19c__V$ASM_ESTIMATE
name: V$ASM_ESTIMATE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ASM_ESTIMATE.html
---

# V$ASM_ESTIMATE

V$ASM_ESTIMATE displays an estimate of the work involved in execution plans for Oracle Automatic Storage Management (Oracle ASM) disk group rebalance and resync operations.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| GROUP_NUMBER | NUMBER |  |
| STATEMENT_ID | VARCHAR2(30) |  |
| TIMESTAMP | DATE |  |
| EST_WORK | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information See Also: Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information