---
id: 19c__DBMS_DATA_MINING.RANK_APPLY
name: DBMS_DATA_MINING.RANK_APPLY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.RANK_APPLY

This procedure ranks the results of an APPLY operation based on a top-N specification for predictive and descriptive model results.

## Syntax

```sql
DBMS_DATA_MINING.RANK_APPLY (
      apply_result_table_name        IN VARCHAR2,
      case_id_column_name            IN VARCHAR2,
      score_column_name              IN VARCHAR2,
      score_criterion_column_name    IN VARCHAR2,
      ranked_apply_table_name        IN VARCHAR2,
      top_N                          IN NUMBER (38) DEFAULT 1,
      cost_matrix_table_name         IN VARCHAR2    DEFAULT NULL,
      apply_result_schema_name       IN VARCHAR2    DEFAULT NULL,
      cost_matrix_schema_name        IN VARCHAR2    DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| apply_result_table_name | VARCHAR2 | IN | Name of the table or view containing the results of an APPLY operation on the test data set (see Usage Notes) |
| case_id_column_name | VARCHAR2 | IN | Name of the case identifier column. This must be the same as the one used for generating APPLY results. |
| score_column_name | VARCHAR2 | IN | Name of the prediction column in the apply results table |
| score_criterion_column_name | VARCHAR2 | IN | Name of the probability column in the apply results table |
| ranked_apply_result_tab_name |  |  | Name of the table containing the ranked apply results |
| top_N | NUMBER | IN | Top N predictions to be considered from the APPLY results for precision recall computation |
| cost_matrix_table_name | VARCHAR2 | IN | Name of the cost matrix table |
| apply_result_schema_name | VARCHAR2 | IN | Name of the schema hosting the APPLY results table |
| cost_matrix_schema_name | VARCHAR2 | IN | Name of the schema hosting the cost matrix table |

## Usage Notes

For classification models, you can provide a cost matrix as input, and obtain the ranked results with costs applied to the predictions. Syntax DBMS_DATA_MINING.RANK_APPLY ( apply_result_table_name IN VARCHAR2, case_id_column_name IN VARCHAR2, score_column_name IN VARCHAR2, score_criterion_column_name IN VARCHAR2, ranked_apply_table_name IN VARCHAR2, top_N IN NUMBER (38) DEFAULT 1, cost_matrix_table_name IN VARCHAR2 DEFAULT NULL, apply_result_schema_name IN VARCHAR2 DEFAULT NULL, cost_matrix_schema_name IN VARCHAR2 DEFAULT NULL); Parameters Table 47-111 RANK_APPLY Procedure Parameters Parameter Description apply_result_table_name Name of the table or view containing the results of an APPLY operation on the test data set (see Usage Notes) case_id_column_name Name of the case identifier column. This must be the same as the one used for generating APPLY results. score_column_name Name of the prediction column in the apply results table score_criterion_column_name Name of the probability column in the apply results table ranked_apply_result_tab_name Name of the table containing the ranked apply results top_N Top N predictions to be considered from the APPLY results for precision recall computation cost_matrix_table_name Name of the cost matrix table apply_result_schema_name Name of the schema hosting the APPLY results table cost_matrix_schema_name Name of the schema hosting the cost matrix table Usage Notes You can use RANK_APPLY to generate ranked apply results, based on a top-N filter and also with application of cost for predictions, if the model was built with costs. The behavior of RANK_APPLY is similar to that of APPLY with respect to other DDL-like operations such as CREATE_MODEL , DROP_MODEL , and RENAME_MODEL . The procedure does not depend on the model; the only input of relevance is the apply results generated in a fixed schema table from APPLY . The main intended use of RANK_APPLY is for the generation of the final APPLY results against the scoring data in a production setting. You can apply the model against test data using APPLY , compute various test metrics against various cost matrix tables, and use the candidate cost matrix for RANK_APPLY . The schema for the apply results from each of the supported algorithms is listed in subsequent sections. The case_id column will be the same case identifier column as that of the apply results. Classification Models — NB and SVM For numerical targets, the ranked results table will have the definition as shown: ( case_id VARCHAR2/NUMBER, prediction NUMBER, probability NUMBER, cost NUMBER, rank INTEGER) For categorical targets, the ranked results table will have the following definition: ( case_id VARCHAR2/NUMBER, prediction VARCHAR2, probability NUMBER, cost NUMBER, rank INTEGER) Clustering Using k -Means or O-Cluster Clustering is an unsupervised mining function, and hence there are no targets. The results of an APPLY operation contains simply the cluster identifier corresponding to a case, and the associated probability. Cost matrix is not considered here. The ranked results table will have the definition as shown, and contains the cluster ids ranked by top-N . (case_id VARCHAR2/NUMBER, cluster_id NUMBER, probability NUMBER, rank INTEGER) Feature Extraction using NMF Feature extraction is also an unsupervised mining function, and hence there are no targets. The results of an APPLY operation contains simply the feature identifier corresponding to a case, and the associated match quality. Cost matrix is not considered here. The ranked results table will have the definition as shown, and contains the feature ids ranked by top-N . (case_id VARCHAR2/NUMBER, feature_id NUMBER, match_quality NUMBER, rank INTEGER) Examples BEGIN /* build a model with name census_model. * (See example under CREATE_MODEL) */ /* if training data was pre-processed in any manner, * perform the same pre-processing steps on apply * data also. * (See examples in the section on DBMS_DATA_MINING_TRANSFORM) */ /* apply the model to data to be scored */ DBMS_DATA_MINING.RANK_APPLY( apply_result_table_name => 'census_apply_result', case_id_column_name => 'person_id', score_column_name => 'prediction', score_criterion_column_name => 'probability ranked_apply_result_tab_name => 'census_ranked_apply_result', top_N => 3, cost_matrix_table_name => 'census_cost_matrix'); END; / -- View Ranked Apply Results SELECT * FROM census_ranked_apply_result;