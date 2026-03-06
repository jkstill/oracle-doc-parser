---
id: 19c__ALL_CAPTURE_PREPARED_TABLES
name: ALL_CAPTURE_PREPARED_TABLES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_CAPTURE_PREPARED_TABLES.html
---

# ALL_CAPTURE_PREPARED_TABLES

ALL_CAPTURE_PREPARED_TABLES displays information about the tables prepared for instantiation that are accessible to the current user at the local database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TABLE_OWNER | VARCHAR2(128) | Owner of the table that is ready to be instantiated |
| TABLE_NAME | VARCHAR2(128) | Name of the table that is ready to be instantiated |
| SCN | NUMBER | Smallest system change number (SCN) for which the table can be instantiated |
| TIMESTAMP | DATE | Date and time at which the table was ready to be instantiated |
| SUPPLEMENTAL_LOG_DATA_PK | VARCHAR2(8) | Status of table-level PRIMARY KEY COLUMNS supplemental logging: IMPLICIT EXPLICIT NO |
| SUPPLEMENTAL_LOG_DATA_UI | VARCHAR2(8) | Status of table-level UNIQUE INDEX COLUMNS supplemental logging: IMPLICIT EXPLICIT NO |
| SUPPLEMENTAL_LOG_DATA_FK | VARCHAR2(8) | Status of table-level FOREIGN KEY COLUMNS supplemental logging: IMPLICIT EXPLICIT NO |
| SUPPLEMENTAL_LOG_DATA_ALL | VARCHAR2(8) | Status of table-level ALL COLUMNS supplemental logging: IMPLICIT EXPLICIT NO |

## Usage Notes

Related View DBA_CAPTURE_PREPARED_TABLES displays information about all tables prepared for instantiation at the local database. See Also: " DBA_CAPTURE_PREPARED_TABLES " See Also: " DBA_CAPTURE_PREPARED_TABLES "