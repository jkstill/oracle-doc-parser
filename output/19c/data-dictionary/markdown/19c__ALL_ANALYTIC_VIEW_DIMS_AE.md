---
id: 19c__ALL_ANALYTIC_VIEW_DIMS_AE
name: ALL_ANALYTIC_VIEW_DIMS_AE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_ANALYTIC_VIEW_DIMS_AE.html
---

# ALL_ANALYTIC_VIEW_DIMS_AE

ALL_ANALYTIC_VIEW_DIMS_AE describes the attribute dimensions in the analytic views (across all editions) accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the analytic view |
| ANALYTIC_VIEW_NAME | VARCHAR2(128) | Name of the analytic view |
| DIMENSION_OWNER | VARCHAR2(128) | Owner of the schema containing the attribute dimension |
| DIMENSION_NAME | VARCHAR2(128) | Name of the attribute dimension |
| DIMENSION_ALIAS | VARCHAR2(128) | Alias of the attribute dimension in the analytic view |
| DIMENSION_TYPE | VARCHAR2(8) | Type of the attribute dimension: TIME STANDARD |
| ALL_MEMBER_NAME | CLOB | An expression for the name of the ALL member for the attribute dimension |
| ALL_MEMBER_CAPTION | CLOB | An expression for the caption for the ALL member of the attribute dimension, or NULL if not specified |
| ALL_MEMBER_DESCRIPTION | CLOB | An expression for the description for the ALL member of the attribute dimension, or NULL if not specified |
| REFERENCES_DISTINCT | VARCHAR2(1) | Indicates whether the reference between the fact table key and the attribute dimension attribute specifies the DISTINCT keyword. Possible values are: Y : The reference specifies the DISTINCT keyword. N : The reference does not specify the DISTINCT keyword. |
| ORDER_NUM | NUMBER | Order number of the attribute dimension in the analytic view |
| ORIGIN_CON_ID | NUMBER | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root). |
| EDITION_NAME | VARCHAR2(128) | Name of the application edition where the analytic view is defined |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_ANALYTIC_VIEW_DIMS_AE describes the attribute dimensions in all analytic views (across all editions) in the database. USER_ANALYTIC_VIEW_DIMS_AE describes the attribute dimensions in the analytic views (across all editions) owned by the current user. This view does not display the OWNER column. Note: This view is available starting with Oracle Database release 19c, version 19.13. See Also: " DBA_ANALYTIC_VIEW_DIMS_AE " " USER_ANALYTIC_VIEW_DIMS_AE " Note: This view is available starting with Oracle Database release 19c, version 19.13. See Also: " DBA_ANALYTIC_VIEW_DIMS_AE " " USER_ANALYTIC_VIEW_DIMS_AE "