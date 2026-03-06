---
id: 19c__ALL_XML_VIEWS
name: ALL_XML_VIEWS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_XML_VIEWS.html
---

# ALL_XML_VIEWS

ALL_XML_VIEWS describes the XML views accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the XML view |
| VIEW_NAME | VARCHAR2(128) | Name of the XML view |
| XMLSCHEMA | VARCHAR2(700) | Name of the XML Schema that is used for the view definition |
| SCHEMA_OWNER | VARCHAR2(128) | Owner of the XML Schema that is used for the view definition |
| ELEMENT_NAME | VARCHAR2(2000) | Name of the XML SChema element that is used for the view |

## Usage Notes

Related Views DBA_XML_VIEWS describes all XML views the database. USER_XML_VIEWS describes the XML views owned by the current user. This view does not display the OWNER column. See Also: " DBA_XML_VIEWS " " USER_XML_VIEWS " See Also: " DBA_XML_VIEWS " " USER_XML_VIEWS "