---
id: 19c__V$ASM_TEMPLATE
name: V$ASM_TEMPLATE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ASM_TEMPLATE.html
---

# V$ASM_TEMPLATE

In an Oracle Automatic Storage Management (Oracle ASM) instance, V$ASM_TEMPLATE displays one row for every template present in every disk group mounted by the Oracle ASM instance.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| GROUP_NUMBER | NUMBER |  |
| ENTRY_NUMBER | NUMBER |  |
| REDUNDANCY | VARCHAR2(6) |  |
| STRIPE | VARCHAR2(6) |  |
| SYSTEM | VARCHAR2(1) |  |
| NAME | VARCHAR2(30) |  |
| PRIMARY_REGION | VARCHAR2(4) |  |
| MIRROR_REGION | VARCHAR2(4) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content In a database instance, V$ASM_TEMPLATE displays one row for every template present in every disk group mounted by the Oracle ASM instance with which the database instance communicates. See Also: Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information See Also: Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information