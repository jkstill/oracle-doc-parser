---
id: 19c__V$DG_BROKER_CONFIG
name: V$DG_BROKER_CONFIG
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-DG_BROKER_CONFIG.html
---

# V$DG_BROKER_CONFIG

V$DG_BROKER_CONFIG provides a summary of an Oracle Data Guard broker configuration.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DATABASE | VARCHAR2(512) |  |
| CONNECT_IDENTIFIER | VARCHAR2(512) |  |
| DATAGUARD_ROLE | VARCHAR2(27) |  |
| REDO_SOURCE | VARCHAR(30) |  |
| ENABLED | VARCHAR2(5) |  |
| STATUS | NUMBER |  |
| VERSION | VARCHAR2(30) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This is similar to the DGMGRL CLI's SHOW CONFIGURATION command. It provides a view of the entire Oracle Data Guard broker configuration from any database in the configuration.