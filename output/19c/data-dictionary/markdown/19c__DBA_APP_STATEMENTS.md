---
id: 19c__DBA_APP_STATEMENTS
name: DBA_APP_STATEMENTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_APP_STATEMENTS.html
---

# DBA_APP_STATEMENTS

DBA_APP_STATEMENTS describes all statements from all the applications in the Application Container.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ORIGIN_CON_ID | NUMBER | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n =1 if the row originates in root) |
| STATEMENT_ID | NUMBER | Statement ID |
| CAPTURE_TIME | DATE | Time of capture of the application statement |
| APP_STATEMENT | CLOB | Application statement |
| APP_NAME | VARCHAR2(128) | Name of the application whose statement was captured |
| APP_STATUS | VARCHAR2(12) | Status of the application when the statement was captured |
| PATCH_NUMBER | NUMBER | Patch number of patch installation when the statement was captured |
| VERSION_NUMBER | NUMBER | Version number when the statement was captured |
| SESSION_ID | NUMBER | Unique session ID when the statement was captured |
| OPCODE | NUMBER | Operation code indicating the statement type |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content