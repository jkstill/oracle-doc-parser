---
id: 19c__ALL_SQLJ_TYPES
name: ALL_SQLJ_TYPES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [all]
source_file: ALL_SQLJ_TYPES.html
---

# ALL_SQLJ_TYPES

ALL_SQLJ_TYPES describes the SQLJ object types accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the type |
| TYPE_NAME | VARCHAR2(128) | Name of the type |
| TYPE_OID | RAW(16) | Object identifier (OID) of the type |
| EXTERNAL_NAME | VARCHAR2(4000) | External class name of the type |
| USING | VARCHAR2(21) | Representation of the type: SQLData CustomDatum Serializable Serializable Internal ORAData |
| TYPECODE | VARCHAR2(128) | Typecode of the type |
| ATTRIBUTES | NUMBER | Number of attributes (if any) in the type |
| METHODS | NUMBER | Number of methods (if any) in the type |
| PREDEFINED | VARCHAR2(3) | Indicates whether the type is a predefined type ( YES ) or not ( NO ) |
| INCOMPLETE | VARCHAR2(3) | Indicates whether the type is an incomplete type ( YES ) or not ( NO ) |
| FINAL | VARCHAR2(3) | Indicates whether the type is a final type ( YES ) or not ( NO ) |
| INSTANTIABLE | VARCHAR2(3) | Indicates whether the type is an instantiable type ( YES ) or not ( NO ) |
| SUPERTYPE_OWNER | VARCHAR2(128) | Owner of the supertype (NULL if type is not a subtype) |
| SUPERTYPE_NAME | VARCHAR2(128) | Name of the supertype (NULL if type is not a subtype) |
| LOCAL_ATTRIBUTES | NUMBER | Number of local (not inherited) attributes (if any) in the subtype |
| LOCAL_METHODS | NUMBER | Number of local (not inherited) methods (if any) in the subtype |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_SQLJ_TYPES describes all SQLJ object types in the database. USER_SQLJ_TYPES describes the SQLJ object types owned by the current user. This view does not display the OWNER column. See Also: " DBA_SQLJ_TYPES " " USER_SQLJ_TYPES " See Also: " DBA_SQLJ_TYPES " " USER_SQLJ_TYPES "