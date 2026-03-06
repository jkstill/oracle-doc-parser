---
id: 19c__DBA_LOGSTDBY_UNSUPPORTED_TABLE
name: DBA_LOGSTDBY_UNSUPPORTED_TABLE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [dba]
source_file: DBA_LOGSTDBY_UNSUPPORTED_TABLE.html
---

# DBA_LOGSTDBY_UNSUPPORTED_TABLE

DBA_LOGSTDBY_UNSUPPORTED_TABLE displays the data tables that are not supported by Logical Standby.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the unsupported table |
| TABLE_NAME | VARCHAR2(128) | Name of the unsupported table |

## Usage Notes

The data displayed pertains to the container in which the view is queried. This view is for logical standby databases only.