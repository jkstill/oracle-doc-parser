---
id: 19c__ALL_XML_SCHEMAS
name: ALL_XML_SCHEMAS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_XML_SCHEMAS.html
---

# ALL_XML_SCHEMAS

ALL_XML_SCHEMAS describes the registered XML schemas accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the XML schema |
| SCHEMA_URL | VARCHAR2(700) | Schema URL of the XML schema Refer to the See Also note below for links to more information about the schemaurl attribute for an XML schema. |
| LOCAL | VARCHAR2(3) | Indicates whether the XML schema is local ( YES ) or global ( NO ) |
| SCHEMA | XMLTYPE | XML schema document |
| INT_OBJNAME | VARCHAR2(4000) | Internal database object name for the schema |
| QUAL_SCHEMA_URL | VARCHAR2(865) | Fully qualified schema URL |
| HIER_TYPE | VARCHAR2(11) | Type of hierarchy for which the schema is enabled: NONE RESMETADATA CONTENTS |
| BINARY | VARCHAR2(3) | Indicates whether the XML Schema is registered for binary encoding usage ( YES ) or not ( NO ) |
| SCHEMA_ID | RAW(16) | Opaque schema identifier (16 bytes) |
| HIDDEN | VARCHAR2(3) | Indicates whether the XML Schema has been deleted in hidden mode ( YES ) or not ( NO ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_XML_SCHEMAS describes all registered XML schemas in the database. USER_XML_SCHEMAS describes the registered XML schemas owned by the current user. This view does not display the OWNER column. See Also: " DBA_XML_SCHEMAS " " USER_XML_SCHEMAS " Oracle XML DB Developer’s Guide for information about registering an XML schema with Oracle XML DB Oracle XML DB Developer’s Guide for information about restrictions for an XML schema URL See Also: " DBA_XML_SCHEMAS " " USER_XML_SCHEMAS " Oracle XML DB Developer’s Guide for information about registering an XML schema with Oracle XML DB Oracle XML DB Developer’s Guide for information about restrictions for an XML schema URL