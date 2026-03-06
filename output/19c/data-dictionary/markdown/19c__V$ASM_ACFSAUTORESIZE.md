---
id: 19c__V$ASM_ACFSAUTORESIZE
name: V$ASM_ACFSAUTORESIZE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ASM_ACFSAUTORESIZE.html
---

# V$ASM_ACFSAUTORESIZE

V$ASM_ACFSAUTORESIZE displays the auto-resize settings for each mounted Oracle ACFS file system.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FS_NAME | VARCHAR2(1024) |  |
| RESIZE_INCREMENT | NUMBER |  |
| RESIZE_MAXIMUM | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: This view is available starting with Oracle Database release 19c, version 19.1. See Also: Oracle Automatic Storage Management Administrator's Guide for more information about Oracle Automatic Storage Management Cluster File System (Oracle ACFS) Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle Automatic Storage Management Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM) information Note: To display information about Oracle ACFS file systems or volumes that are located on nodes in an Oracle Flex ASM configuration, you must connect to the Oracle ASM proxy instance instead of the local Oracle ASM instance. For information about Oracle Flex ASM, refer to Oracle Automatic Storage Management Administrator's Guide . Note: This view is available starting with Oracle Database release 19c, version 19.1. See Also: Oracle Automatic Storage Management Administrator's Guide for more information about Oracle Automatic Storage Management Cluster File System (Oracle ACFS) Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle Automatic Storage Management Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM) information Note: To display information about Oracle ACFS file systems or volumes that are located on nodes in an Oracle Flex ASM configuration, you must connect to the Oracle ASM proxy instance instead of the local Oracle ASM instance. For information about Oracle Flex ASM, refer to Oracle Automatic Storage Management Administrator's Guide .