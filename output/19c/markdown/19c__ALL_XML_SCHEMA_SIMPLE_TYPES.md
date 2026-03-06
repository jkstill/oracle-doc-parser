---
id: 19c__ALL_XML_SCHEMA_SIMPLE_TYPES
name: ALL_XML_SCHEMA_SIMPLE_TYPES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_XML_SCHEMA_SIMPLE_TYPES.html
---

# ALL_XML_SCHEMA_SIMPLE_TYPES

ALL_XML_SCHEMA_SIMPLE_TYPES describes all simple types accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | The user who owns the type |
| SCHEMA_URL | VARCHAR2(700) | The URL of the schema within which the type is defined Refer to the See Also note below for links to more information about the schemaurl attribute for an XML schema. |
| TARGET_NAMESPACE | VARCHAR2(2000) | The namespace of the type |
| SIMPLE_TYPE_NAME | VARCHAR2(256) | Name of the simple type |
| SIMPLE_TYPE | XMLTYPE(XMLSchema "http://xmlns.oracle.com/xdb/XDBSchema.xsd" Element "simpleType") | The actual XMLType of the type |

## Usage Notes

Related Views DBA_XML_SCHEMA_SIMPLE_TYPES describes all simple types. USER_XML_SCHEMA_SIMPLE_TYPES describes all simple types owned by the current user. This view does not display the OWNER column. See Also: " DBA_XML_SCHEMA_SIMPLE_TYPES " " USER_XML_SCHEMA_SIMPLE_TYPES " Oracle XML DB Developer’s Guide for information about registering an XML schema with Oracle XML DB Oracle XML DB Developer’s Guide for information about restrictions for an XML schema URL See Also: " DBA_XML_SCHEMA_SIMPLE_TYPES " " USER_XML_SCHEMA_SIMPLE_TYPES " Oracle XML DB Developer’s Guide for information about registering an XML schema with Oracle XML DB Oracle XML DB Developer’s Guide for information about restrictions for an XML schema URL