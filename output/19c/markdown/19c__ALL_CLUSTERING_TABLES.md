---
id: 19c__ALL_CLUSTERING_TABLES
name: ALL_CLUSTERING_TABLES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_CLUSTERING_TABLES.html
---

# ALL_CLUSTERING_TABLES

ALL_CLUSTERING_TABLES describes tables with an attribute clustering clause that are accessible to the user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the table |
| TABLE_NAME | VARCHAR2(128) | Name of the table |
| CLUSTERING_TYPE | VARCHAR2(11) | Clustering type: INTERLEAVED LINEAR |
| ON_LOAD | VARCHAR2(3) | Indicates whether Oracle will cluster data on load ( YES ) or not ( NO ) |
| ON_DATAMOVEMENT | VARCHAR2(3) | Indicates whether Oracle will cluster data on data movement, for example, partition move ( YES ), or not ( NO ) |
| VALID | VARCHAR2(3) | Indicates if clustering is valid ( YES ) or not ( NO ). For clustering with dimension tables, it is required that the joins of the fact table to the dimensions is via primary key or unique key on the dimension table. Therefore, dimension join keys must have a valid primary key or unique key constraint. If the primary key or unique key constraint is not valid, then clustering will not occur. If there are no joins in the CLUSTERING clause, then the value of this column is YES . |
| WITH_ZONEMAP | VARCHAR2(3) | Indicates if a zonemap was created with clustering ( YES ) or not ( NO ). |
| LAST_LOAD_CLST | TIMESTAMP(6) | Last time the clustering occurred on load |
| LAST_DATAMOVE_CLST | TIMESTAMP(6) | Last time the clustering occurred on data movement, for example, partition move |

## Usage Notes

Related Views DBA_CLUSTERING_TABLES describes all the tables with an attribute clustering clause. USER_CLUSTERING_TABLES describes the tables with an attribute clustering clause owned by the user. See Also: " DBA_CLUSTERING_TABLES " " USER_CLUSTERING_TABLES " The ALTER TABLE section in Oracle Database SQL Language Reference for information about using the CLUSTERING clause to create an attribute clustering table The CREATE TABLE section in Oracle Database SQL Language Reference for information about using the CLUSTERING clause to create an attribute clustering table Oracle Database Data Warehousing Guide for information about dimension tables Oracle Database Data Warehousing Guide for information about attribute clustering with zone maps See Also: " DBA_CLUSTERING_TABLES " " USER_CLUSTERING_TABLES " The ALTER TABLE section in Oracle Database SQL Language Reference for information about using the CLUSTERING clause to create an attribute clustering table The CREATE TABLE section in Oracle Database SQL Language Reference for information about using the CLUSTERING clause to create an attribute clustering table Oracle Database Data Warehousing Guide for information about dimension tables Oracle Database Data Warehousing Guide for information about attribute clustering with zone maps