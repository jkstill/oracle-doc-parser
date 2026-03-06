---
id: 19c__DBA_SR_STLOG_STATS
name: DBA_SR_STLOG_STATS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_SR_STLOG_STATS.html
---

# DBA_SR_STLOG_STATS

DBA_SR_STLOG_STATS provides information on the statistics in the staging logs for the tables processed by DBMS_SYNC_REFRESH.PREPARE_STAGING_LOG .

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the base table registered for synchronous refresh |
| TABLE_NAME | VARCHAR2(128) | Name of the table |
| STAGING_LOG_NAME | VARCHAR2(128) | Name of the staging log for tables. NULL for materialized views |
| NUM_INSERTS | NUMBER | The number of inserts in the staging log |
| NUM_DELETES | NUMBER | The number of deletes in the staging log |
| NUM_UPDATES | NUMBER | The number of updates in the staging log |
| PSL_MODE | VARCHAR2(33) | The mode specified by the user in running DBMS_SYNC_REFRESH.PREPARE_STAGING_LOG . Possible values: DELETE_TRUSTED DELETE_TRUSTED and UPDATE_TRUSTED ENFORCED INSERT_TRUSTED INSERT_TRUSTED and DELETE_TRUSTED TRUSTED UPDATE_TRUSTED UPDATE_TRUSTED and INSERT_TRUSTED |

## Usage Notes

These three statistics columns in the staging log are filled in PREPARE_STAGING_LOG : The number of inserts ( NUM_INSERTS ) The number of deletes ( NUM_DELETES ) The number of updates ( NUM_UPDATES ) After the data in the staging logs of a synchronous refresh group have been processed by PREPARE_REFRESH and EXECUTE_REFRESH , the statistics columns for the tables in the group are cleared and appear as NULL . Related View USER_SR_STLOG_STATS provides information on the statistics in the staging logs for the tables belonging to the current user processed by DBMS_SYNC_REFRESH.PREPARE_STAGING_LOG . See Also: " USER_SR_STLOG_STATS " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_SYNC_REFRESH package See Also: " USER_SR_STLOG_STATS " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_SYNC_REFRESH package