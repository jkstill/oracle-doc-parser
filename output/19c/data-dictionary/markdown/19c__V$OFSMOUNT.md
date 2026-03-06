---
id: 19c__V$OFSMOUNT
name: V$OFSMOUNT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-OFSMOUNT.html
---

# V$OFSMOUNT

V$OFSMOUNT provides information about the file systems that are mounted by Oracle File System.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OFS_MNTPATH | VARCHAR2(1024) |  |
| OFS_FSPATH | VARCHAR2(1024) |  |
| OFS_MNTOPTS | VARCHAR2(1024) |  |
| OFS_MNTFLAGS | VARCHAR2(7) |  |
| CON_ID | NUMBER |  |
| OFS_NODENM | VARCHAR2(255) |  |
| OFS_FSID | NUMBER |  |
| OFS_FSTYPE | VARCHAR2(255) |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: This database view is supported only on the Linux operating system. See Also: " V$OFS_STATS " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_FS.MOUNT_ORACLE_FS procedure Note: This database view is supported only on the Linux operating system. See Also: " V$OFS_STATS " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_FS.MOUNT_ORACLE_FS procedure