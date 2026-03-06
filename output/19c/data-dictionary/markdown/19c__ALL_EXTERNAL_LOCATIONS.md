---
id: 19c__ALL_EXTERNAL_LOCATIONS
name: ALL_EXTERNAL_LOCATIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_EXTERNAL_LOCATIONS.html
---

# ALL_EXTERNAL_LOCATIONS

ALL_EXTERNAL_LOCATIONS describes the locations (data sources) of the external tables accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the external table location |
| TABLE_NAME | VARCHAR2(128) | Name of the corresponding external table |
| LOCATION | VARCHAR2(4000) | External table location clause |
| DIRECTORY_OWNER | CHAR(3) | Owner of the directory containing the external table location |
| DIRECTORY_NAME | VARCHAR2(128) | Name of the directory containing the external table location |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_EXTERNAL_LOCATIONS describes the locations (data sources) of all external tables in the database. USER_EXTERNAL_LOCATIONS describes the locations (data sources) of the external tables owned by the current user. This view does not display the OWNER column. See Also: " DBA_EXTERNAL_LOCATIONS " " USER_EXTERNAL_LOCATIONS " See Also: " DBA_EXTERNAL_LOCATIONS " " USER_EXTERNAL_LOCATIONS "