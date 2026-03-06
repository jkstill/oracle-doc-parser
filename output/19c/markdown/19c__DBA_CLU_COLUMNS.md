---
id: 19c__DBA_CLU_COLUMNS
name: DBA_CLU_COLUMNS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [dba]
source_file: DBA_CLU_COLUMNS.html
---

# DBA_CLU_COLUMNS

DBA_CLU_COLUMNS maps all table columns to related cluster columns.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the cluster |
| CLUSTER_NAME | VARCHAR2(128) | Name of the cluster |
| CLU_COLUMN_NAME | VARCHAR2(128) | Key column in the cluster |
| TABLE_NAME | VARCHAR2(128) | Clustered table name |
| TAB_COLUMN_NAME | VARCHAR2(4000) | Key column or attribute of the object type column |

## Usage Notes

Related View USER_CLU_COLUMNS maps all table columns owned by the current user to related cluster columns. This view does not display the OWNER column. See Also: " USER_CLU_COLUMNS " See Also: " USER_CLU_COLUMNS "