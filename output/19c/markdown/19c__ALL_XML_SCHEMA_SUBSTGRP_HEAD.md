---
id: 19c__ALL_XML_SCHEMA_SUBSTGRP_HEAD
name: ALL_XML_SCHEMA_SUBSTGRP_HEAD
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_XML_SCHEMA_SUBSTGRP_HEAD.html
---

# ALL_XML_SCHEMA_SUBSTGRP_HEAD

ALL_XML_SCHEMA_SUBSTGRP_HEAD describes the heads of substitution groups accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | The user who owns the element |
| SCHEMA_URL | VARCHAR2(700) | The URL of the schema within which the element is defined Refer to the See Also note below for links to more information about the schemaurl attribute for an XML schema. |
| TARGET_NAMESPACE | VARCHAR2(2000) | The namespace of the element |
| ELEMENT_NAME | VARCHAR2(256) | Name of the element |
| ELEMENT | XMLTYPE(XMLSchema "http://xmlns.oracle.com/xdb/XDBSchema.xsd" Element "element") | The actual XML fragment of the element |

## Usage Notes

Related Views DBA_XML_SCHEMA_SUBSTGRP_HEAD describes the heads of substitution groups. USER_XML_SCHEMA_SUBSTGRP_HEAD describes the heads of substitution groups owned by the current user. This view does not display the OWNER column. See Also: " DBA_XML_SCHEMA_SUBSTGRP_HEAD " " USER_XML_SCHEMA_SUBSTGRP_HEAD " Oracle XML DB Developer’s Guide for information about registering an XML schema with Oracle XML DB Oracle XML DB Developer’s Guide for information about restrictions for an XML schema URL See Also: " DBA_XML_SCHEMA_SUBSTGRP_HEAD " " USER_XML_SCHEMA_SUBSTGRP_HEAD " Oracle XML DB Developer’s Guide for information about registering an XML schema with Oracle XML DB Oracle XML DB Developer’s Guide for information about restrictions for an XML schema URL