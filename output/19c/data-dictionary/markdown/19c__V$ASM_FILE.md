---
id: 19c__V$ASM_FILE
name: V$ASM_FILE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ASM_FILE.html
---

# V$ASM_FILE

In an Oracle Automatic Storage Management (Oracle ASM) instance, V$ASM_FILE displays one row for each file in each disk group mounted by the Oracle ASM instance.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| GROUP_NUMBER | NUMBER |  |
| FILE_NUMBER | NUMBER |  |
| COMPOUND_INDEX | NUMBER |  |
| INCARNATION | NUMBER |  |
| BLOCK_SIZE | NUMBER |  |
| BLOCKS | NUMBER |  |
| BYTES | NUMBER |  |
| SPACE | NUMBER |  |
| TYPE | VARCHAR2(64) |  |
| REDUNDANCY | VARCHAR2(6) |  |
| STRIPED | VARCHAR2(6) |  |
| CREATION_DATE | DATE |  |
| MODIFICATION_DATE | DATE |  |
| REDUNDANCY_LOWERED | VARCHAR2(1) |  |
| PERMISSIONS | VARCHAR2(16) |  |
| USER_NUMBER | NUMBER |  |
| USER_INCARNATION | NUMBER |  |
| USERGROUP_NUMBER | NUMBER |  |
| USERGROUP_INCARNATION | NUMBER |  |
| PRIMARY_REGION | VARCHAR2(4) |  |
| MIRROR_REGION | VARCHAR2(4) |  |
| HOT_READS | NUMBER |  |
| HOT_WRITES | NUMBER |  |
| HOT_BYTES_READ | NUMBER |  |
| HOT_BYTES_WRITTEN | NUMBER |  |
| COLD_READS | NUMBER |  |
| COLD_WRITES | NUMBER |  |
| COLD_BYTES_READ | NUMBER |  |
| COLD_BYTES_WRITTEN | NUMBER |  |
| FILEGROUP_NUMBER | NUMBER |  |
| FILEGROUP_INCARNATION | NUMBER |  |
| REMIRROR | VARCHAR2(1) |  |
| PARENT_FILNUM | NUMBER |  |
| PARENT_FILNUMINC | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content For example, if there are three disk groups and five files in each, fifteen rows are displayed (unless the query is qualified with a WHERE clause). See Also: Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information See Also: Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information