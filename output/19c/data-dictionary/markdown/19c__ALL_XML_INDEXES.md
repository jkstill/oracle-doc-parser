---
id: 19c__ALL_XML_INDEXES
name: ALL_XML_INDEXES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: index
tags: [all]
source_file: ALL_XML_INDEXES.html
---

# ALL_XML_INDEXES

ALL_XML_INDEXES describes the XML indexes accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| INDEX_OWNER | VARCHAR2(128) | Owner of the XML index |
| INDEX_NAME | VARCHAR2(128) | Name of the XML index |
| TABLE_OWNER | VARCHAR2(128) | Owner of the indexed object |
| TABLE_NAME | VARCHAR2(128) | Name of the indexed object |
| TYPE | VARCHAR2(10) | Type of the indexed column: REPOSITORY BINARY CLOB in OR CLOB |
| INDEX_TYPE | VARCHAR2(27) | Type of the index: STRUCTURED STRUCTURED and UNSTRUCTURED UNSTRUCTURED |
| PATH_TABLE_NAME | VARCHAR2(128) | Name of the path table |
| PARAMETERS | XMLTYPE | Indexed paths and Scheduler job information |
| ASYNC | VARCHAR2(9) | Asynchronous index type: ON-COMMIT MANUAL EVERY ALWAYS |
| STALE | VARCHAR2(5) | Indicates whether the index type is stale ( TRUE ) or not ( FALSE ) |
| PEND_TABLE_NAME | VARCHAR2(128) | Name of the pending table |
| EX_OR_INCLUDE | VARCHAR2(8) | Path subsetting: INCLUDE EXCLUDE FULLY IX |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_XML_INDEXES describes all XML indexes in the database. USER_XML_INDEXES describes the XML indexes owned by the current user. This view does not display the INDEX_OWNER column. See Also: " DBA_XML_INDEXES " " USER_XML_INDEXES " See Also: " DBA_XML_INDEXES " " USER_XML_INDEXES "