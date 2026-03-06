---
id: 19c__DBA_SODA_COLLECTIONS
name: DBA_SODA_COLLECTIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_SODA_COLLECTIONS.html
---

# DBA_SODA_COLLECTIONS

DBA_SODA_COLLECTIONS describes all Simple Oracle Document Access (SODA) collections in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| URI_NAME | NVARCHAR2(255) | Collection name |
| OWNER | VARCHAR2(128) | Owner of the collection |
| OBJECT_TYPE | VARCHAR2(10) | Indicates whether the collection is table-based ( TABLE ) or view-based ( VIEW ) |
| OBJECT_SCHEMA | VARCHAR2(128) | Name of the schema that includes the table or view on which the collection is based |
| OBJECT_NAME | VARCHAR2(128) | Name of the table or view on which the collection is based |
| CREATED_ON | TIMESTAMP(6) | Collection creation time |
| CREATE_MODE | VARCHAR2(10) | Creation mode. Possible values: DDL : A new table was created at collection creation time MAP : The collection was created by mapping a preexisting table or view Note: For view-based collections, the value of this column is always MAP . New views are not created for view-based collections. A view-based collection is always created by mapping a preexisting view. |
| JSON_DESCRIPTOR | VARCHAR2(4000) | Collection metadata, expressed in JavaScript Object Notation (JSON) |

## Usage Notes

Related View USER_SODA_COLLECTIONS describes the SODA collections owned by the current user. This view does not display the OWNER column. Note: The DBA_SODA_COLLECTIONS view is available only in Oracle Autonomous Database. However, the USER_SODA_COLLECTIONS view is available in on-premises Oracle databases and Oracle Autonomous Database. See Also: " USER_SODA_COLLECTIONS " Note: The DBA_SODA_COLLECTIONS view is available only in Oracle Autonomous Database. However, the USER_SODA_COLLECTIONS view is available in on-premises Oracle databases and Oracle Autonomous Database. See Also: " USER_SODA_COLLECTIONS "