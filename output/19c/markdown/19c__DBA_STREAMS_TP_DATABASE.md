---
id: 19c__DBA_STREAMS_TP_DATABASE
name: DBA_STREAMS_TP_DATABASE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_STREAMS_TP_DATABASE.html
---

# DBA_STREAMS_TP_DATABASE

DBA_STREAMS_TP_DATABASE displays information about each database that contains Replication components.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| GLOBAL_NAME | VARCHAR2(128) | Global name of the database |
| LAST_QUERIED | DATE | Time that the database was last queried |
| VERSION | VARCHAR2(128) | Database version of the database |
| COMPATIBILITY | VARCHAR2(128) | Compatible setting of the database |
| MANAGEMENT_PACK_ACCESS | VARCHAR2(128) | Management pack access of the database |