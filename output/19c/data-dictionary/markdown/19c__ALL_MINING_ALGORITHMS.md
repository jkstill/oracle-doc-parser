---
id: 19c__ALL_MINING_ALGORITHMS
name: ALL_MINING_ALGORITHMS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_MINING_ALGORITHMS.html
---

# ALL_MINING_ALGORITHMS

ALL_MINING_ALGORITHMS describes the settings for a current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ALGORITHM_NAME | VARCHAR2(128) | Algorithm used by the model. |
| MINING_FUNCTION | VARCHAR2(30) | Function of the mining model. The mining function is specified when the model is built: CLASSIFICATION REGRESSION CLUSTERING FEATURE_EXTRACTION ASSOCIATION_RULES ATTRIBUTE_IMPORTANCE ANOMALY DETECTION |
| ALGORITHM_TYPE | VARCHAR2(20) | Algorithm type of the model |
| ALGORITHM_METADATA | CLOB | Metadata of the algorithm |
| DESCRIPTION | VARCHAR2(4000) | Description of the algorithm |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content