---
id: 19c__ALL_REWRITE_EQUIVALENCES
name: ALL_REWRITE_EQUIVALENCES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_REWRITE_EQUIVALENCES.html
---

# ALL_REWRITE_EQUIVALENCES

ALL_REWRITE_EQUIVALENCES describes the rewrite equivalences accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the rewrite equivalence |
| NAME | VARCHAR2(128) | Name of the rewrite equivalence |
| SOURCE_STMT | CLOB | Source statement of the rewrite equivalence |
| DESTINATION_STMT | CLOB | Destination of the rewrite equivalence |
| REWRITE_MODE | VARCHAR2(10) | Rewrite mode of the rewrite equivalence: DISABLED TEXT_MATCH GENERAL RECURSIVE |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_REWRITE_EQUIVALENCES describes all rewrite equivalences in the database. USER_REWRITE_EQUIVALENCES describes the rewrite equivalences owned by the current user. See Also: " DBA_REWRITE_EQUIVALENCES " " USER_REWRITE_EQUIVALENCES " See Also: " DBA_REWRITE_EQUIVALENCES " " USER_REWRITE_EQUIVALENCES "