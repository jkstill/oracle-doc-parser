---
id: 19c__V$ASM_ACFS_SEC_RULESET_RULE
name: V$ASM_ACFS_SEC_RULESET_RULE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ASM_ACFS_SEC_RULESET_RULE.html
---

# V$ASM_ACFS_SEC_RULESET_RULE

V$ASM_ACFS_SEC_RULESET_RULE contains an entry for every rule in the Oracle ACFS security rule set for each Oracle ACFS file system. This view also supports GV$ global views.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RULESET_NAME | VARCHAR2(256) |  |
| RULE_NAME | VARCHAR2(256) |  |
| FS_NAME | VARCHAR2(1024) |  |
| VOL_DEVICE | VARCHAR2(256) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: Oracle Automatic Storage Management Administrator's Guide for more information about Oracle Automatic Storage Management Cluster File System (Oracle ACFS) Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle Automatic Storage Management Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM) information Note: To display information about Oracle ACFS file systems or volumes that are located on nodes in an Oracle Flex ASM configuration, you must connect to the Oracle ASM proxy instance instead of the local Oracle ASM instance. For information about Oracle Flex ASM, refer to Oracle Automatic Storage Management Administrator's Guide . See Also: Oracle Automatic Storage Management Administrator's Guide for more information about Oracle Automatic Storage Management Cluster File System (Oracle ACFS) Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle Automatic Storage Management Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM) information Note: To display information about Oracle ACFS file systems or volumes that are located on nodes in an Oracle Flex ASM configuration, you must connect to the Oracle ASM proxy instance instead of the local Oracle ASM instance. For information about Oracle Flex ASM, refer to Oracle Automatic Storage Management Administrator's Guide .