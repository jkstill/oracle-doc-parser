---
id: 19c__V$ASM_FILEGROUP_PROPERTY
name: V$ASM_FILEGROUP_PROPERTY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ASM_FILEGROUP_PROPERTY.html
---

# V$ASM_FILEGROUP_PROPERTY

V$ASM_FILEGROUP_PROPERTY describes all the properties of every Oracle Automatic Storage Management (Oracle ASM) File Group.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| GROUP_NUMBER | NUMBER |  |
| FILEGROUP_NUMBER | NUMBER |  |
| COMPOUND_INDEX | NUMBER |  |
| PROPERTY_INDEX | NUMBER |  |
| INCARNATION | NUMBER |  |
| FILE_TYPE | VARCHAR2(30) |  |
| NAME | VARCHAR2(64) |  |
| VALUE | VARCHAR2(256) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content In both Oracle ASM and Oracle Database instances, V$ASM_FILEGROUP_PROPERTY will display one row for every property of every file type of every File Group contained in every Disk Group mounted by the instance. File Group properties are only displayed for File Groups on Disk Groups where COMPATIBLE.ASM is set to 12.2 or higher. Note: There will not be an entry for the default File Group. Note: There will not be an entry for the default File Group. See Also: " V$ASM_FILEGROUP " See Also: " V$ASM_FILEGROUP "