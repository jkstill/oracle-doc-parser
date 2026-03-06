---
id: 19c__ALL_TYPES
name: ALL_TYPES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_TYPES.html
---

# ALL_TYPES

ALL_TYPES describes the object types accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the type |
| TYPE_NAME | VARCHAR2(128) | Name of the type |
| TYPE_OID | RAW(16) | Object identifier (OID) of the type |
| TYPECODE | VARCHAR2(128) | Typecode of the type |
| ATTRIBUTES | NUMBER | Number of attributes (if any) in the type |
| METHODS | NUMBER | Number of methods (if any) in the type |
| PREDEFINED | VARCHAR2(3) | Indicates whether the type is a predefined type ( YES ) or not ( NO ) |
| INCOMPLETE | VARCHAR2(3) | Indicates whether the type is an incomplete type ( YES ) or not ( NO ) |
| FINAL | VARCHAR2(3) | Indicates whether the type is a final type ( YES ) or not ( NO ) |
| INSTANTIABLE | VARCHAR2(3) | Indicates whether the type is an instantiable type ( YES ) or not ( NO ) |
| PERSISTABLE | VARCHAR2(3) | Indicates whether the type is a persistable type ( YES ) or not ( NO ) |
| SUPERTYPE_OWNER | VARCHAR2(128) | Owner of the supertype (NULL if type is not a subtype) |
| SUPERTYPE_NAME | VARCHAR2(128) | Name of the supertype (NULL if type is not a subtype) |
| LOCAL_ATTRIBUTES | NUMBER | Number of local (not inherited) attributes (if any) in the subtype |
| LOCAL_METHODS | NUMBER | Number of local (not inherited) methods (if any) in the subtype |
| TYPEID | RAW(16) | Type ID value of the type |

## Usage Notes

Related Views DBA_TYPES describes all object types in the database. USER_TYPES describes the object types owned by the current user. This view does not display the OWNER column. See Also: " DBA_TYPES " " USER_TYPES " See Also: " DBA_TYPES " " USER_TYPES "