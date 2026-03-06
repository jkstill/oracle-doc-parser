---
id: 19c__ALL_ANALYTIC_VIEW_CLC_MEAS_AE
name: ALL_ANALYTIC_VIEW_CLC_MEAS_AE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_ANALYTIC_VIEW_CLC_MEAS_AE.html
---

# ALL_ANALYTIC_VIEW_CLC_MEAS_AE

ALL_ANALYTIC_VIEW_CLC_MEAS_AE describes the calculated measures in the analytic views (across all editions) accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the analytic view |
| ANALYTIC_VIEW_NAME | VARCHAR2(128) | Name of the analytic view |
| MEASURE_NAME | VARCHAR2(128) | Name of the analytic view calculated measure |
| MEAS_EXPRESSION | CLOB | Text of the expression for the measure |
| ORDER_NUM | NUMBER | Order number of the calculated measure in the list of the measures in the analytic view |
| ORIGIN_CON_ID | NUMBER | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root). |
| EDITION_NAME | VARCHAR2(128) | Name of the application edition where the analytic view is defined |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_ANALYTIC_VIEW_CLC_MEAS_AE describes the calculated measures in all analytic views (across all editions) in the database. USER_ANALYTIC_VIEW_CLC_MEAS_AE describes the calculated measures in the analytic views (across all editions) owned by the current user. This view does not display the OWNER column. Note: This view is available starting with Oracle Database release 19c, version 19.13. See Also: " DBA_ANALYTIC_VIEW_CLC_MEAS_AE " " USER_ANALYTIC_VIEW_CLC_MEAS_AE " Note: This view is available starting with Oracle Database release 19c, version 19.13. See Also: " DBA_ANALYTIC_VIEW_CLC_MEAS_AE " " USER_ANALYTIC_VIEW_CLC_MEAS_AE "