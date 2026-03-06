---
id: 19c__ALL_MINING_MODELS
name: ALL_MINING_MODELS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_MINING_MODELS.html
---

# ALL_MINING_MODELS

ALL_MINING_MODELS describes the mining models accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the mining model |
| MODEL_NAME | VARCHAR2(128) | Name of the mining model |
| MINING_FUNCTION | VARCHAR2(30) | Function of the mining model. The function identifies the class of problems that can be solved by this model. The mining function is specified when the model is built: CLASSIFICATION REGRESSION CLUSTERING FEATURE_EXTRACTION ASSOCIATION_RULES ATTRIBUTE_IMPORTANCE |
| ALGORITHM | VARCHAR2(30) | Algorithm used by the model. Each mining function has a default algorithm. The default can be overridden with a model setting (see *_MINING_MODEL_SETTINGS ): CUR_DECOMPOSITION NAIVE_BAYES DECISION_TREE EXPLICIT_SEMANTIC_ANALYS EXPONENTIAL_ SMOOTHING SUPPORT_VECTOR_MACHINES KMEANS O_CLUSTER NONNEGATIVE_MATRIX_FACTOR NEURAL_NETWORK GENERALIZED_LINEAR_MODEL APRIORI_ASSOCIATION_RULES MINIMUM_DESCRIPTION_LENGTH EXPECTATION_MAXIMIZATION RANDOM_FOREST SINGULAR_VALUE_DECOMP R_EXTENSIBLE |
| ALGORITHM_TYPE | VARCHAR2(10) | Algorithm type of the model |
| CREATION_DATE | DATE | Date that the model was created |
| BUILD_DURATION | NUMBER | Time (in seconds) of the model build process |
| MODEL_SIZE | NUMBER | Size of the model (in megabytes) |
| PARTITIONED | VARCHAR2(3) | Indicates whether the model is partitioned or not. Possible values: YES : The model is partitioned. NO : The model is not partitioned |
| COMMENTS | VARCHAR2(4000) | Comment applied to the model with a SQL COMMENT statement |

## Usage Notes

Mining models are schema objects created by Oracle Data Mining. Related Views DBA_MINING_MODELS describes all mining models in the database. USER_MINING_MODELS describes the mining models owned by the current user. This view does not display the OWNER column. See Also: Oracle Data Mining User’s Guide for information about mining model schema objects Oracle Data Mining Concepts for an introduction to Data Mining See Also: Oracle Data Mining User’s Guide for information about mining model schema objects Oracle Data Mining Concepts for an introduction to Data Mining