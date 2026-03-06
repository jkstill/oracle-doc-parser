---
id: 19c__ALL_MINING_MODEL_PARTITIONS
name: ALL_MINING_MODEL_PARTITIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: partitioning
tags: [all]
source_file: ALL_MINING_MODEL_PARTITIONS.html
---

# ALL_MINING_MODEL_PARTITIONS

ALL_MINING_MODEL_PARTITIONS describes all the model partitions accessible to the user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Name of the model owner |
| MODEL_NAME | VARCHAR2(128) | Name of the model |
| PARTITION_NAME | VARCHAR2(128) | Name of the model partition |
| POSITION | NUMBER | Column position number for partitioning column. Column position represents the position of the column in a multi-column partitioning key, or 1 for a unary column partitioning key. |
| COLUMN_NAME | VARCHAR2(128) | Name of the column used for partitioning |
| COLUMN_VALUE | VARCHAR2(4000) | Value of the column for this partition |

## Usage Notes

Related Views DBA_MINING_MODEL_PARTITIONS describes all the model partitions accessible to the system. USER_MINING_MODEL_PARTITIONS describes the user's own model partitions. This view does not display the OWNER column.