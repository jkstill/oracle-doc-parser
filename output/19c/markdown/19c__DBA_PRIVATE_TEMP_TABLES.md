---
id: 19c__DBA_PRIVATE_TEMP_TABLES
name: DBA_PRIVATE_TEMP_TABLES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [dba]
source_file: DBA_PRIVATE_TEMP_TABLES.html
---

# DBA_PRIVATE_TEMP_TABLES

DBA_PRIVATE_TEMP_TABLES describes all of the private temporary tables in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SID | NUMBER | Session ID of the session that created the private temporary table |
| SERIAL# | NUMBER | Session serial number of the session that created the private temporary table |
| INST_ID | NUMBER | Instance ID of the session that created the private temporary table |
| OWNER | VARCHAR2(128) | Owner name of the private temporary table |
| TABLE_NAME | VARCHAR2(128) | Private temporary table name |
| TABLESPACE_NAME | VARCHAR2(128) | Private temporary table's tablespace name |
| DURATION | VARCHAR2(128) | Private temporary table's duration (for example, SESSION or TRANSACTION ) |
| NUM_ROWS | NUMBER | Number of rows in the private temporary table when analyzed |
| BLOCKS | NUMBER | Number of blocks used by private temporary table |
| AVG_ROW_LEN | NUMBER | Average row length |
| LAST_ANALYZED | DATE | Timestamp of last analyze |
| TXN_ID | RAW(8) | Transaction ID of the transaction duration private temporary table |
| SAVE_POINT_NUM | NUMBER | Save point number of the transaction duration private temporary table |

## Usage Notes

Related View USER_PRIVATE_TEMP_TABLES describes the private temporary tables in the current session. This view does not display the INST_ID column. See Also: " USER_PRIVATE_TEMP_TABLES " " PRIVATE_TEMP_TABLE_PREFIX " Oracle Database Administrator’s Guide for an introduction to private temporary tables See Also: " USER_PRIVATE_TEMP_TABLES " " PRIVATE_TEMP_TABLE_PREFIX " Oracle Database Administrator’s Guide for an introduction to private temporary tables