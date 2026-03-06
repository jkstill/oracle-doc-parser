---
id: 19c__V$ASM_DBCLONE_INFO
name: V$ASM_DBCLONE_INFO
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ASM_DBCLONE_INFO.html
---

# V$ASM_DBCLONE_INFO

V$ASM_DBCLONE_INFO shows the relationship between the parent database and point-in-time database clones.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| GROUP_NUMBER | NUMBER |  |
| DBCLONE_NAME | VARCHAR2(128) |  |
| MIRRORCOPY_NAME | VARCHAR2(128) |  |
| DBCLONE_STATUS | VARCHAR2(128) |  |
| PARENT_DBNAME | VARCHAR2(128) |  |
| PARENT_FILEGROUP_NAME | VARCHAR2(128) |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: Oracle Automatic Storage Management Administrator's Guide for information about point-in-time database clones See Also: Oracle Automatic Storage Management Administrator's Guide for information about point-in-time database clones