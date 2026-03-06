---
id: 19c__ALL_CUBE_ATTRIBUTES
name: ALL_CUBE_ATTRIBUTES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_CUBE_ATTRIBUTES.html
---

# ALL_CUBE_ATTRIBUTES

ALL_CUBE_ATTRIBUTES describes the attributes for the OLAP cube dimensions accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the cube dimension |
| DIMENSION_NAME | VARCHAR2(128) | Name of a cube dimension (such as TIME ) |
| ATTRIBUTE_NAME | VARCHAR2(128) | Name of an attribute of the dimension (such as LONG_DESCRIPTION or END_DATE ) |
| ATTRIBUTE_ID | NUMBER | ID of the attribute of the dimension |
| TARGET_DIMENSION_NAME | VARCHAR2(128) | Name of the target dimension of the attribute |
| ATTRIBUTE_ROLE | VARCHAR2(17) | Special role this attribute plays; NULL if none: SHORT_DESCRIPTION LONG_DESCRIPTION DESCRIPTION TIME_SPAN END_DATE |
| DESCRIPTION | NVARCHAR2(300) | Description of the attribute in the session language |
| ATTRIBUTE_GROUP_NAME | VARCHAR2(200) | Name of the attribute group |
| DATA_TYPE | VARCHAR2(106) | Data type of the attribute, (such as VARCHAR2 or FLOAT ) |
| DATA_LENGTH | NUMBER | Length of a text data type |
| DATA_PRECISION | NUMBER | Precision of a numeric data type |
| DATA_SCALE | NUMBER | Scale of a numeric data type |
| CREATE_INDEX | VARCHAR2(3) | Create index flag of the OLAP attribute. Possible values: YES : The attribute is represented in the AW as a relation. Setting CreateIndex="True" in the metadata guarantees that it will be represented in the AW as a relation. NO : The attribute is not represented in the AW as a relation. Setting CreateIndex="False" in the metadata does not guarantee that it will be represented in the AW a a variable; the system will make that determination. |
| IS_MULTI_LINGUAL | VARCHAR2(3) | Shows the setting for the IsMultiLingual flag of the OLAP Atttribute. Possible values: YES : The attribute is set as multilingual. Setting IsMultiLingual to True in the metadata means that the attribute can have a value per language instead of a single value. NO : The attribute is not set as multilingual. Setting IsMultiLingual to False in the metadata means that the attribute has only one value, independent of language. |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_CUBE_ATTRIBUTES describes the attributes for all OLAP cube dimensions in the database. USER_CUBE_ATTRIBUTES describes the attributes for the OLAP cube dimensions owned by the current user. This view does not display the OWNER column. See Also: " DBA_CUBE_ATTRIBUTES " " USER_CUBE_ATTRIBUTES " See Also: " DBA_CUBE_ATTRIBUTES " " USER_CUBE_ATTRIBUTES "