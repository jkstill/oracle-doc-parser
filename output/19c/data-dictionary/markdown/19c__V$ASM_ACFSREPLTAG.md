---
id: 19c__V$ASM_ACFSREPLTAG
name: V$ASM_ACFSREPLTAG
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ASM_ACFSREPLTAG.html
---

# V$ASM_ACFSREPLTAG

V$ASM_ACFSREPLTAG displays replicated tag information for Oracle ACFS file systems that are initialized for replication.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FSNAME | VARCHAR2(1024) |  |
| VOLDEV | VARCHAR2(256) |  |
| TAG | VARCHAR2(32) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: This view only contains records for Oracle ASM releases prior to Oracle Database 12 c Release 2 (12.2.0.1). To display Oracle ACFS replication information for Oracle Database 12 c Release 2 (12.2.0.1) or higher, use the acfsutil repl info command. See Also: Oracle Automatic Storage Management Administrator's Guide for more information about Oracle Automatic Storage Management Cluster File System (Oracle ACFS) Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle Automatic Storage Management Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM) information Note: To display information about Oracle ACFS file systems or volumes that are located on nodes in an Oracle Flex ASM configuration, you must connect to the Oracle ASM proxy instance instead of the local Oracle ASM instance. For information about Oracle Flex ASM, refer to Oracle Automatic Storage Management Administrator's Guide . Note: This view only contains records for Oracle ASM releases prior to Oracle Database 12 c Release 2 (12.2.0.1). To display Oracle ACFS replication information for Oracle Database 12 c Release 2 (12.2.0.1) or higher, use the acfsutil repl info command. See Also: Oracle Automatic Storage Management Administrator's Guide for more information about Oracle Automatic Storage Management Cluster File System (Oracle ACFS) Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle Automatic Storage Management Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM) information Note: To display information about Oracle ACFS file systems or volumes that are located on nodes in an Oracle Flex ASM configuration, you must connect to the Oracle ASM proxy instance instead of the local Oracle ASM instance. For information about Oracle Flex ASM, refer to Oracle Automatic Storage Management Administrator's Guide .