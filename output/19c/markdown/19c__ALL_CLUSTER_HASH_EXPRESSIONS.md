---
id: 19c__ALL_CLUSTER_HASH_EXPRESSIONS
name: ALL_CLUSTER_HASH_EXPRESSIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_CLUSTER_HASH_EXPRESSIONS.html
---

# ALL_CLUSTER_HASH_EXPRESSIONS

ALL_CLUSTER_HASH_EXPRESSIONS displays hash functions for all hash clusters accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the cluster |
| CLUSTER_NAME | VARCHAR2(128) | Name of the cluster |
| HASH_EXPRESSION | LONG | Text of the hash function of the hash cluster |

## Usage Notes

Related Views DBA_CLUSTER_HASH_EXPRESSIONS displays hash functions for all hash clusters in the database. USER_CLUSTER_HASH_EXPRESSIONS displays hash functions for all hash clusters owned by the current user. See Also: " DBA_CLUSTER_HASH_EXPRESSIONS " " USER_CLUSTER_HASH_EXPRESSIONS " See Also: " DBA_CLUSTER_HASH_EXPRESSIONS " " USER_CLUSTER_HASH_EXPRESSIONS "