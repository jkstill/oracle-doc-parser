---
id: 19c__DBA_LOGSTDBY_EDS_TABLES
name: DBA_LOGSTDBY_EDS_TABLES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [dba]
source_file: DBA_LOGSTDBY_EDS_TABLES.html
---

# DBA_LOGSTDBY_EDS_TABLES

DBA_LOGSTDBY_EDS_TABLES lists the tables that have EDS-based replication for Logical Standby.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Schema name of supportable table |
| TABLE_NAME | VARCHAR2(128) | Table name of supportable table |
| CTIME | TIMESTAMP(6) | Time that the table had EDS added |

## Usage Notes

In a CDB, the data displayed pertains to the container in which the view is queried.