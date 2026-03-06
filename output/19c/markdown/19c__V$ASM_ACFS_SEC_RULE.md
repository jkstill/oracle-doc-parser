---
id: 19c__V$ASM_ACFS_SEC_RULE
name: V$ASM_ACFS_SEC_RULE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ASM_ACFS_SEC_RULE.html
---

# V$ASM_ACFS_SEC_RULE

V$ASM_ACFS_SEC_RULE contains information about all Oracle ACFS security rules for each Oracle ACFS file system. This view also supports GV$ global views.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RULE_NAME | VARCHAR2(256) |  |
| RULE_TYPE | VARCHAR2(32) |  |
| RULE_VALUE | VARCHAR2(512) |  |
| RULE_VALUE2 | VARCHAR2(512) |  |
| RULE_OPTION | VARCHAR2(7) |  |
| FS_NAME | VARCHAR2(1024) |  |
| VOL_DEVICE | VARCHAR2(256) |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: Oracle Automatic Storage Management Administrator's Guide for more information about Oracle Automatic Storage Management Cluster File System (Oracle ACFS) Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle Automatic Storage Management Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM) information Note: To display information about Oracle ACFS file systems or volumes that are located on nodes in an Oracle Flex ASM configuration, you must connect to the Oracle ASM proxy instance instead of the local Oracle ASM instance. For information about Oracle Flex ASM, refer to Oracle Automatic Storage Management Administrator's Guide . See Also: Oracle Automatic Storage Management Administrator's Guide for more information about Oracle Automatic Storage Management Cluster File System (Oracle ACFS) Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle Automatic Storage Management Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM) information Note: To display information about Oracle ACFS file systems or volumes that are located on nodes in an Oracle Flex ASM configuration, you must connect to the Oracle ASM proxy instance instead of the local Oracle ASM instance. For information about Oracle Flex ASM, refer to Oracle Automatic Storage Management Administrator's Guide .