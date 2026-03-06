---
id: 19c__ALL_ANALYTIC_VIEW_COLUMNS_AE
name: ALL_ANALYTIC_VIEW_COLUMNS_AE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_ANALYTIC_VIEW_COLUMNS_AE.html
---

# ALL_ANALYTIC_VIEW_COLUMNS_AE

ALL_ANALYTIC_VIEW_COLUMNS_AE describes the columns of the analytic views (across all editions) accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the analytic view |
| ANALYTIC_VIEW_NAME | VARCHAR2(128) | Name of the analytic view |
| DIMENSION_NAME | VARCHAR2(128) | Alias of the analytic view dimension in the analytic view; for a measure the value is MEASURES |
| HIER_NAME | VARCHAR2(128) | Alias of the analytic view hierarchy within DIMENSION_NAME in the analytic view; for a measure the value is MEASURES |
| COLUMN_NAME | VARCHAR2(128) | Name of the column |
| ROLE | VARCHAR2(4) | The role the attribute plays in the analytic view: KEY AKEY HIER PROP MEAS |
| DATA_TYPE | VARCHAR2(106) | Datatype of the column |
| DATA_LENGTH | NUMBER | Length of the column (in bytes) |
| DATA_PRECISION | NUMBER | Decimal precision for the NUMBER datatype; binary precision for the FLOAT datatype, NULL for all other datatypes |
| DATA_SCALE | NUMBER | Number of digits to the right of the decimal point in a number |
| NULLABLE | CHAR(1) | Indicates whether a column allows NULL values; the value is N if there is a NOT NULL constraint on the column or if the column is part of a PRIMARY KEY |
| CHARACTER_SET_NAME | VARCHAR2(44) | Name of the character set: CHAR_CS NCHAR_CS |
| CHAR_COL_DECL_LENGTH | NUMBER | Declaration length of the character type column |
| CHAR_USED | VARCHAR2(1) | Indicates that the column uses BYTE length semantics ( B ) or CHAR length semantics ( C ), or whether the datatype is not any of the following (NULL): CHAR VARCHAR2 NCHAR NVARCHAR2 |
| ORDER_NUM | NUMBER | Order of the column, with the hierarchy columns first followed by measure columns. The columns for a hierarchy are grouped together, listed in their order in the HIERARCHIES clause of the analytic view definition. Within a hierarchy, attributes are listed first in order of their definition in the ATTRIBUTES clause of the attribute dimension definition followed by hierarchical attributes in the DIMENSION BY clause of the analytic view. |
| ORIGIN_CON_ID | NUMBER | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root). |
| EDITION_NAME | VARCHAR2(128) | Name of the application edition where the analytic view is defined |

## Usage Notes

Related Views DBA_ANALYTIC_VIEW_COLUMNS_AE describes the columns of all analytic views (across all editions) in the database. USER_ANALYTIC_VIEW_COLUMNS_AE describes the columns of the analytic views (across all editions) owned by the current user. This view does not display the OWNER column. Note: This view is available starting with Oracle Database release 19c, version 19.13. See Also: " DBA_ANALYTIC_VIEW_COLUMNS_AE " " USER_ANALYTIC_VIEW_COLUMNS_AE " Note: This view is available starting with Oracle Database release 19c, version 19.13. See Also: " DBA_ANALYTIC_VIEW_COLUMNS_AE " " USER_ANALYTIC_VIEW_COLUMNS_AE "