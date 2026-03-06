---
id: 19c__V$VPD_POLICY
name: V$VPD_POLICY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-VPD_POLICY.html
---

# V$VPD_POLICY

V$VPD_POLICY displays all the fine-grained security policies and predicates associated with the cursors currently in the library cache.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ADDRESS | RAW(4 | 8) |  |
| PARADDR | RAW(4 | 8) |  |
| SQL_HASH | NUMBER |  |
| SQL_ID | VARCHAR2(13) |  |
| CHILD_NUMBER | NUMBER |  |
| OBJECT_OWNER | VARCHAR2(128) |  |
| OBJECT_NAME | VARCHAR2(128) |  |
| POLICY_GROUP | VARCHAR2(128) |  |
| POLICY | VARCHAR2(128) |  |
| POLICY_FUNCTION_OWNER | VARCHAR2(128) |  |
| PREDICATE | VARCHAR2(4000) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content