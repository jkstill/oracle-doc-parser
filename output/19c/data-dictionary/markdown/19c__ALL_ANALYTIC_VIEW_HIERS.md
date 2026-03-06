---
id: 19c__ALL_ANALYTIC_VIEW_HIERS
name: ALL_ANALYTIC_VIEW_HIERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_ANALYTIC_VIEW_HIERS.html
---

# ALL_ANALYTIC_VIEW_HIERS

ALL_ANALYTIC_VIEW_HIERS describes the hierarchies in the analytic views accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the analytic view hierarchy |
| ANALYTIC_VIEW_NAME | VARCHAR2(128) | Name of the analytic view |
| DIMENSION_ALIAS | VARCHAR2(128) | Alias of the attribute dimension in the analytic view |
| HIER_OWNER | VARCHAR2(128) | Owner of the hierarchy |
| HIER_NAME | VARCHAR2(128) | Name of the hierarchy |
| HIER_ALIAS | VARCHAR2(128) | Alias specified for the hierarchy |
| IS_DEFAULT | VARCHAR2(1) | Indicates whether this is the default hierarchy for the analytic view dimension in the analytic view ( Y ) or not ( N ) |
| ORDER_NUM | NUMBER | Order of the hierarchy in the list of hierarchies in the analytic view |
| ORIGIN_CON_ID | NUMBER | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root). |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_ANALYTIC_VIEW_HIERS describes the hierarchies in all analytic views in the database. USER_ANALYTIC_VIEW_HIERS describes the hierarchies in the analytic views owned by the current user. This view does not display the OWNER column. See Also: " DBA_ANALYTIC_VIEW_HIERS " " USER_ANALYTIC_VIEW_HIERS " See Also: " DBA_ANALYTIC_VIEW_HIERS " " USER_ANALYTIC_VIEW_HIERS "