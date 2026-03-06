---
id: 19c__ALL_XML_OUT_OF_LINE_TABLES
name: ALL_XML_OUT_OF_LINE_TABLES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_XML_OUT_OF_LINE_TABLES.html
---

# ALL_XML_OUT_OF_LINE_TABLES

ALL_XML_OUT_OF_LINE_TABLES descibes all the out of line tables connected to a given root table for the same schema accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SCHEMA_URL | VARCHAR2(700) | The URL of the schema within which the out of line table is defined Refer to the See Also note below for links to more information about the schemaurl attribute for an XML schema. |
| SCHEMA_OWNER | VARCHAR2(128) | Owner of the schema |
| TABLE_NAME | VARCHAR2(128) | Name of the out of line table |
| TABLE_OWNER | VARCHAR2(128) | Owner of the out of line table |

## Usage Notes

Related Views DBA_XML_OUT_OF_LINE_TABLES describes all the out of line tables connected to a given root table for the same schema in the database. USER_XML_OUT_OF_LINE_TABLES describes all the out of line tables connected to a given root table for the same schema owned by the current user. This view does not display the TABLE_OWNER column. See Also: " DBA_XML_OUT_OF_LINE_TABLES " " USER_XML_OUT_OF_LINE_TABLES " Oracle XML DB Developer’s Guide for information about registering an XML schema with Oracle XML DB Oracle XML DB Developer’s Guide for information about restrictions for an XML schema URL See Also: " DBA_XML_OUT_OF_LINE_TABLES " " USER_XML_OUT_OF_LINE_TABLES " Oracle XML DB Developer’s Guide for information about registering an XML schema with Oracle XML DB Oracle XML DB Developer’s Guide for information about restrictions for an XML schema URL