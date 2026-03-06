---
id: 19c__V$ASM_ACFS_SEC_CMDRULE
name: V$ASM_ACFS_SEC_CMDRULE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ASM_ACFS_SEC_CMDRULE.html
---

# V$ASM_ACFS_SEC_CMDRULE

V$ASM_ACFS_SEC_CMDRULE contains one row for every Oracle ACFS security command rule for each Oracle ACFS file system. This view also supports GV$ global views.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CMD_RULE_NAME | VARCHAR2(32) |  |
| FS_NAME | VARCHAR2(1024) |  |
| VOL_DEVICE | VARCHAR2(256) |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: Oracle Automatic Storage Management Administrator's Guide for more information about Oracle Automatic Storage Management Cluster File System (Oracle ACFS) Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle Automatic Storage Management Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM) information Note: To display information about Oracle ACFS file systems or volumes that are located on nodes in an Oracle Flex ASM configuration, you must connect to the Oracle ASM proxy instance instead of the local Oracle ASM instance. For information about Oracle Flex ASM, refer to Oracle Automatic Storage Management Administrator's Guide . See Also: Oracle Automatic Storage Management Administrator's Guide for more information about Oracle Automatic Storage Management Cluster File System (Oracle ACFS) Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle Automatic Storage Management Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM) information Note: To display information about Oracle ACFS file systems or volumes that are located on nodes in an Oracle Flex ASM configuration, you must connect to the Oracle ASM proxy instance instead of the local Oracle ASM instance. For information about Oracle Flex ASM, refer to Oracle Automatic Storage Management Administrator's Guide .