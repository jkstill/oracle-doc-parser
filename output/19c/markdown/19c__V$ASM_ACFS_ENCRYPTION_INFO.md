---
id: 19c__V$ASM_ACFS_ENCRYPTION_INFO
name: V$ASM_ACFS_ENCRYPTION_INFO
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ASM_ACFS_ENCRYPTION_INFO.html
---

# V$ASM_ACFS_ENCRYPTION_INFO

V$ASM_ACFS_ENCRYPTION_INFO displays encryption information for every mounted Oracle ACFS.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FS_NAME | VARCHAR2(1024) |  |
| VOL_DEVICE | VARCHAR2(256) |  |
| SET_STATUS | VARCHAR2(7) |  |
| ENABLED_STATUS | VARCHAR2(8) |  |
| ALGORITHM | VARCHAR2(7) |  |
| KEY_LENGTH | VARCHAR2(7) |  |
| LAST_REKEY_TIME | DATE |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: Oracle Automatic Storage Management Administrator's Guide for more information about Oracle Automatic Storage Management Cluster File System (Oracle ACFS) Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle Automatic Storage Management Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM) information Note: To display information about Oracle ACFS file systems or volumes that are located on nodes in an Oracle Flex ASM configuration, you must connect to the Oracle ASM proxy instance instead of the local Oracle ASM instance. For information about Oracle Flex ASM, refer to Oracle Automatic Storage Management Administrator's Guide . See Also: Oracle Automatic Storage Management Administrator's Guide for more information about Oracle Automatic Storage Management Cluster File System (Oracle ACFS) Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle Automatic Storage Management Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM) information Note: To display information about Oracle ACFS file systems or volumes that are located on nodes in an Oracle Flex ASM configuration, you must connect to the Oracle ASM proxy instance instead of the local Oracle ASM instance. For information about Oracle Flex ASM, refer to Oracle Automatic Storage Management Administrator's Guide .