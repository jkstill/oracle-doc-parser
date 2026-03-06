---
id: 19c__ALL_FILE_GROUP_TABLES
name: ALL_FILE_GROUP_TABLES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_FILE_GROUP_TABLES.html
---

# ALL_FILE_GROUP_TABLES

ALL_FILE_GROUP_TABLES shows information about the tables accessible to the current user that can be imported using the file set.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FILE_GROUP_OWNER | VARCHAR2(128) | Owner of the file group |
| FILE_GROUP_NAME | VARCHAR2(128) | Name of the file group |
| VERSION_NAME | VARCHAR2(128) | Version of the file group that contains the table |
| VERSION | NUMBER | Internal version number |
| OWNER | VARCHAR2(128) | Schema to which the table belongs |
| TABLE_NAME | VARCHAR2(128) | Name of the table |
| TABLESPACE_NAME | VARCHAR2(30) | Name of the tablespace to which the table belongs |
| SCN | NUMBER | SCN at which the table was exported (available only for Streams-prepared tables) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_FILE_GROUP_TABLES shows information about all the tables in the database that can be imported using the file set. USER_FILE_GROUP_TABLES shows information about tables owned by the current user that can be imported using the file set. This view does not display the FILE_GROUP_OWNER column. See Also: " DBA_FILE_GROUP_TABLES " " USER_FILE_GROUP_TABLES " See Also: " DBA_FILE_GROUP_TABLES " " USER_FILE_GROUP_TABLES "