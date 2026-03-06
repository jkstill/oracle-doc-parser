---
id: 19c__V$ASM_ACFSVOLUMES
name: V$ASM_ACFSVOLUMES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ASM_ACFSVOLUMES.html
---

# V$ASM_ACFSVOLUMES

V$ASM_ACFSVOLUMES displays information about mounted Oracle ACFS volumes, correlated with V$ASM_FILESYSTEM .

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FS_NAME | VARCHAR2(1024) |  |
| VOL_DEVICE | VARCHAR2(256) |  |
| VOL_LABEL | VARCHAR2(64) |  |
| PRIMARY_VOL | VARCHAR2(5) |  |
| TOTAL_MB | NUMBER |  |
| FREE_MB | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: " V$ASM_FILESYSTEM " Oracle Automatic Storage Management Administrator's Guide for more information about Oracle Automatic Storage Management Cluster File System (Oracle ACFS) Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle Automatic Storage Management Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM) information Note: To display information about Oracle ACFS file systems or volumes that are located on nodes in an Oracle Flex ASM configuration, you must connect to the Oracle ASM proxy instance instead of the local Oracle ASM instance. For information about Oracle Flex ASM, refer to Oracle Automatic Storage Management Administrator's Guide . See Also: " V$ASM_FILESYSTEM " Oracle Automatic Storage Management Administrator's Guide for more information about Oracle Automatic Storage Management Cluster File System (Oracle ACFS) Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle Automatic Storage Management Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM) information Note: To display information about Oracle ACFS file systems or volumes that are located on nodes in an Oracle Flex ASM configuration, you must connect to the Oracle ASM proxy instance instead of the local Oracle ASM instance. For information about Oracle Flex ASM, refer to Oracle Automatic Storage Management Administrator's Guide .