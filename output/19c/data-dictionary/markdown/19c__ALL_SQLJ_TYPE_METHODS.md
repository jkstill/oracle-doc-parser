---
id: 19c__ALL_SQLJ_TYPE_METHODS
name: ALL_SQLJ_TYPE_METHODS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [all]
source_file: ALL_SQLJ_TYPE_METHODS.html
---

# ALL_SQLJ_TYPE_METHODS

ALL_SQLJ_TYPE_METHODS describes the methods of the SQLJ object types accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the type |
| TYPE_NAME | VARCHAR2(128) | Name of the type |
| METHOD_NAME | VARCHAR2(128) | Name of the method |
| EXTERNAL_VAR_NAME | VARCHAR2(4000) | Name of the external variable |
| METHOD_NO | NUMBER | Method number that distinguishes overloaded methods (not to be used as an ID number) |
| METHOD_TYPE | VARCHAR2(6) | Type of the method: MAP ORDER PUBLIC |
| PARAMETERS | NUMBER | Number of parameters to the method |
| RESULTS | NUMBER | Number of results returned by the method |
| FINAL | VARCHAR2(3) | Indicates whether the method is final ( YES ) or not ( NO ) |
| INSTANTIABLE | VARCHAR2(3) | Indicates whether the method is instantiable ( YES ) or not ( NO ) |
| OVERRIDING | VARCHAR2(3) | Indicates whether the method is overriding a supertype method ( YES ) or not ( NO ) |
| INHERITED | VARCHAR2(3) | Indicates whether the method is inherited from a supertype ( YES ) or not ( NO ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_SQLJ_TYPE_METHODS describes the methods of all SQLJ object types in the database. USER_SQLJ_TYPE_METHODS describes the methods of the SQLJ object types owned by the current user. This view does not display the OWNER column. See Also: " DBA_SQLJ_TYPE_METHODS " " USER_SQLJ_TYPE_METHODS " See Also: " DBA_SQLJ_TYPE_METHODS " " USER_SQLJ_TYPE_METHODS "