---
id: 19c__DBA_MINING_MODEL_TABLES
name: DBA_MINING_MODEL_TABLES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [dba]
source_file: DBA_MINING_MODEL_TABLES.html
---

# DBA_MINING_MODEL_TABLES

DBA_MINING_MODEL_TABLES describes the tables that contain metadata about the mining models in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the mining model |
| MODEL_NAME | VARCHAR2(128) | Name of the mining model |
| TABLE_NAME | VARCHAR2(128) | Name of the table |
| TABLE_TYPE | VARCHAR2(21) | The type of metadata stored in the table |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Mining models are schema objects created by Oracle Data Mining. Model tables reside in the schema of the mining model owner. The metadata stored in the tables is controlled by Oracle Data Mining APIs. The tables are read-only. They should not be modified by users.