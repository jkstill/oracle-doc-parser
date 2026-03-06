---
id: 19c__ALL_BLOCKCHAIN_TABLES
name: ALL_BLOCKCHAIN_TABLES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_BLOCKCHAIN_TABLES.html
---

# ALL_BLOCKCHAIN_TABLES

ALL_BLOCKCHAIN_TABLES describes the blockchain tables accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SCHEMA_NAME | VARCHAR2(128) | The schema containing the blockchain table |
| TABLE_NAME | VARCHAR2(128) | Name of the blockchain table |
| ROW_RETENTION | NUMBER | Row retention period for the blockchain table, that is, the minimum number of days a row must be retained and cannot be deleted after it is inserted into the table If the value of this column is NULL, then rows can never be deleted from the table. |
| ROW_RETENTION_LOCKED | VARCHAR2(3) | Indicates whether the row retention period for the blockchain table is locked. Possible values: YES : The row retention period is locked. You cannot change the row retention period NO : The row retention period is not locked. You can change the row retention period to a value higher than the current value with the SQL statement ALTER TABLE … NO DELETE UNTIL n DAYS AFTER INSERT |
| TABLE_INACTIVITY_RETENTION | NUMBER | Number of days for which the blockchain table must be inactive before it can be dropped, that is, the number of days that must pass after the most recent row insertion before the table can be dropped A table with no rows can be dropped at any time, regardless of this column value. |
| HASH_ALGORITHM | VARCHAR2(8) | Algorithm used for computing the hash value for each table row |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_BLOCKCHAIN_TABLES describes all blockchain tables in the database. USER_BLOCKCHAIN_TABLES describes the blockchain tables owned by the current user. This view does not display the SCHEMA_NAME column. Note: This view is available starting with Oracle Database release 19c, version 19.10. See Also: " DBA_BLOCKCHAIN_TABLES " " USER_BLOCKCHAIN_TABLES " Note: This view is available starting with Oracle Database release 19c, version 19.10. See Also: " DBA_BLOCKCHAIN_TABLES " " USER_BLOCKCHAIN_TABLES "