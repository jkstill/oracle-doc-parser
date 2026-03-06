---
id: 19c__ALL_ANALYTIC_VIEW_BAS_MEAS_AE
name: ALL_ANALYTIC_VIEW_BAS_MEAS_AE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_ANALYTIC_VIEW_BAS_MEAS_AE.html
---

# ALL_ANALYTIC_VIEW_BAS_MEAS_AE

ALL_ANALYTIC_VIEW_BAS_MEAS_AE describes the base measures in the analytic views (across all editions) accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the analytic view |
| ANALYTIC_VIEW_NAME | VARCHAR2(128) | Name of the analytic view |
| MEASURE_NAME | VARCHAR2(128) | Name of the analytic view base measure |
| TABLE_ALIAS | VARCHAR2(128) | Alias of the table or view in the USING clause to which the column belongs |
| COLUMN_NAME | VARCHAR2(128) | Column name in the table or view on which this measure is defined |
| AGGR_FUNCTION | VARCHAR2(128) | Aggregation operator specified for this measure or NULL if not specified |
| ORDER_NUM | NUMBER | Order number of the base measure in the list of measures in the analytic view |
| ORIGIN_CON_ID | NUMBER | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root). |
| EDITION_NAME | VARCHAR2(128) | Name of the application edition where the analytic view is defined |

## Usage Notes

Related Views DBA_ANALYTIC_VIEW_BAS_MEAS_AE describes the base measures in all analytic views (across all editions) in the database. USER_ANALYTIC_VIEW_BAS_MEAS_AE describes the base measures in the analytic views (across all editions) owned by the current user. This view does not display the OWNER column. Note: This view is available starting with Oracle Database release 19c, version 19.13. See Also: " DBA_ANALYTIC_VIEW_BAS_MEAS_AE " " USER_ANALYTIC_VIEW_BAS_MEAS_AE " Note: This view is available starting with Oracle Database release 19c, version 19.13. See Also: " DBA_ANALYTIC_VIEW_BAS_MEAS_AE " " USER_ANALYTIC_VIEW_BAS_MEAS_AE "