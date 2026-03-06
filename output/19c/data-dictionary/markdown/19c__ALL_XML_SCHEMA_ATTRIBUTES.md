---
id: 19c__ALL_XML_SCHEMA_ATTRIBUTES
name: ALL_XML_SCHEMA_ATTRIBUTES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_XML_SCHEMA_ATTRIBUTES.html
---

# ALL_XML_SCHEMA_ATTRIBUTES

ALL_XML_SCHEMA_ATTRIBUTES describes all the attributes and their properties accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | The user who owns the attribute |
| SCHEMA_URL | VARCHAR2(700) | The URL of the schema within which the attribute is defined Refer to the See Also note below for links to more information about the schemaurl attribute for an XML schema. |
| TARGET_NAMESPACE | VARCHAR2(2000) | The namespace of the attribute |
| ATTRIBUTE_NAME | VARCHAR2(2000) | Name of the attribute |
| IS_REF | NUMBER | Indicates whether an attribute was defined using a reference in the XML schema ( 1 ) or not ( 0 ) |
| TYPE_NAME | VARCHAR2(2000) | Name of the type of the attribute |
| GLOBAL | RAW(1) | Indicates whether the attribute is global ( 1 ) or not ( 0 ) |
| ATTRIBUTE | XMLTYPE | Actual XMLType for the attribute |
| ELEMENT_ID | RAW(20) | Element ID of the element to which the attribute belongs |
| SQL_TYPE | VARCHAR2(128) | XDB annotation for sqlType |
| SQL_NAME | VARCHAR2(128) | XDB annotation value for sqlName |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_XML_SCHEMA_ATTRIBUTES describes all the attributes and their properties accessible to the current user in the database. USER_XML_SCHEMA_ATTRIBUTES describes all the attributes and their properties owned by the current user. This view does not display the OWNER column. See Also: " DBA_XML_SCHEMA_ATTRIBUTES " " USER_XML_SCHEMA_ATTRIBUTES " Oracle XML DB Developer’s Guide for information about registering an XML schema with Oracle XML DB Oracle XML DB Developer’s Guide for information about restrictions for an XML schema URL See Also: " DBA_XML_SCHEMA_ATTRIBUTES " " USER_XML_SCHEMA_ATTRIBUTES " Oracle XML DB Developer’s Guide for information about registering an XML schema with Oracle XML DB Oracle XML DB Developer’s Guide for information about restrictions for an XML schema URL