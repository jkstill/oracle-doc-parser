---
id: 19c__DBA_TUNE_MVIEW
name: DBA_TUNE_MVIEW
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [dba]
source_file: DBA_TUNE_MVIEW.html
---

# DBA_TUNE_MVIEW

DBA_TUNE_MVIEW displays the result of executing the DBMS_ADVISOR.TUNE_MVIEW procedure.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the task |
| TASK_NAME | VARCHAR2(128) | Name of the task |
| ACTION_ID | NUMBER | Identifier of the action |
| SCRIPT_TYPE | VARCHAR2(14) | Type of the script: IMPLEMENTATION UNDO |
| STATEMENT | CLOB | Action statement |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View USER_TUNE_MVIEW displays the result of executing the DBMS_ADVISOR.TUNE_MVIEW procedure. This view does not display the OWNER column. See Also: " USER_TUNE_MVIEW " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_ADVISOR.TUNE_MVIEW procedure See Also: " USER_TUNE_MVIEW " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_ADVISOR.TUNE_MVIEW procedure