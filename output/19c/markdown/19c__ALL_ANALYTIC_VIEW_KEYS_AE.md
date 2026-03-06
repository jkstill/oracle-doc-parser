---
id: 19c__ALL_ANALYTIC_VIEW_KEYS_AE
name: ALL_ANALYTIC_VIEW_KEYS_AE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_ANALYTIC_VIEW_KEYS_AE.html
---

# ALL_ANALYTIC_VIEW_KEYS_AE

ALL_ANALYTIC_VIEW_KEYS_AE describes the key columns of the attribute dimensions in the analytic views (across all editions) accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of analytic view |
| ANALYTIC_VIEW_NAME | VARCHAR2(128) | Name of the analytic view |
| DIMENSION_ALIAS | VARCHAR2(128) | Alias of the attribute dimension in the analytic view |
| AV_KEY_TABLE_ALIAS | VARCHAR2(128) | Table alias of the key column |
| AV_KEY_COLUMN | VARCHAR2(128) | Name of the column for the key |
| REF_DIMENSION_ATTR | VARCHAR2(128) | Name of the referenced attribute dimension attribute |
| ORDER_NUM | NUMBER | Order number of the key in the list of keys in the analytic view |
| ORIGIN_CON_ID | NUMBER | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root). |
| EDITION_NAME | VARCHAR2(128) | Name of the application edition where the analytic view is defined |

## Usage Notes

The keys reference attributes of the attribute dimensions of the analytic view. Related Views DBA_ANALYTIC_VIEW_KEYS_AE describes the key columns of the attribute dimensions in all analytic views (across all editions) in the database. USER_ANALYTIC_VIEW_KEYS_AE describes the key columns of the attribute dimensions in the analytic views (across all editions) owned by the current user. This view does not display the OWNER column. Note: This view is available starting with Oracle Database release 19c, version 19.13. See Also: " DBA_ANALYTIC_VIEW_KEYS_AE " " USER_ANALYTIC_VIEW_KEYS_AE " Note: This view is available starting with Oracle Database release 19c, version 19.13. See Also: " DBA_ANALYTIC_VIEW_KEYS_AE " " USER_ANALYTIC_VIEW_KEYS_AE "