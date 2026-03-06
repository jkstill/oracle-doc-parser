---
id: 19c__ALL_STREAMS_NEWLY_SUPPORTED
name: ALL_STREAMS_NEWLY_SUPPORTED
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_STREAMS_NEWLY_SUPPORTED.html
---

# ALL_STREAMS_NEWLY_SUPPORTED

ALL_STREAMS_NEWLY_SUPPORTED displays information about the tables accessible to the current user that are newly supported by capture processes.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the table |
| TABLE_NAME | VARCHAR2(128) | Name of the table |
| REASON | VARCHAR2(39) | Reason why the table was not supported in a previous release: IOT column with user-defined type unsupported column exists object table AQ queue table temporary table sub object external table materialized view FILE column exists materialized view log materialized view container table streams unsupported object domain index |
| COMPATIBLE | CHAR(4) | Minimum database compatibility for capture processes to support the database object |

## Usage Notes

Related View DBA_STREAMS_NEWLY_SUPPORTED displays information about all tables in the database that are newly supported by capture processes. See Also: " DBA_STREAMS_NEWLY_SUPPORTED " See Also: " DBA_STREAMS_NEWLY_SUPPORTED "