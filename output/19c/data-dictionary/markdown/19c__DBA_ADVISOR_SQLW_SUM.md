---
id: 19c__DBA_ADVISOR_SQLW_SUM
name: DBA_ADVISOR_SQLW_SUM
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dba]
source_file: DBA_ADVISOR_SQLW_SUM.html
---

# DBA_ADVISOR_SQLW_SUM

DBA_ADVISOR_SQLW_SUM displays an aggregated picture of all SQLWkld workload objects in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the workload object |
| WORKLOAD_ID | NUMBER | Unique identifier number of the workload object |
| WORKLOAD_NAME | VARCHAR2(128) | Unique name of the workload |
| DESCRIPTION | VARCHAR2(256) | User-specified description of the workload |
| CREATE_DATE | DATE | Date on which the workload object was created |
| MODIFY_DATE | DATE | Date of last update to the current workload |
| NUM_SELECT_STMT | NUMBER | Number of SELECT statements in the workload |
| NUM_UPDATE_STMT | NUMBER | Number of UPDATE statements in the workload |
| NUM_DELETE_STMT | NUMBER | Number of DELETE statements in the workload |
| NUM_INSERT_STMT | NUMBER | Number of INSERT statements in the workload |
| NUM_MERGE_STMT | NUMBER | Number of MERGE statements in the workload |
| SOURCE | VARCHAR2(128) | Optional name that identifies the creator of the object |
| HOW_CREATED | VARCHAR2(30) | Optional object or template on which the object was based |
| DATA_SOURCE | VARCHAR2(2000) | Workload data source |
| READ_ONLY | VARCHAR2(5) | Indicates whether or not the workload can be modified or deleted ( TRUE ) or not ( FALSE ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View USER_ADVISOR_SQLW_SUM displays an aggregated picture of the SQLWkld workload objects owned by the current user. This view does not display the OWNER column. See Also: " USER_ADVISOR_SQLW_SUM " See Also: " USER_ADVISOR_SQLW_SUM "