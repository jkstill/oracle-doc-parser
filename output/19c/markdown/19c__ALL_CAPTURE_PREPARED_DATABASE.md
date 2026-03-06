---
id: 19c__ALL_CAPTURE_PREPARED_DATABASE
name: ALL_CAPTURE_PREPARED_DATABASE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_CAPTURE_PREPARED_DATABASE.html
---

# ALL_CAPTURE_PREPARED_DATABASE

ALL_CAPTURE_PREPARED_DATABASE displays information about when the local database was prepared for instantiation. If the local database was not prepared for instantiation, then this view contains no rows.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TIMESTAMP | DATE | Date and time at which the local database was ready to be instantiated |
| SUPPLEMENTAL_LOG_DATA_PK | VARCHAR2(8) | Status of database-level PRIMARY KEY COLUMNS supplemental logging: IMPLICIT EXPLICIT NO |
| SUPPLEMENTAL_LOG_DATA_UI | VARCHAR2(8) | Status of database-level UNIQUE INDEX COLUMNS supplemental logging: IMPLICIT EXPLICIT NO |
| SUPPLEMENTAL_LOG_DATA_FK | VARCHAR2(8) | Status of database-level FOREIGN KEY COLUMNS supplemental logging: IMPLICIT EXPLICIT NO |
| SUPPLEMENTAL_LOG_DATA_ALL | VARCHAR2(8) | Status of database-level ALL COLUMNS supplemental logging: IMPLICIT EXPLICIT NO |

## Usage Notes

Related View DBA_CAPTURE_PREPARED_DATABASE displays information about when the local database was prepared for instantiation. See Also: " DBA_CAPTURE_PREPARED_DATABASE " See Also: " DBA_CAPTURE_PREPARED_DATABASE "