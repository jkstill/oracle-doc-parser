---
id: 19c__ALL_HIER_COLUMNS_AE
name: ALL_HIER_COLUMNS_AE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_HIER_COLUMNS_AE.html
---

# ALL_HIER_COLUMNS_AE

ALL_HIER_COLUMNS_AE describes the columns of the hierarchies (across all editions) accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the hierarchy |
| HIER_NAME | VARCHAR2(128) | Name of the hierarchy |
| COLUMN_NAME | VARCHAR2(128) | Name of the column |
| ROLE | VARCHAR2(4) | The role the attribute plays in the hierarchy: KEY AKEY HIER PROP |
| DATA_TYPE | VARCHAR2(106) | Datatype of the column |
| DATA_LENGTH | NUMBER | Length of the column (in bytes) |
| DATA_PRECISION | NUMBER | Decimal precision for the NUMBER datatype; binary precision for the FLOAT datatype, NULL for all other datatypes |
| DATA_SCALE | NUMBER | Number of digits to the right of the decimal point in a number |
| NULLABLE | CHAR(1) | Indicates whether a column allows NULL values; the value is N if there is a NOT NULL constraint on the column or if the column is part of a PRIMARY KEY |
| CHARACTER_SET_NAME | VARCHAR2(44) | Name of the character set: CHAR_CS NCHAR_CS |
| CHAR_COL_DECL_LENGTH | NUMBER | Declaration length of the character type column |
| CHAR_USED | VARCHAR2(1) | Indicates that the column uses BYTE length semantics ( B ) or CHAR length semantics ( C ), or whether the datatype is not any of the following (NULL): CHAR VARCHAR2 NCHAR NVARCHAR2 |
| ORDER_NUM | NUMBER | Order of the column, with attributes first in the order specified in the definition of the hierarchy followed by hierarchical attributes |
| ORIGIN_CON_ID | NUMBER | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root). |
| EDITION_NAME | VARCHAR2(128) | Name of the application edition where the hierarchy is defined |

## Usage Notes

Related Views DBA_HIER_COLUMNS_AE describes the columns of all hierarchies (across all editions) in the database. USER_HIER_COLUMNS_AE describes the columns of the hierarchies (across all editions) owned by the current user. This view does not display the OWNER column. Note: This view is available starting with Oracle Database release 19c, version 19.13. See Also: " DBA_HIER_COLUMNS_AE " " USER_HIER_COLUMNS_AE " Note: This view is available starting with Oracle Database release 19c, version 19.13. See Also: " DBA_HIER_COLUMNS_AE " " USER_HIER_COLUMNS_AE "