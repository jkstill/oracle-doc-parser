---
id: 19c__ALL_CLUSTERING_DIMENSIONS
name: ALL_CLUSTERING_DIMENSIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_CLUSTERING_DIMENSIONS.html
---

# ALL_CLUSTERING_DIMENSIONS

ALL_CLUSTERING_DIMENSIONS describes dimension tables associated with tables with an attribute clustering clause that the user owns or has system privileges for.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the attribute clustering table |
| TABLE_NAME | VARCHAR2(128) | Name of the attribute clustering table |
| DIMENSION_OWNER | VARCHAR2(128) | Owner of the dimension table |
| DIMENSION_NAME | VARCHAR2(128) | Name of the dimension table |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_CLUSTERING_DIMENSIONS describes dimension tables associated with all tables with an attribute clustering clause in the database. USER_CLUSTERING_DIMENSIONS describes dimension tables associated with tables with an attribute clustering clause owned by the user. This view does not display the OWNER column. See Also: " DBA_CLUSTERING_DIMENSIONS " " USER_CLUSTERING_DIMENSIONS " The ALTER TABLE section in Oracle Database SQL Language Reference for information about using the CLUSTERING clause to create an attribute clustering table The CREATE TABLE section in Oracle Database SQL Language Reference for information about using the CLUSTERING clause to create an attribute clustering table Oracle Database Data Warehousing Guide for information about dimension tables Oracle Database Data Warehousing Guide for information about attribute clustering with zone maps See Also: " DBA_CLUSTERING_DIMENSIONS " " USER_CLUSTERING_DIMENSIONS " The ALTER TABLE section in Oracle Database SQL Language Reference for information about using the CLUSTERING clause to create an attribute clustering table The CREATE TABLE section in Oracle Database SQL Language Reference for information about using the CLUSTERING clause to create an attribute clustering table Oracle Database Data Warehousing Guide for information about dimension tables Oracle Database Data Warehousing Guide for information about attribute clustering with zone maps