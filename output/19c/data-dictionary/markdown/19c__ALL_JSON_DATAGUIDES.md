---
id: 19c__ALL_JSON_DATAGUIDES
name: ALL_JSON_DATAGUIDES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_JSON_DATAGUIDES.html
---

# ALL_JSON_DATAGUIDES

ALL_JSON_DATAGUIDES provides information on the JavaScript Object Notation (JSON) columns accessible to the current user that have data guide enabled.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the table containing the JSON column |
| TABLE_NAME | VARCHAR2(128) | Name of the table containing the JSON column |
| COLUMN_NAME | VARCHAR2(128) | Name of the JSON column that has data guide enabled |
| DATAGUIDE | CLOB | The data guide of the JSON column in flat format |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_JSON_DATAGUIDES provides information on the JavaScript Object Notation (JSON) columns in the database that have data guide enabled. Its columns are the same as those in ALL_JSON_DATAGUIDES . USER_JSON_DATAGUIDES provides information on the JavaScript Object Notation (JSON) columns owned by the current user that have data guide enabled. This view does not display the OWNER column. See Also: " DBA_JSON_DATAGUIDES " " USER_JSON_DATAGUIDES " See Also: " DBA_JSON_DATAGUIDES " " USER_JSON_DATAGUIDES "