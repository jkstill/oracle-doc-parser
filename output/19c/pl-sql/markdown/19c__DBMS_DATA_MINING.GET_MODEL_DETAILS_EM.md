---
id: 19c__DBMS_DATA_MINING.GET_MODEL_DETAILS_EM
name: DBMS_DATA_MINING.GET_MODEL_DETAILS_EM
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.GET_MODEL_DETAILS_EM

The GET_MODEL_DETAILS_EM function returns a set of rows that provide statistics about the clusters produced by an Expectation Maximization model. Starting from Oracle Database 12 c Release 2, this function is deprecated. See "Model Detail Views" in Oracle Data Mining User’s Guide .

## Syntax

```sql
DBMS_DATA_MINING.get_model_details_em(
      model_name VARCHAR2,
      cluster_id NUMBER   DEFAULT NULL,
      attribute  VARCHAR2 DEFAULT NULL,
      centroid   NUMBER   DEFAULT 1,
      histogram  NUMBER   DEFAULT 1,
      rules      NUMBER   DEFAULT 2,
      attribute_subname  VARCHAR2 DEFAULT NULL,
      topn_attributes NUMBER DEFAULT NULL,
      partition_name IN VARCHAR2 DEFAULT NULL)
  RETURN dm_clusters PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| model_name | VARCHAR2 | IN | Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. |
| cluster_id | NUMBER | IN | The ID of a cluster in the model. When a valid cluster ID is specified, only the details of this cluster are returned. Otherwise, the details for all clusters are returned. |
| attribute | VARCHAR2 | IN | The name of an attribute. When a valid attribute name is specified, only the details of this attribute are returned. Otherwise, the details for all attributes are returned |
| centroid | NUMBER | IN | This parameter accepts the following values: 1: Details about centroids are returned (default) 0: Details about centroids are not returned |
| histogram | NUMBER | IN | This parameter accepts the following values: 1: Details about histograms are returned (default) 0: Details about histograms are not returned |
| rules | NUMBER | IN | This parameter accepts the following values: 2: Details about rules are returned (default) 1: Rule summaries are returned 0: No information about rules is returned |
| attribute_subname | VARCHAR2 | IN | The name of a nested attribute. The full name of a nested attribute has the form: attribute_name.attribute_subname where attribute_name is the name of the column and attribute_subname is the name of the nested attribute in that column. If the attribute is not nested, then attribute_subname is null. |
| topn_attributes | NUMBER | IN | Restricts the number of attributes returned in the centroid, histogram, and rules objects. Only the n attributes with the highest confidence values in the rules are returned. If the number of attributes included in the rules is less than topn , then, up to n additional attributes in alphabetical order are returned. If both the attribute and topn_attributes parameters are specified, then topn_attributes is ignored. |
| partition_name | VARCHAR2 | IN | Specifies a partition in a partitioned model. |

**Returns:** `dm_clusters`

## Usage Notes

By default, the EM algorithm groups components into high-level clusters, and GET_MODEL_DETAILS_EM returns only the high-level clusters with their hierarchies. Alternatively, you can configure EM model to disable the grouping of components into high-level clusters. In this case, GET_MODEL_DETAILS_EM returns the components themselves as clusters with their hierarchies. See Table 47-12 . Syntax DBMS_DATA_MINING.get_model_details_em( model_name VARCHAR2, cluster_id NUMBER DEFAULT NULL, attribute VARCHAR2 DEFAULT NULL, centroid NUMBER DEFAULT 1, histogram NUMBER DEFAULT 1, rules NUMBER DEFAULT 2, attribute_subname VARCHAR2 DEFAULT NULL, topn_attributes NUMBER DEFAULT NULL, partition_name IN VARCHAR2 DEFAULT NULL) RETURN dm_clusters PIPELINED; Parameters Table 47-79 GET_MODEL_DETAILS_EM Function Parameters Parameter Description model_name Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. cluster_id The ID of a cluster in the model. When a valid cluster ID is specified, only the details of this cluster are returned. Otherwise, the details for all clusters are returned. attribute The name of an attribute. When a valid attribute name is specified, only the details of this attribute are returned. Otherwise, the details for all attributes are returned centroid This parameter accepts the following values: 1: Details about centroids are returned (default) 0: Details about centroids are not returned histogram This parameter accepts the following values: 1: Details about histograms are returned (default) 0: Details about histograms are not returned rules This parameter accepts the following values: 2: Details about rules are returned (default) 1: Rule summaries are returned 0: No information about rules is returned attribute_subname The name of a nested attribute. The full name of a nested attribute has the form: attribute_name.attribute_subname where attribute_name is the name of the column and attribute_subname is the name of the nested attribute in that column. If the attribute is not nested, then attribute_subname is null. topn_attributes Restricts the number of attributes returned in the centroid, histogram, and rules objects. Only the n attributes with the highest confidence values in the rules are returned. If the number of attributes included in the rules is less than topn , then, up to n additional attributes in alphabetical order are returned. If both the attribute and topn_attributes parameters are specified, then topn_attributes is ignored. partition_name Specifies a partition in a partitioned model. Usage Notes For information on Data Mining datatypes and Return Values for Clustering Algorithms piped output from table functions, see " Datatypes " . GET_MODEL_DETAILS functions preserve model transparency by automatically reversing the transformations applied during the build process. Thus the attributes returned in the model details are the original attributes (or a close approximation of the original attributes) used to build the model. When cluster statistics are disabled ( EMCS_CLUSTER_STATISTICS is set to EMCS_CLUS_STATS_DISABLE ), GET_MODEL_DETAILS_EM does not return centroids, histograms, or rules. Only taxonomy (hierarchy) and cluster counts are returned. When the partition_name is NULL for a partitioned model, an exception is thrown. When the value is not null, it must contain the desired partition name.