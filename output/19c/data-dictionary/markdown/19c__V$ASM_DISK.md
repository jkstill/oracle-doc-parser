---
id: 19c__V$ASM_DISK
name: V$ASM_DISK
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ASM_DISK.html
---

# V$ASM_DISK

V$ASM_DISK displays one row for every disk discovered by the Oracle Automatic Storage Management (Oracle ASM) instance, including disks that are not part of any disk group.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| GROUP_NUMBER | NUMBER |  |
| DISK_NUMBER | NUMBER |  |
| COMPOUND_INDEX | NUMBER |  |
| INCARNATION | NUMBER |  |
| MOUNT_STATUS | VARCHAR2(7) |  |
| HEADER_STATUS | VARCHAR2(12) |  |
| MODE_STATUS | VARCHAR2(7) |  |
| STATE | VARCHAR2(8) |  |
| REDUNDANCY | VARCHAR2(7) |  |
| LIBRARY | VARCHAR2(64) |  |
| OS_MB | NUMBER |  |
| TOTAL_MB | NUMBER |  |
| FREE_MB | NUMBER |  |
| HOT_USED_MB | NUMBER |  |
| COLD_USED_MB | NUMBER |  |
| NAME | VARCHAR2(30) |  |
| FAILGROUP | VARCHAR2(30) |  |
| LABEL | VARCHAR2(31) |  |
| PATH | VARCHAR2(256) |  |
| UDID | VARCHAR2(64) |  |
| PRODUCT | VARCHAR2(32) |  |
| CREATE_DATE | DATE |  |
| MOUNT_DATE | DATE |  |
| REPAIR_TIMER | NUMBER |  |
| READS | NUMBER |  |
| WRITES | NUMBER |  |
| READ_ERRS | NUMBER |  |
| WRITE_ERRS | NUMBER |  |
| READ_TIMEOUT | NUMBER |  |
| WRITE_TIMEOUT | NUMBER |  |
| READ_TIME | NUMBER |  |
| WRITE_TIME | NUMBER |  |
| BYTES_READ | NUMBER |  |
| BYTES_WRITTEN | NUMBER |  |
| PREFERRED_READ | VARCHAR2(1) |  |
| HASH_VALUE | NUMBER |  |
| HOT_READS | NUMBER |  |
| HOT_WRITES | NUMBER |  |
| HOT_BYTES_READ | NUMBER |  |
| HOT_BYTES_WRITTEN | NUMBER |  |
| COLD_READS | NUMBER |  |
| COLD_WRITES | NUMBER |  |
| COLD_BYTES_READ | NUMBER |  |
| COLD_BYTES_WRITTEN | NUMBER |  |
| VOTING_FILE | VARCHAR2(1) |  |
| SECTOR_SIZE | NUMBER |  |
| LOGICAL_SECTOR_SIZE | NUMBER |  |
| FAILGROUP_TYPE | VARCHAR2(7) |  |
| CON_ID | NUMBER |  |
| THIN_PROVISION_CAPABLE | VARCHAR2(1) |  |
| DATA_INTEGRITY_CAPABLE | VARCHAR2(1) |  |
| SITE_NAME | VARCHAR2(30) |  |
| SITE_GUID | VARCHAR2(33) |  |
| FAILGROUP_LABEL | VARCHAR2(30) |  |
| SITE_LABEL | VARCHAR2(30) |  |
| SITE_STATUS | VARCHAR2(11) |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: The GROUP_NUMBER and DISK_NUMBER columns will only be valid if the disk is part of a disk group which is currently mounted by the instance. Otherwise, GROUP_NUMBER will be 0 , and DISK_NUMBER will be a unique value with respect to the other disks that also have a group number of 0 . See Also: Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information Note: The GROUP_NUMBER and DISK_NUMBER columns will only be valid if the disk is part of a disk group which is currently mounted by the instance. Otherwise, GROUP_NUMBER will be 0 , and DISK_NUMBER will be a unique value with respect to the other disks that also have a group number of 0 . See Also: Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information