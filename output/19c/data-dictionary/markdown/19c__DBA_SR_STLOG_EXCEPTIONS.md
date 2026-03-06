---
id: 19c__DBA_SR_STLOG_EXCEPTIONS
name: DBA_SR_STLOG_EXCEPTIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dba]
source_file: DBA_SR_STLOG_EXCEPTIONS.html
---

# DBA_SR_STLOG_EXCEPTIONS

DBA_SR_STLOG_EXCEPTIONS provides information on the exceptions in the staging logs for the tables processed by DBMS_SYNC_REFRESH . PREPARE_STAGING_LOG .

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the base table registered for synchronous refresh |
| TABLE_NAME | VARCHAR2(128) | Name of the base table registered for synchronous refresh |
| STAGING_LOG_NAME | VARCHAR2(128) | Name of the staging log for tables. This column has a value of NULL for materialized views. |
| BAD_ROWID | ROWID | Row ID of the staging log row causing the exception for the synchronous refresh |
| ERROR_NUMBER | NUMBER | Error number of the exception for the synchronous refresh |
| ERROR_MESSAGE | VARCHAR2(4000) | Error message associated with the ERROR_NUMBER for the synchronous refresh |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View USER_SR_STLOG_EXCEPTIONS provides information on the exceptions in the staging logs for the tables belonging to the current user processed by DBMS_SYNC_REFRESH . PREPARE_STAGING_LOG . Its columns are the same as those in DBA_SR_STLOG_EXCEPTIONS . See Also: " USER_SR_STLOG_EXCEPTIONS " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_SYNC_REFRESH package See Also: " USER_SR_STLOG_EXCEPTIONS " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_SYNC_REFRESH package