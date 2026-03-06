---
id: 19c__ALL_ANALYTIC_VIEW_LVLGRPS_AE
name: ALL_ANALYTIC_VIEW_LVLGRPS_AE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_ANALYTIC_VIEW_LVLGRPS_AE.html
---

# ALL_ANALYTIC_VIEW_LVLGRPS_AE

ALL_ANALYTIC_VIEW_LVLGRPS_AE describes the analytic view measure and level groups of the analytic views (across all editions) accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the analytic view |
| ANALYTIC_VIEW_NAME | VARCHAR2(128) | Name of the analytic view |
| CACHE_TYPE | VARCHAR2(128) | Type of the materialized view; one of the following: DYNAMIC MATERIALIZED (the default value) |
| DIMENSION_ALIAS | VARCHAR2(128) | Alias of the attribute dimension in the group |
| HIER_ALIAS | VARCHAR2(128) | Alias of the hierarchy associated with the attribute dimension in the group |
| LEVEL_NAME | VARCHAR2(128) | Name of the level in the hierarchy in the group |
| MEASURE_NAME | VARCHAR2(128) | Names of the measures in the group |
| AV_LVLGRP_ORDER | NUMBER | Order of the groups in the analytic view |
| LEVEL_MEAS_ORDER | NUMBER | Order of the levels and measures in the group |
| ORIGIN_CON_ID | NUMBER | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root). |
| EDITION_NAME | VARCHAR2(128) | Name of the application edition where the analytic view is defined |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_ANALYTIC_VIEW_LVLGRPS_AE describes the analytic view measure and level groups of all analytic views (across all editions) in the database. USER_ANALYTIC_VIEW_LVLGRPS_AE describes the analytic view measure and level groups of the analytic views (across all editions) owned by the current user. This view does not display the OWNER column. Note: This view is available starting with Oracle Database release 19c, version 19.13. See Also: " DBA_ANALYTIC_VIEW_LVLGRPS_AE " " USER_ANALYTIC_VIEW_LVLGRPS_AE " Note: This view is available starting with Oracle Database release 19c, version 19.13. See Also: " DBA_ANALYTIC_VIEW_LVLGRPS_AE " " USER_ANALYTIC_VIEW_LVLGRPS_AE "