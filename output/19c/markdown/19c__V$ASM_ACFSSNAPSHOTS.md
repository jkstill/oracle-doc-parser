---
id: 19c__V$ASM_ACFSSNAPSHOTS
name: V$ASM_ACFSSNAPSHOTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ASM_ACFSSNAPSHOTS.html
---

# V$ASM_ACFSSNAPSHOTS

V$ASM_ACFSSNAPSHOTS displays snapshot information for every mounted Oracle ACFS.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FS_NAME | VARCHAR2(1024) |  |
| VOL_DEVICE | VARCHAR2(256) |  |
| SNAP_NAME | VARCHAR2(1024) |  |
| CREATE_TIME | DATE |  |
| TYPE | VARCHAR2(2) |  |
| PARENT | VARCHAR2(1024) |  |
| LINK Foot 1 | VARCHAR2(1024) |  |
| ADDITIONAL_STORAGE Foot 1 | NUMBER |  |
| QUOTA Foot 1 | NUMBER |  |
| REPL Foot 1 | VARCHAR2(5) |  |
| STATE Foot 1 | VARCHAR2(14) |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: Oracle Automatic Storage Management Administrator's Guide for more information about Oracle Automatic Storage Management Cluster File System (Oracle ACFS) Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle Automatic Storage Management Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM) information Note: To display information about Oracle ACFS file systems or volumes that are located on nodes in an Oracle Flex ASM configuration, you must connect to the Oracle ASM proxy instance instead of the local Oracle ASM instance. For information about Oracle Flex ASM, refer to Oracle Automatic Storage Management Administrator's Guide . See Also: Oracle Automatic Storage Management Administrator's Guide for more information about Oracle Automatic Storage Management Cluster File System (Oracle ACFS) Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle Automatic Storage Management Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM) information Note: To display information about Oracle ACFS file systems or volumes that are located on nodes in an Oracle Flex ASM configuration, you must connect to the Oracle ASM proxy instance instead of the local Oracle ASM instance. For information about Oracle Flex ASM, refer to Oracle Automatic Storage Management Administrator's Guide .