---
id: 19c__ALL_SQLJ_TYPE_ATTRS
name: ALL_SQLJ_TYPE_ATTRS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [all]
source_file: ALL_SQLJ_TYPE_ATTRS.html
---

# ALL_SQLJ_TYPE_ATTRS

ALL_SQLJ_TYPE_ATTRS describes the attributes of the SQLJ object types accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the type |
| TYPE_NAME | VARCHAR2(128) | Name of the type |
| ATTR_NAME | VARCHAR2(128) | Name of the attribute |
| EXTERNAL_ATTR_NAME | VARCHAR2(4000) | External name of the attribute |
| ATTR_TYPE_MOD | VARCHAR2(7) | Type modifier of the attribute: REF POINTER |
| ATTR_TYPE_OWNER | VARCHAR2(128) | Owner of the type of the attribute |
| ATTR_TYPE_NAME | VARCHAR2(128) | Name of the type of the attribute |
| LENGTH | NUMBER | Length of the CHAR attribute, or maximum length of the VARCHAR or VARCHAR2 attribute. |
| PRECISION | NUMBER | Decimal precision of the NUMBER or DECIMAL attribute, or binary precision of the FLOAT attribute. |
| SCALE | NUMBER | Scale of the NUMBER or DECIMAL attribute |
| CHARACTER_SET _NAME | VARCHAR2(44) | Character set name of the attribute ( CHAR_CS or NCHAR_CS ) |
| ATTR_NO | NUMBER | Syntactical order number or position of the attribute as specified in the type specification or CREATE TYPE statement (not to be used as an ID number) |
| INHERITED | VARCHAR2(3) | Indicates whether the attribute is inherited from a supertype ( YES ) or not ( NO ) |

## Usage Notes

Related Views DBA_SQLJ_TYPE_ATTRS describes the attributes of all SQLJ object types in the database. USER_SQLJ_TYPE_ATTRS describes the attributes of the object types owned by the current user. This view does not display the OWNER column. See Also: " DBA_SQLJ_TYPE_ATTRS " " USER_SQLJ_TYPE_ATTRS " See Also: " DBA_SQLJ_TYPE_ATTRS " " USER_SQLJ_TYPE_ATTRS "