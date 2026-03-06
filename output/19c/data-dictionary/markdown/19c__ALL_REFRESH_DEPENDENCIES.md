---
id: 19c__ALL_REFRESH_DEPENDENCIES
name: ALL_REFRESH_DEPENDENCIES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_REFRESH_DEPENDENCIES.html
---

# ALL_REFRESH_DEPENDENCIES

ALL_REFRESH_DEPENDENCIES displays the names of the dependent detail or container tables of all the materialized views in the current schema.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the table |
| TABLE_NAME | VARCHAR2(128) | Table name, unique within this schema |
| PARENT_OBJECT_TYPE | CHAR(17) | MATERIALIZED VIEW |
| OLDEST_REFRESH_SCN | NUMBER | Minimum SCN of any summary or materialized view that has TABLE_NAME as a detail table |
| OLDEST_REFRESH_DATE | DATE | SYSDATE when last refreshed |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content