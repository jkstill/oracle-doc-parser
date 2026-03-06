---
id: 19c__USER_JSON_COLUMNS
name: USER_JSON_COLUMNS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [user]
source_file: USER_JSON_COLUMNS.html
---

# USER_JSON_COLUMNS

USER_JSON_COLUMNS provides information on the JavaScript Object Notation (JSON) columns for which the user is the owner. Its columns (except for OWNER ) are the same as those in ALL_JSON_COLUMNS .

## Usage Notes

Each column owned by the user that has an IS JSON check constraint in an AND condition appears in this view. This view enables a user to find all the JSON columns that he or she owns. For example, if a check constraint combines the IS JSON condition with another condition using logical condition OR, then the column is not listed in this view. In this case, it is not certain that the data in the column is JSON data. For example, the following constraint does not ensure that the data in column jcol is JSON data: jcol is json OR length(jcol) < 1000 See Also: " ALL_JSON_COLUMNS " Oracle XML DB Developer’s Guide for more information about using JSON with Oracle Database See Also: " ALL_JSON_COLUMNS " Oracle XML DB Developer’s Guide for more information about using JSON with Oracle Database