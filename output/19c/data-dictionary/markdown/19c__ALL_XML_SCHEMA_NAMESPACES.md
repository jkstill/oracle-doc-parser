---
id: 19c__ALL_XML_SCHEMA_NAMESPACES
name: ALL_XML_SCHEMA_NAMESPACES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_XML_SCHEMA_NAMESPACES.html
---

# ALL_XML_SCHEMA_NAMESPACES

ALL_XML_SCHEMA_NAMESPACES describes all the available namespaces accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | User who owns the namespace |
| TARGET_NAMESPACE | VARCHAR2(2000) | The target namespace |
| SCHEMA_URL | VARCHAR2(700) | The URL of the schema Refer to the See Also note below for links to more information about the schemaurl attribute for an XML schema. |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_XML_SCHEMA_NAMESPACES describes all the available namespaces. USER_XML_SCHEMA_NAMESPACES describes all the available namespaces owned by the current user. This view does not display the OWNER column. See Also: " DBA_XML_SCHEMA_NAMESPACES " " USER_XML_SCHEMA_NAMESPACES " Oracle XML DB Developer’s Guide for information about registering an XML schema with Oracle XML DB Oracle XML DB Developer’s Guide for information about restrictions for an XML schema URL See Also: " DBA_XML_SCHEMA_NAMESPACES " " USER_XML_SCHEMA_NAMESPACES " Oracle XML DB Developer’s Guide for information about registering an XML schema with Oracle XML DB Oracle XML DB Developer’s Guide for information about restrictions for an XML schema URL