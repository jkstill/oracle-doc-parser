---
id: 19c__ALL_MEASURE_FOLDER_SUBFOLDERS
name: ALL_MEASURE_FOLDER_SUBFOLDERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_MEASURE_FOLDER_SUBFOLDERS.html
---

# ALL_MEASURE_FOLDER_SUBFOLDERS

ALL_MEASURE_FOLDER_SUBFOLDERS describes the OLAP measure folders contained within the OLAP measure folders accessible to the user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the OLAP measure folder that contains a subfolder |
| MEASURE_FOLDER_NAME | VARCHAR2(128) | Name of the OLAP measure folder that contains a subfolder |
| MEASURE_SUBFOLDER_OWNER | VARCHAR2(128) | Owner of the OLAP measure folder subfolder |
| MEASURE_SUBFOLDER_NAME | VARCHAR2(128) | Name of the owning OLAP measure folder subfolder |

## Usage Notes

Related Views DBA_MEASURE_FOLDER_SUBFOLDERS describes the OLAP measure folders contained within the database OLAP measure folders. USER_MEASURE_FOLDER_SUBFOLDERS describes the OLAP measure folders contained within the OLAP measure folders owned by the current user. This view does not display the OWNER column. See Also: " DBA_MEASURE_FOLDER_SUBFOLDERS " " USER_MEASURE_FOLDER_SUBFOLDERS " See Also: " DBA_MEASURE_FOLDER_SUBFOLDERS " " USER_MEASURE_FOLDER_SUBFOLDERS "