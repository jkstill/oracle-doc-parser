---
id: 19c__V$ASM_DISKGROUP
name: V$ASM_DISKGROUP
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ASM_DISKGROUP.html
---

# V$ASM_DISKGROUP

V$ASM_DISKGROUP displays one row for every Oracle Automatic Storage Management (Oracle ASM) disk group discovered by the Oracle ASM instance on the node.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| GROUP_NUMBER | NUMBER |  |
| NAME | VARCHAR2(30) |  |
| SECTOR_SIZE | NUMBER |  |
| LOGICAL_SECTOR_SIZE | NUMBER |  |
| BLOCK_SIZE | NUMBER |  |
| ALLOCATION_UNIT_SIZE | NUMBER |  |
| STATE | VARCHAR2(11) |  |
| TYPE | VARCHAR2(6) |  |
| TOTAL_MB | NUMBER |  |
| FREE_MB | NUMBER |  |
| HOT_USED_MB | NUMBER |  |
| COLD_USED_MB | NUMBER |  |
| REQUIRED_MIRROR_FREE_MB | NUMBER |  |
| USABLE_FILE_MB | NUMBER |  |
| OFFLINE_DISKS | NUMBER |  |
| COMPATIBILITY | VARCHAR2(60) |  |
| DATABASE_COMPATIBILITY | VARCHAR2(60) |  |
| VOTING_FILES | VARCHAR2(1) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Note: The GROUP_NUMBER , TOTAL_MB , and FREE_MB columns are only meaningful if the disk group is mounted by the instance. Otherwise, their values will be 0 . See Also: Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information Note: The GROUP_NUMBER , TOTAL_MB , and FREE_MB columns are only meaningful if the disk group is mounted by the instance. Otherwise, their values will be 0 . See Also: Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information