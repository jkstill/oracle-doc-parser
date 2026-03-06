---
id: 19c__ALL_CLUSTERING_KEYS
name: ALL_CLUSTERING_KEYS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_CLUSTERING_KEYS.html
---

# ALL_CLUSTERING_KEYS

ALL_CLUSTERING_KEYS describes clustering keys for tables with an attribute clustering clause accessible to the user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the table on which the clustering clause is defined |
| TABLE_NAME | VARCHAR2(128) | Name of the table on which the clustering clause is defined |
| DETAIL_OWNER | VARCHAR2(128) | Owner of the detailed table contributing to the clustering keys |
| DETAIL_NAME | VARCHAR2(128) | Name of the detailed table contributing to the clustering keys |
| DETAIL_COLUMN | VARCHAR2(128) | Name of the detail column |
| POSITION | NUMBER | Position of the column in the clustering clause |
| GROUPID | NUMBER | Group ID of the column in the clustering clause |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_CLUSTERING_KEYS describes clustering keys for all tables with an attribute clustering clause. USER_CLUSTERING_KEYS describes clustering keys for tables with an attribute clustering clause owned by the user. See Also: " DBA_CLUSTERING_KEYS " " USER_CLUSTERING_KEYS " The ALTER TABLE section in Oracle Database SQL Language Reference for information about using the CLUSTERING clause to create an attribute clustering table The CREATE TABLE section in Oracle Database SQL Language Reference for information about using the CLUSTERING clause to create an attribute clustering table Oracle Database Data Warehousing Guide for information about dimension tables Oracle Database Data Warehousing Guide for information about attribute clustering with zone maps See Also: " DBA_CLUSTERING_KEYS " " USER_CLUSTERING_KEYS " The ALTER TABLE section in Oracle Database SQL Language Reference for information about using the CLUSTERING clause to create an attribute clustering table The CREATE TABLE section in Oracle Database SQL Language Reference for information about using the CLUSTERING clause to create an attribute clustering table Oracle Database Data Warehousing Guide for information about dimension tables Oracle Database Data Warehousing Guide for information about attribute clustering with zone maps