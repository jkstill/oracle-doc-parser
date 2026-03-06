---
id: 19c__V$ASM_ALIAS
name: V$ASM_ALIAS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ASM_ALIAS.html
---

# V$ASM_ALIAS

In an Oracle Automatic Storage Management (Oracle ASM) instance, V$ASM_ALIAS displays one row for every alias present in every disk group mounted by the Oracle ASM instance.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAME | VARCHAR2(70) |  |
| GROUP_NUMBER | NUMBER |  |
| FILE_NUMBER | NUMBER |  |
| FILE_INCARNATION | NUMBER |  |
| ALIAS_INDEX | NUMBER |  |
| ALIAS_INCARNATION | NUMBER |  |
| PARENT_INDEX | NUMBER |  |
| REFERENCE_INDEX | NUMBER |  |
| ALIAS_DIRECTORY | VARCHAR2(1) |  |
| SYSTEM_CREATED | VARCHAR2(1) |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information See Also: Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information