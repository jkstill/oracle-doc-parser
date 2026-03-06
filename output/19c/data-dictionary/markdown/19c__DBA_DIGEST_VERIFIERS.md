---
id: 19c__DBA_DIGEST_VERIFIERS
name: DBA_DIGEST_VERIFIERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_DIGEST_VERIFIERS.html
---

# DBA_DIGEST_VERIFIERS

DBA_DIGEST_VERIFIERS enables the database administrator to check which users have Digest verifiers stored on disk and the type of hashing algorithm used for the verifiers.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| USERNAME | VARCHAR2(128) | Name of the user |
| HAS_DIGEST_VERIFIERS | VARCHAR2(3) | YES if a Digest verifier exists, NO otherwise |
| DIGEST_TYPE | CHAR(3) | The type of hashing algorithm used for the Digest verifier. For instance, MD5 for users with MD5 Digest verifiers. If no Digest verifier exists, this column is NULL . |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content