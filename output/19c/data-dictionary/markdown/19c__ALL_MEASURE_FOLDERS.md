---
id: 19c__ALL_MEASURE_FOLDERS
name: ALL_MEASURE_FOLDERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_MEASURE_FOLDERS.html
---

# ALL_MEASURE_FOLDERS

ALL_MEASURE_FOLDERS describes the OLAP measure folders accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the measure folder |
| MEASURE_FOLDER_NAME | VARCHAR2(128) | Name of a measure folder |
| MEASURE_FOLDER_ID | NUMBER | ID of a measure folder |
| DESCRIPTION | NVARCHAR2(300) | Description of the measure folder in the session language |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_MEASURE_FOLDERS describes all OLAP measure folders in the database. USER_MEASURE_FOLDERS describes the OLAP measure folders owned by the current user. This view does not display the OWNER column. See Also: " DBA_MEASURE_FOLDERS " " USER_MEASURE_FOLDERS " See Also: " DBA_MEASURE_FOLDERS " " USER_MEASURE_FOLDERS "