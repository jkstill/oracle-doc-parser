---
id: 19c__DBA_REPAIR_TABLE
name: DBA_REPAIR_TABLE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [dba]
source_file: DBA_REPAIR_TABLE.html
---

# DBA_REPAIR_TABLE

DBA_REPAIR_TABLE describes any corruptions found by the DBMS_REPAIR . CHECK_OBJECT procedure.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OBJECT_ID | NUMBER | Dictionary object number of the object with the corruption |
| TABLESPACE_ID | NUMBER | Tablespace number of the corrupt object |
| RELATIVE_FILE_ID | NUMBER) | Relative file number of the corrupt object |
| BLOCK_ID | NUMBER | Block number of the corruption |
| CORRUPT_TYPE | NUMBER | Type of corruption encountered |
| SCHEMA_NAME | VARCHAR2(128) | Schema of the corrupt object |
| OBJECT_NAME | VARCHAR2(128) | Name of the corrupt object |
| BASEOBJECT_NAME | VARCHAR2(128) | If the object is an index, the name of its base table |
| PARTITION_NAME | VARCHAR2(128) | Partition or subpartition name, if applicable |
| CORRUPT_DESCRIPTION | VARCHAR2(2000) | Description of corruption |
| REPAIR_DESCRIPTION | VARCHAR2(200) | Description of repair action |
| MARKED_CORRUPT | VARCHAR2(10) | Whether the block is marked corrupt ( TRUE | FALSE ) |
| CHECK_TIMESTAMP | DATE | Date and time when this row was inserted into the repair table |
| FIX_TIMESTAMP | DATE | Date and time when the block was modified by the FIX_CORRUPT_BLOCKS procedure, if applicable |
| REFORMAT_TIMESTAMP | DATE | Reserved for future use |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This information is used by the DBMS_REPAIR . FIX_CORRUPT_BLOCKS procedure on execution. To create this view, first run the DBMS_REPAIR . ADMIN_TABLES procedure. To populate the resulting repair table for an object, run the DBMS_REPAIR . CHECK_OBJECT procedure on the object. Note: The table created by the DBMS_REPAIR.ADMIN_TABLES procedure is called REPAIR TABLE by default. If you specify a different name, this view will have the name you specify, preceded by " DBA_REPAIR_ ". Note: The table created by the DBMS_REPAIR.ADMIN_TABLES procedure is called REPAIR TABLE by default. If you specify a different name, this view will have the name you specify, preceded by " DBA_REPAIR_ ". See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_REPAIR package See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_REPAIR package