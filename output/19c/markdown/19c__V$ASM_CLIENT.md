---
id: 19c__V$ASM_CLIENT
name: V$ASM_CLIENT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ASM_CLIENT.html
---

# V$ASM_CLIENT

In an Oracle Automatic Storage Management (Oracle ASM) instance, V$ASM_CLIENT identifies databases using disk groups managed by the Oracle ASM instance.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| GROUP_NUMBER | NUMBER |  |
| INSTANCE_NAME | VARCHAR2(64) |  |
| DB_NAME | VARCHAR2(8) |  |
| CLUSTER_NAME | VARCHAR2(31) |  |
| STATUS | VARCHAR2(12) |  |
| SOFTWARE_VERSION | VARCHAR2(60) |  |
| COMPATIBLE_VERSION | VARCHAR2(60) |  |
| CON_ID | NUMBER |  |

## Usage Notes

In a database instance, V$ASM_CLIENT displays information about the Oracle ASM instance if the database has any open Oracle ASM files. See Also: Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information See Also: Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information