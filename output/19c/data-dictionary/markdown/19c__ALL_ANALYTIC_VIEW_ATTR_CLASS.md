---
id: 19c__ALL_ANALYTIC_VIEW_ATTR_CLASS
name: ALL_ANALYTIC_VIEW_ATTR_CLASS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_ANALYTIC_VIEW_ATTR_CLASS.html
---

# ALL_ANALYTIC_VIEW_ATTR_CLASS

ALL_ANALYTIC_VIEW_ATTR_CLASS describes the attribute classifications of the analytic views accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the analytic view |
| ANALYTIC_VIEW_NAME | VARCHAR2(128) | Name of analytic view |
| DIMENSION_ALIAS | VARCHAR2(128) | Alias of the attribute dimension in the analytic view |
| HIER_ALIAS | VARCHAR2(128) | Alias of the hierarchy specified by an attribute dimension in the analytic view |
| ATTRIBUTE_NAME | VARCHAR2(128) | Name of the attribute within the analytic view |
| CLASSIFICATION | VARCHAR2(128) | Name of analytic view attribute classification |
| VALUE | CLOB | Value of attribute classification |
| LANGUAGE | VARCHAR2(64) | Language of attribute classification |
| ORDER_NUM | NUMBER | Order number of the attribute classification |
| ORIGIN_CON_ID | NUMBER | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root). |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_ANALYTIC_VIEW_ATTR_CLASS describes the attribute classifications of all analytic views in the database. USER_ANALYTIC_VIEW_ATTR_CLASS describes the attribute classifications of the analytic views owned by the current user. This view does not display the OWNER column. See Also: " DBA_ANALYTIC_VIEW_ATTR_CLASS " " USER_ANALYTIC_VIEW_ATTR_CLASS " See Also: " DBA_ANALYTIC_VIEW_ATTR_CLASS " " USER_ANALYTIC_VIEW_ATTR_CLASS "