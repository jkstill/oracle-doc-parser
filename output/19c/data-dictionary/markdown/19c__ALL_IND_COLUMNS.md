---
id: 19c__ALL_IND_COLUMNS
name: ALL_IND_COLUMNS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_IND_COLUMNS.html
---

# ALL_IND_COLUMNS

ALL_IND_COLUMNS describes the columns of indexes on all tables accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| INDEX_OWNER | VARCHAR2(128) | Owner of the index |
| INDEX_NAME | VARCHAR2(128) | Name of the index |
| TABLE_OWNER | VARCHAR2(128) | Owner of the table or cluster |
| TABLE_NAME | VARCHAR2(128) | Name of the table or cluster |
| COLUMN_NAME | VARCHAR2(4000) | Column name or attribute of the object type column Note: If you create an index on a user-defined REF column, the system creates the index on the attributes that make up the REF column. Therefore, the column names displayed in this view are the attribute names, with the REF column name as a prefix, in the following form: "REF_name"."attribute" |
| COLUMN_POSITION | NUMBER | Position of the column or attribute within the index |
| COLUMN_LENGTH | NUMBER | Indexed length of the column |
| CHAR_LENGTH | NUMBER | Maximum codepoint length of the column |
| DESCEND | VARCHAR2(4) | Indicates whether the column is sorted in descending order ( DESC ) or ascending order ( ASC ) |
| COLLATED_COLUMN_ID | NUMBER | Internal sequence number of the column for which this column provides linguistic ordering |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_IND_COLUMNS describes the columns of indexes on all tables in the database. USER_IND_COLUMNS describes the columns of indexes owned by the current user and columns of indexes on tables owned by the current user. This view does not display the INDEX_OWNER or TABLE_OWNER columns. Note: For join indexes, the TABLE_NAME and TABLE_OWNER columns in this view may not match the TABLE_NAME and TABLE_OWNER columns you find in the *_INDEXES (and other similar) data dictionary views. Note: For join indexes, the TABLE_NAME and TABLE_OWNER columns in this view may not match the TABLE_NAME and TABLE_OWNER columns you find in the *_INDEXES (and other similar) data dictionary views. See Also: " DBA_IND_COLUMNS " " USER_IND_COLUMNS "