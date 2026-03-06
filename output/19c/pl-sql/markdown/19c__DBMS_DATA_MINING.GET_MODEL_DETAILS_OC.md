---
id: 19c__DBMS_DATA_MINING.GET_MODEL_DETAILS_OC
name: DBMS_DATA_MINING.GET_MODEL_DETAILS_OC
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.GET_MODEL_DETAILS_OC

The GET_MODEL_DETAILS_OC function returns a set of rows that provide the details of an O-Cluster clustering model. The rows are an enumeration of the Clustering patterns generated during the creation of the model. Starting from Oracle Database 12 c Release 2, this function is deprecated. See "Model Detail Views" in Oracle Data Mining User’s Guide .

## Syntax

```sql
DBMS_DATA_MINING.get_model_details_oc(
      model_name VARCHAR2,
      cluster_id NUMBER   DEFAULT NULL,
      attribute  VARCHAR2 DEFAULT NULL,
      centroid   NUMBER   DEFAULT 1,
      histogram  NUMBER   DEFAULT 1,
      rules      NUMBER   DEFAULT 2,
      topn_attributes NUMBER DEFAULT NULL,
      partition_name VARCHAR2 DEFAULT NULL)
  RETURN dm_clusters PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| model_name | VARCHAR2 | IN | Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. |
| cluster_id | NUMBER | IN | The ID of a cluster in the model. When a valid cluster ID is specified, only the details of this cluster are returned. Otherwise the details for all clusters are returned. |
| attribute | VARCHAR2 | IN | The name of an attribute. When a valid attribute name is specified, only the details of this attribute are returned. Otherwise, the details for all attributes are returned |
| centroid | NUMBER | IN | This parameter accepts the following values: 1: Details about centroids are returned (default) 0: Details about centroids are not returned |
| histogram | NUMBER | IN | This parameter accepts the following values: 1: Details about histograms are returned (default) 0: Details about histograms are not returned |
| rules | NUMBER | IN | This parameter accepts the following values: 2: Details about rules are returned (default) 1: Rule summaries are returned 0: No information about rules is returned |
| topn_attributes | NUMBER | IN | Restricts the number of attributes returned in the centroid, histogram, and rules objects. Only the n attributes with the highest confidence values in the rules are returned. If the number of attributes included in the rules is less than topn , then up to n additional attributes in alphabetical order are returned. If both the attribute and topn_attributes parameters are specified, then topn_attributes is ignored. |
| partition_name | VARCHAR2 | IN | Specifies a partition in a partitioned model. |

**Returns:** `dm_clusters`

## Usage Notes

You can provide input to GET_MODEL_DETAILS_OC to request specific information about the model, thus improving the performance of the query. If you do not specify filtering parameters, then GET_MODEL_DETAILS_OC returns all the information about the model. Syntax DBMS_DATA_MINING.get_model_details_oc( model_name VARCHAR2, cluster_id NUMBER DEFAULT NULL, attribute VARCHAR2 DEFAULT NULL, centroid NUMBER DEFAULT 1, histogram NUMBER DEFAULT 1, rules NUMBER DEFAULT 2, topn_attributes NUMBER DEFAULT NULL, partition_name VARCHAR2 DEFAULT NULL) RETURN dm_clusters PIPELINED; Parameters Table 47-94 GET_MODEL_DETAILS_OC Function Parameters Parameter Description model_name Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. cluster_id The ID of a cluster in the model. When a valid cluster ID is specified, only the details of this cluster are returned. Otherwise the details for all clusters are returned. attribute The name of an attribute. When a valid attribute name is specified, only the details of this attribute are returned. Otherwise, the details for all attributes are returned centroid This parameter accepts the following values: 1: Details about centroids are returned (default) 0: Details about centroids are not returned histogram This parameter accepts the following values: 1: Details about histograms are returned (default) 0: Details about histograms are not returned rules This parameter accepts the following values: 2: Details about rules are returned (default) 1: Rule summaries are returned 0: No information about rules is returned topn_attributes Restricts the number of attributes returned in the centroid, histogram, and rules objects. Only the n attributes with the highest confidence values in the rules are returned. If the number of attributes included in the rules is less than topn , then up to n additional attributes in alphabetical order are returned. If both the attribute and topn_attributes parameters are specified, then topn_attributes is ignored. partition_name Specifies a partition in a partitioned model. Usage Notes For information about Data Mining datatypes and Return Values for Clustering Algorithms piped output from table functions, see " Datatypes " . When the value is NULL for a partitioned model, an exception is thrown. When the value is not null, it must contain the desired partition name. Examples The following example returns model details for the clustering model OC_SH_Clus_sample , which was created by the sample program dmocdemo.sql . For information about the sample programs, see Oracle Data Mining User's Guide . For each cluster in this example, the split predicate indicates the attribute and the condition used to assign records to the cluster's children during model build. It provides an important piece of information on how the population within a cluster can be divided up into two smaller clusters. SELECT clu_id, attribute_name, op, s_value FROM (SELECT a.id clu_id, sp.attribute_name, sp.conditional_operator op, sp.attribute_str_value s_value FROM TABLE(DBMS_DATA_MINING.GET_MODEL_DETAILS_OC( 'OC_SH_Clus_sample')) a, TABLE(a.split_predicate) sp ORDER BY a.id, op, s_value) WHERE ROWNUM < 11; CLU_ID ATTRIBUTE_NAME OP S_VALUE ----------- -------------------- --------------------------------- 1 OCCUPATION IN ? 1 OCCUPATION IN Armed-F 1 OCCUPATION IN Cleric. 1 OCCUPATION IN Crafts 2 OCCUPATION IN ? 2 OCCUPATION IN Armed-F 2 OCCUPATION IN Cleric. 3 OCCUPATION IN Exec. 3 OCCUPATION IN Farming 3 OCCUPATION IN Handler