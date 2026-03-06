---
id: 19c__DBA_DBFS_HS_COMMANDS
name: DBA_DBFS_HS_COMMANDS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_DBFS_HS_COMMANDS.html
---

# DBA_DBFS_HS_COMMANDS

DBA_DBFS_HS_COMMANDS shows all the registered store commands for all Database File System (DBFS) hierarchical stores.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| STORENAME | VARCHAR2(256) | Name of store |
| STOREOWNER | VARCHAR2(64) | Owner of store |
| STORECOMMAND | VARCHAR2(512) | Store command |
| STOREFLAGS | NUMBER | Valid values are: 1 - Indicates that the command is sent to the device before put 2 - Indicates that the command is sent to the device before get |

## Usage Notes

Related View USER_DBFS_HS_COMMANDS shows all the registered store commands for all DBFS hierarchical stores owned by current user. This view does not display the STOREOWNER column. See Also: " USER_DBFS_HS_COMMANDS " See Also: " USER_DBFS_HS_COMMANDS "