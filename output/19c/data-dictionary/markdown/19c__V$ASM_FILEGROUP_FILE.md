---
id: 19c__V$ASM_FILEGROUP_FILE
name: V$ASM_FILEGROUP_FILE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ASM_FILEGROUP_FILE.html
---

# V$ASM_FILEGROUP_FILE

V$ASM_FILEGROUP_FILE lists all the Oracle Automatic Storage Management (Oracle ASM) files associated with each File Group.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| GROUP_NUMBER | NUMBER |  |
| FILEGROUP_NUMBER | NUMBER |  |
| FILEGROUP_INCARN | NUMBER |  |
| FILE_NUMBER | NUMBER |  |
| INCARNATION | NUMBER |  |
| COMPOUND_INDEX | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content In both Oracle ASM and Oracle Database instances, V$ASM_FILEGROUP_FILE will display one row for every file associated with a File Group contained in every Disk Group mounted by the instance. See Also: " V$ASM_FILE " " V$ASM_FILEGROUP " See Also: " V$ASM_FILE " " V$ASM_FILEGROUP "