---
id: 19c__V$ASM_FILEGROUP
name: V$ASM_FILEGROUP
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ASM_FILEGROUP.html
---

# V$ASM_FILEGROUP

V$ASM_FILEGROUP describes the properties of the Oracle Automatic Storage Management (Oracle ASM) File Groups.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| GROUP_NUMBER | NUMBER |  |
| FILEGROUP_NUMBER | NUMBER |  |
| INCARNATION | NUMBER |  |
| COMPOUND_INDEX | NUMBER |  |
| NAME | VARCHAR2(128) |  |
| CLIENT_TYPE | NUMBER |  |
| CLIENT_NAME | VARCHAR2(128) |  |
| GUID | VARCHAR2(32) |  |
| QUOTAGROUP_NUMBER | NUMBER |  |
| QUOTAGROUP_INCARNATION | NUMBER |  |
| USED_QUOTA_MB | NUMBER |  |
| USER_NUMBER | NUMBER |  |
| USER_INCARNATION | NUMBER |  |
| USERGROUP_NUMBER | NUMBER |  |
| USERGROUP_INCARNATION | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

In both Oracle ASM and Oracle Database instances, V$ASM_FILEGROUP displays one row for every File Group present in every Disk Group mounted by the Oracle ASM instance. File Groups are only displayed for Disk Groups where COMPATIBLE.ASM is set to 12.2 or higher. Note: There will not be an entry for the default File Group. Note: There will not be an entry for the default File Group. See Also: " V$ASM_FILEGROUP_PROPERTY " See Also: " V$ASM_FILEGROUP_PROPERTY "