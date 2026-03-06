---
id: 19c__DBA_REGISTRY_SCHEMAS
name: DBA_REGISTRY_SCHEMAS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_REGISTRY_SCHEMAS.html
---

# DBA_REGISTRY_SCHEMAS

DBA_REGISTRY_SCHEMAS lists the primary and ancillary schemas included in the component registry. The ancillary schemas that are listed in this view are the same schemas that would be included in the OTHER_SCHEMAS column of the DBA_REGISTRY view.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAMESPACE | VARCHAR2(30) | Component namespace |
| COMP_ID | VARCHAR2(30) | Component identifier |
| SCHEMA | VARCHAR2(128) | User that contains the objects for the component |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: " DBA_REGISTRY " " USER_REGISTRY " See Also: " DBA_REGISTRY " " USER_REGISTRY "