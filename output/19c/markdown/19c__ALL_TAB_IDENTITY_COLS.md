---
id: 19c__ALL_TAB_IDENTITY_COLS
name: ALL_TAB_IDENTITY_COLS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_TAB_IDENTITY_COLS.html
---

# ALL_TAB_IDENTITY_COLS

ALL_TAB_IDENTITY_COLS describes all table identity columns.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the table |
| TABLE_NAME | VARCHAR2(128) | Name of the table |
| COLUMN_NAME | VARCHAR2(128) | Name of the identity column |
| GENERATION_TYPE | VARCHAR2(10) | Generation type of the identity column. Possible values are ALWAYS or BY DEFAULT . |
| SEQUENCE_NAME | VARCHAR2(128) | Name of the sequence associated with the identity column |
| IDENTITY_OPTIONS | VARCHAR2(298) | Options for the identity column sequence generator |

## Usage Notes

Related Views DBA_TAB_IDENTITY_COLS describes all table identity columns. USER_TAB_IDENTITY_COLS describes all table identity columns. This view does not display the OWNER column. See Also: " DBA_TAB_IDENTITY_COLS " " USER_TAB_IDENTITY_COLS " See Also: The ALTER TABLE statement in Oracle Database SQL Language Reference for more information about creating an identity column The CREATE TABLE statements in Oracle Database SQL Language Reference for more information about creating an identity column See Also: " DBA_TAB_IDENTITY_COLS " " USER_TAB_IDENTITY_COLS " See Also: The ALTER TABLE statement in Oracle Database SQL Language Reference for more information about creating an identity column The CREATE TABLE statements in Oracle Database SQL Language Reference for more information about creating an identity column