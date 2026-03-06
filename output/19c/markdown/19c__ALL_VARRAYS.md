---
id: 19c__ALL_VARRAYS
name: ALL_VARRAYS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_VARRAYS.html
---

# ALL_VARRAYS

ALL_VARRAYS describes the varrays accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the table containing the varray |
| PARENT_TABLE_NAME | VARCHAR2(128) | Name of the containing table |
| PARENT_TABLE_COLUMN | VARCHAR2(4000) | Name of the varray column or attribute |
| TYPE_OWNER | VARCHAR2(128) | Owner of the varray type |
| TYPE_NAME | VARCHAR2(128) | Name of the varray type |
| LOB_NAME | VARCHAR2(128) | Name of the LOB if the varray is stored in a LOB |
| STORAGE_SPEC | VARCHAR2(30) | Indicates whether the storage was defaulted ( DEFAULT ) or user-specified ( USER_SPECIFIED ) |
| RETURN_TYPE | VARCHAR2(20) | Return type of the column: LOCATOR VALUE |
| ELEMENT_SUBSTITUTABLE | VARCHAR2(25) | Indicates whether the varray element is substitutable ( Y ) or not ( N ) |

## Usage Notes

Related Views DBA_VARRAYS describes all varrays in the database. USER_VARRAYS describes the varrays owned by the current user. This view does not display the OWNER column. See Also: " DBA_VARRAYS " " USER_VARRAYS " See Also: " DBA_VARRAYS " " USER_VARRAYS "