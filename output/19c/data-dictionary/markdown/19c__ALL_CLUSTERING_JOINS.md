---
id: 19c__ALL_CLUSTERING_JOINS
name: ALL_CLUSTERING_JOINS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_CLUSTERING_JOINS.html
---

# ALL_CLUSTERING_JOINS

ALL_CLUSTERING_JOINS describes joins to the dimension tables associated with tables with an attribute clustering clause the user owns or has system privileges for.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the attribute clustering table |
| TABLE_NAME | VARCHAR2(128) | Name of the attribute clustering table |
| TAB1_OWNER | VARCHAR2(128) | Table 1 owner of the join |
| TAB1_NAME | VARCHAR2(128) | Table 1 name of the join |
| TAB1_COLUMN | VARCHAR2(128) | Table 1 column name of the join |
| TAB2_OWNER | VARCHAR2(128) | Table 2 owner of the join |
| TAB2_NAME | VARCHAR2(128) | Table 2 name of the join |
| TAB2_COLUMN | VARCHAR2(128) | Table 2 column name of the join |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_CLUSTERING_JOINS describes joins to the dimension tables associated with all tables with an attribute clustering clause in the database. USER_CLUSTERING_JOINS describes joins to the dimension tables associated with tables with an attribute clustering clause owned by the user. This view does not display the OWNER column. See Also: " DBA_CLUSTERING_JOINS " " USER_CLUSTERING_JOINS " The ALTER TABLE section in Oracle Database SQL Language Reference for information about using the CLUSTERING clause to create an attribute clustering table The CREATE TABLE section in Oracle Database SQL Language Reference for information about using the CLUSTERING clause to create an attribute clustering table Oracle Database Data Warehousing Guide for information about dimension tables Oracle Database Data Warehousing Guide for information about attribute clustering with zone maps See Also: " DBA_CLUSTERING_JOINS " " USER_CLUSTERING_JOINS " The ALTER TABLE section in Oracle Database SQL Language Reference for information about using the CLUSTERING clause to create an attribute clustering table The CREATE TABLE section in Oracle Database SQL Language Reference for information about using the CLUSTERING clause to create an attribute clustering table Oracle Database Data Warehousing Guide for information about dimension tables Oracle Database Data Warehousing Guide for information about attribute clustering with zone maps