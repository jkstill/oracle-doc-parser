---
id: 19c__DBA_REGISTRY_LOG
name: DBA_REGISTRY_LOG
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dba]
source_file: DBA_REGISTRY_LOG.html
---

# DBA_REGISTRY_LOG

DBA_REGISTRY_LOG displays operating information about components loaded into the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OPTIME | VARCHAR2(20) | Operation time |
| NAMESPACE | VARCHAR2(30) | Component namespace |
| COMP_ID | VARCHAR2(30) | Component identifier |
| OPERATION | VARCHAR2(11) | Operation name |
| MESSAGE | VARCHAR2(1000) | Message |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content