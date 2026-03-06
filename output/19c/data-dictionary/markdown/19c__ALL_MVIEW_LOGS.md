---
id: 19c__ALL_MVIEW_LOGS
name: ALL_MVIEW_LOGS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [all]
source_file: ALL_MVIEW_LOGS.html
---

# ALL_MVIEW_LOGS

ALL_MVIEW_LOGS describes all materialized view logs accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| LOG_OWNER | VARCHAR2(128) | Owner of the materialized view log |
| MASTER | VARCHAR2(128) | Name of the master table or master materialized view whose changes are logged |
| LOG_TABLE | VARCHAR2(128) | Name of the table where the changes to the master table or master materialized view are logged |
| LOG_TRIGGER | VARCHAR2(128) | Obsolete with Oracle8 i and later. Set to NULL. Formerly, this parameter was an after-row trigger on the master which inserted rows into the log. |
| ROWIDS | VARCHAR2(3) | Indicates whether rowid information is recorded ( YES ) or not ( NO ) |
| PRIMARY_KEY | VARCHAR2(3) | Indicates whether primary key information is recorded ( YES ) or not ( NO ) |
| OBJECT_ID | VARCHAR2(3) | Indicates whether object identifier information in an object table is recorded ( YES ) or not ( NO ) |
| FILTER_COLUMNS | VARCHAR2(3) | Indicates whether filter column information is recorded ( YES ) or not ( NO ) |
| SEQUENCE | VARCHAR2(3) | Indicates whether the sequence value, which provides additional ordering information, is recorded ( YES ) or not ( NO ) |
| INCLUDE_NEW_VALUES | VARCHAR2(3) | Indicates whether both old and new values are recorded ( YES ) or old values are recorded but new values are not recorded ( NO ) |
| PURGE_ASYNCHRONOUS | VARCHAR2(3) | Indicates whether the materialized view log is purged asynchronously ( YES ) or not ( NO ) |
| PURGE_DEFERRED | VARCHAR2(3) | Indicates whether the materialized view log is purged in a deferred manner ( YES ) or not ( NO ) |
| PURGE_START | DATE | For deferred purge, the purge start date |
| PURGE_INTERVAL | VARCHAR2(200) | For deferred purge, the purge interval |
| LAST_PURGE_DATE | DATE | Date of the last purge |
| LAST_PURGE_STATUS | NUMBER | Status of the last purge (error code or 0 for success) |
| NUM_ROWS_PURGED | NUMBER | Number of rows purged in the last purge |
| COMMIT_SCN_BASED | VARCHAR2(3) | Indicates whether the materialized view log is commit SCN-based ( YES ) or not ( NO ) |
| STAGING_LOG | VARCHAR2(3) | Indicates whether the materialized view log is a staging log for synchronous refresh ( YES ) or not ( NO ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_MVIEW_LOGS describes all materialized view logs in the database. USER_MVIEW_LOGS describes all materialized view logs owned by the current user. See Also: " DBA_MVIEW_LOGS " " USER_MVIEW_LOGS " See Also: " DBA_MVIEW_LOGS " " USER_MVIEW_LOGS "