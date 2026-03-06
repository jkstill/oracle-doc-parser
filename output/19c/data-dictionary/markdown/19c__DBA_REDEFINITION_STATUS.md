---
id: 19c__DBA_REDEFINITION_STATUS
name: DBA_REDEFINITION_STATUS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_REDEFINITION_STATUS.html
---

# DBA_REDEFINITION_STATUS

DBA_REDEFINITION_STATUS is an online redefinition view. It provides information about the online redefinition status.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| REDEFINITION_ID | NUMBER(38) | ID for the redefinition object |
| BASE_TABLE_OWNER | VARCHAR2(128) | Owner of the base table of the redefinition object |
| BASE_TABLE_NAME | VARCHAR2(128) | Name of the base table of the redefinition object |
| BASE_OBJECT_NAME | VARCHAR2(128) | Name of the base object of the redefinition object |
| BASE_OBJECT_TYPE | VARCHAR2(9) | Type of the base object of the redefinition object |
| INTERIM_OBJECT_OWNER | VARCHAR2(128) | Owner of the interim object of the redefinition object |
| INTERIM_OBJECT_NAME | VARCHAR2(128) | Name of the interim object of the redefinition object |
| OPERATION | VARCHAR2(128) | The current redefinition operation: START_REDEF_TABLE SYNC_INTERIM_TABLE COPY_TABLE_DEPENDENTS FINISH_REDEF_TABLE |
| STATUS | VARCHAR2(128) | Status of the previous redefinition operation: FAILURE SUCCESS |
| RESTARTABLE | VARCHAR2(1) | Indicates whether the previous operation can be restarted |
| ERR_TXT | VARCHAR2(1000) | The error message raised from the previous operation |
| ACTION | VARCHAR2(400) | The suggested action |
| REFRESH_DEP_MVIEWS | VARCHAR2(1) | Indicates whether the online redefinition will also refresh dependent materialized views when syncing the interim table ( Y ) or not ( N ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: Oracle Database Administrator’s Guide for more information about online redefinition See Also: Oracle Database Administrator’s Guide for more information about online redefinition