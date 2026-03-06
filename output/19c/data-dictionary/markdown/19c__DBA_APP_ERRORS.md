---
id: 19c__DBA_APP_ERRORS
name: DBA_APP_ERRORS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_APP_ERRORS.html
---

# DBA_APP_ERRORS

DBA_APP_ERRORS displays errors raised when an application PDB synchronizes with an application in the application root.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| APP_NAME | VARCHAR2(128) | Name of the application whose statement was captured |
| APP_STATEMENT | CLOB | Application statement |
| ERRORNUM | NUMBER | Error number for the statement |
| ERRORMSG | VARCHAR2(4000) | Error message for the statement |
| SYNC_TIME | DATE | Sync time for the statement |
| SYSTEM_IGNORABLE | VARCHAR2(1) | Indicates whether the error is a system-ignorable error ( Y ) or not ( N ) |
| USER_IGNORABLE | VARCHAR2(1) | Indicates whether the error is a user-ignorable error ( Y ) or not ( N ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view displays errors raised during the last synchronization for each application.