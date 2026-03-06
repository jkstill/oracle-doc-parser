---
id: 19c__DBA_MVREF_STATS_PARAMS
name: DBA_MVREF_STATS_PARAMS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_MVREF_STATS_PARAMS.html
---

# DBA_MVREF_STATS_PARAMS

DBA_MVREF_STATS_PARAMS displays the refresh statistics properties associated with each materialized view. These properties can be modified with the DBMS_MVIEW_STATS.SET_MVREF_STATS_PARAMS procedure.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| MV_OWNER | VARCHAR2(128) | Owner of the materialized view |
| MV_NAME | VARCHAR2(128) | Name of the materialized view |
| COLLECTION_LEVEL | VARCHAR2(8) | The collection level for the materialized view |
| RETENTION_PERIOD | NUMBER | The retention period for the materialize view |

## Usage Notes

Related View USER_MVREF_STATS_PARAMS displays the refresh statistics properties associated with each materialized view accessible to the current user. These properties can be modified with the DBMS_MVIEW_STATS.SET_MVREF_STATS_PARAMS procedure. See Also: " USER_MVREF_STATS_PARAMS " See Also: " USER_MVREF_STATS_PARAMS "