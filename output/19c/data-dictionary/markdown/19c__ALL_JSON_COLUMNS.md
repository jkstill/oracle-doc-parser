---
id: 19c__ALL_JSON_COLUMNS
name: ALL_JSON_COLUMNS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_JSON_COLUMNS.html
---

# ALL_JSON_COLUMNS

For example, if a check constraint combines the IS JSON condition with another condition using logical condition OR, then the column is not listed in this view. In this case, it is not certain that the data in the column is JSON data. For example, the following constraint does not ensure that the data in column jcol is JSON data:

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the table with the JSON column |
| TABLE_NAME | VARCHAR2(128) | Name of the table with the JSON column |
| OBJECT_TYPE | VARCHAR2(5) | Object type: TABLE VIEW |
| COLUMN_NAME | VARCHAR2(128) | Name of the JSON column |
| FORMAT | VARCHAR2(9) | Format of the JSON data |
| DATA_TYPE | VARCHAR2(13) | Data type of the JSON column |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content For example, if a check constraint combines the IS JSON condition with another condition using logical condition OR, then the column is not listed in this view. In this case, it is not certain that the data in the column is JSON data. For example, the following constraint does not ensure that the data in column jcol is JSON data: jcol is json OR length(jcol) < 1000 Related Views DBA_JSON_COLUMNS provides information on all JSON columns. USER_JSON_COLUMNS provides information on the JSON columns for which the user is the owner. This view does not display the OWNER column. See Also: " DBA_JSON_COLUMNS " " USER_JSON_COLUMNS " Oracle XML DB Developer’s Guide for more information about using JSON with Oracle Database