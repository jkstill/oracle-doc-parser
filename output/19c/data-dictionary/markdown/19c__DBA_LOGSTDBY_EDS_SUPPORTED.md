---
id: 19c__DBA_LOGSTDBY_EDS_SUPPORTED
name: DBA_LOGSTDBY_EDS_SUPPORTED
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dba]
source_file: DBA_LOGSTDBY_EDS_SUPPORTED.html
---

# DBA_LOGSTDBY_EDS_SUPPORTED

DBA_LOGSTDBY_EDS_SUPPORTED lists the tables that are candidates for EDS-based replication for Logical Standby based on the data types they contain.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Table owner |
| TABLE_NAME | VARCHAR2(128) | Table name |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content In a CDB, the data displayed pertains to the container in which the view is queried.