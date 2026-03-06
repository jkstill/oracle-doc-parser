---
id: 19c__ALL_INDEXTYPES
name: ALL_INDEXTYPES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: index
tags: [all]
source_file: ALL_INDEXTYPES.html
---

# ALL_INDEXTYPES

ALL_INDEXTYPES displays information about the indextypes accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the indextype |
| INDEXTYPE_NAME | VARCHAR2(128) | Name of the indextype |
| IMPLEMENTATION_SCHEMA | VARCHAR2(128) | Name of the schema for the indextype implementation (that is, containing the indextype operators) |
| IMPLEMENTATION_NAME | VARCHAR2(128) | Name of the indextype implementation type |
| INTERFACE_VERSION | NUMBER | Version of the indextype interface |
| IMPLEMENTATION_VERSION | NUMBER | Version of the indextype implementation |
| NUMBER_OF_OPERATORS | NUMBER | Number of operators associated with the indextype |
| PARTITIONING | VARCHAR2(10) | Kinds of local partitioning supported by the indextype: NONE - Indextype does not support local domain indexes RANGE - Indextype can support range partitioned local user managed domain indexes LOCAL - Indextype can support local system managed domain indexes (range, list, hash, or interval) |
| ARRAY_DML | VARCHAR2(3) | Indicates whether the indextype supports array DML ( YES ) or not ( NO ) |
| MAINTENANCE_TYPE | VARCHAR2(14) | Indicates whether the indextype is system-managed ( SYSTEM_MANAGED ) or user-managed ( USER_MANAGED ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_INDEXTYPES displays information about all indextypes in the database. USER_INDEXTYPES displays information about the indextypes owned by the current user. See Also: " DBA_INDEXTYPES " " USER_INDEXTYPES " See Also: " DBA_INDEXTYPES " " USER_INDEXTYPES "