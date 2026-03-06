---
id: 19c__ALL_CAPTURE_PREPARED_SCHEMAS
name: ALL_CAPTURE_PREPARED_SCHEMAS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_CAPTURE_PREPARED_SCHEMAS.html
---

# ALL_CAPTURE_PREPARED_SCHEMAS

ALL_CAPTURE_PREPARED_SCHEMAS displays information about the schemas prepared for instantiation that are accessible to the current user at the local database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SCHEMA_NAME | VARCHAR2(128) | Name of the schema that is ready to be instantiated |
| TIMESTAMP | DATE | Date and time at which the schema was ready to be instantiated |
| SUPPLEMENTAL_LOG_DATA_PK | VARCHAR2(8) | Status of schema-level PRIMARY KEY COLUMNS supplemental logging: IMPLICIT EXPLICIT NO |
| SUPPLEMENTAL_LOG_DATA_UI | VARCHAR2(8) | Status of schema-level UNIQUE INDEX COLUMNS supplemental logging: IMPLICIT EXPLICIT NO |
| SUPPLEMENTAL_LOG_DATA_FK | VARCHAR2(8) | Status of schema-level FOREIGN KEY COLUMNS supplemental logging: IMPLICIT EXPLICIT NO |
| SUPPLEMENTAL_LOG_DATA_ALL | VARCHAR2(8) | Status of schema-level ALL COLUMNS supplemental logging: IMPLICIT EXPLICIT NO |

## Usage Notes

Related View DBA_CAPTURE_PREPARED_SCHEMAS displays information about all schemas prepared for instantiation at the local database. See Also: " DBA_CAPTURE_PREPARED_SCHEMAS " See Also: " DBA_CAPTURE_PREPARED_SCHEMAS "