---
id: 19c__ALL_JSON_DATAGUIDE_FIELDS
name: ALL_JSON_DATAGUIDE_FIELDS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_JSON_DATAGUIDE_FIELDS.html
---

# ALL_JSON_DATAGUIDE_FIELDS

ALL_JSON_DATAGUIDE_FIELDS extracts the path and type information from the data guides accessible to the current user, which are the data guides returned to the user by the ALL_JSON_DATAGUIDE view.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the table containing the JSON column |
| TABLE_NAME | VARCHAR2(128) | Name of the table containing the JSON column |
| COLUMN_NAME | VARCHAR2(128) | Name of the JSON column that has data guide enabled |
| PATH | VARCHAR2(4000) | Path to the JSON field in the data guide |
| TYPE | VARCHAR2(40) | Type of the JSON field in the data guide |
| LENGTH | NUMBER | Maximum length of the JSON field value, in bytes |

## Usage Notes

Related Views DBA_JSON_DATAGUIDE_FIELDS extracts the path and type information from all the data guides in the database, which are the data guides returned by the DBA_JSON_DATAGUIDE view. USER_JSON_DATAGUIDE_FIELDS extracts the path and type information from all the data guides in the current user’s schema, which are the data guides returned to the user by the USER_JSON_DATAGUIDE view. This view does not display the OWNER column. See Also: " DBA_JSON_DATAGUIDE_FIELDS " " USER_JSON_DATAGUIDE_FIELDS " See Also: " DBA_JSON_DATAGUIDE_FIELDS " " USER_JSON_DATAGUIDE_FIELDS "