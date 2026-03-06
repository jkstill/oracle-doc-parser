---
id: 19c__ALL_ANALYTIC_VIEW_CLASS
name: ALL_ANALYTIC_VIEW_CLASS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_ANALYTIC_VIEW_CLASS.html
---

# ALL_ANALYTIC_VIEW_CLASS

ALL_ANALYTIC_VIEW_CLASS describes the classifications of the analytic views accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the analytic view |
| ANALYTIC_VIEW_NAME | VARCHAR2(128) | Name of the analytic view |
| CLASSIFICATION | VARCHAR2(128) | Classification associated with the analytic view |
| VALUE | CLOB | Value of the classification or NULL if not specified |
| LANGUAGE | VARCHAR2(64) | NLS_LANGUAGE value associated with the classification or NULL if not specified |
| ORDER_NUM | NUMBER | Order of the classification in the list of classifications associated with the analytic view |
| ORIGIN_CON_ID | NUMBER | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root). |

## Usage Notes

Related Views DBA_ANALYTIC_VIEW_CLASS describes the classifications of all analytic views in the database. USER_ANALYTIC_VIEW_CLASS describes the classifications of the analytic views owned by the current user. This view does not display the OWNER column. See Also: " DBA_ANALYTIC_VIEW_CLASS " " USER_ANALYTIC_VIEW_CLASS " See Also: " DBA_ANALYTIC_VIEW_CLASS " " USER_ANALYTIC_VIEW_CLASS "