---
id: 19c__DBMS_DATA_MINING.GET_MODEL_DETAILS_KM
name: DBMS_DATA_MINING.GET_MODEL_DETAILS_KM
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.GET_MODEL_DETAILS_KM

The GET_MODEL_DETAILS_KM function returns a set of rows that provide the details of a k -Means clustering model. Starting from Oracle Database 12 c Release 2, this function is deprecated. See "Model Detail Views" in Oracle Data Mining User’s Guide .

## Syntax

```sql
DBMS_DATA_MINING.get_model_details_km(
      model_name VARCHAR2,
      cluster_id NUMBER   DEFAULT NULL,
      attribute  VARCHAR2 DEFAULT NULL,
      centroid   NUMBER   DEFAULT 1,
      histogram  NUMBER   DEFAULT 1,
      rules      NUMBER   DEFAULT 2,
      attribute_subname  VARCHAR2 DEFAULT NULL,
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
| attribute_subname | VARCHAR2 | IN | The name of a nested attribute. The full name of a nested attribute has the form: attribute_name.attribute_subname where attribute_name is the name of the column and attribute_subname is the name of the nested attribute in that column. If the attribute is not nested, attribute_subname is null. |
| topn_attributes | NUMBER | IN | Restricts the number of attributes returned in the centroid, histogram, and rules objects. Only the n attributes with the highest confidence values in the rules are returned. If the number of attributes included in the rules is less than topn , then up to n additional attributes in alphabetical order are returned. If both the attribute and topn_attributes parameters are specified, then topn_attributes is ignored. |
| partition_name | VARCHAR2 | IN | Specifies a partition in a partitioned model. |

**Returns:** `dm_clusters`

## Usage Notes

You can provide input to GET_MODEL_DETAILS_KM to request specific information about the model, thus improving the performance of the query. If you do not specify filtering parameters, then GET_MODEL_DETAILS_KM returns all the information about the model. Syntax DBMS_DATA_MINING.get_model_details_km( model_name VARCHAR2, cluster_id NUMBER DEFAULT NULL, attribute VARCHAR2 DEFAULT NULL, centroid NUMBER DEFAULT 1, histogram NUMBER DEFAULT 1, rules NUMBER DEFAULT 2, attribute_subname VARCHAR2 DEFAULT NULL, topn_attributes NUMBER DEFAULT NULL, partition_name VARCHAR2 DEFAULT NULL) RETURN dm_clusters PIPELINED; Parameters Table 47-89 GET_MODEL_DETAILS_KM Function Parameters Parameter Description model_name Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. cluster_id The ID of a cluster in the model. When a valid cluster ID is specified, only the details of this cluster are returned. Otherwise the details for all clusters are returned. attribute The name of an attribute. When a valid attribute name is specified, only the details of this attribute are returned. Otherwise, the details for all attributes are returned centroid This parameter accepts the following values: 1: Details about centroids are returned (default) 0: Details about centroids are not returned histogram This parameter accepts the following values: 1: Details about histograms are returned (default) 0: Details about histograms are not returned rules This parameter accepts the following values: 2: Details about rules are returned (default) 1: Rule summaries are returned 0: No information about rules is returned attribute_subname The name of a nested attribute. The full name of a nested attribute has the form: attribute_name.attribute_subname where attribute_name is the name of the column and attribute_subname is the name of the nested attribute in that column. If the attribute is not nested, attribute_subname is null. topn_attributes Restricts the number of attributes returned in the centroid, histogram, and rules objects. Only the n attributes with the highest confidence values in the rules are returned. If the number of attributes included in the rules is less than topn , then up to n additional attributes in alphabetical order are returned. If both the attribute and topn_attributes parameters are specified, then topn_attributes is ignored. partition_name Specifies a partition in a partitioned model. Usage Notes The table function pipes out rows of type DM_CLUSTERS . For information on Data Mining datatypes and Return Value for Clustering Algorithms piped output from table functions, see " Datatypes " . When the value is NULL for a partitioned model, an exception is thrown. When the value is not null, it must contain the desired partition name. Examples The following example returns model details for the k -Means clustering model KM_SH_Clus_sample , which was created by the sample program dmkmdemo.sql . For information about the sample programs, see Oracle Data Mining User's Guide . SELECT T.id clu_id, T.record_count rec_cnt, T.parent parent, T.tree_level tree_level, T.dispersion dispersion FROM (SELECT * FROM TABLE(DBMS_DATA_MINING.GET_MODEL_DETAILS_KM( 'KM_SH_Clus_sample')) ORDER BY id) T WHERE ROWNUM < 6; CLU_ID REC_CNT PARENT TREE_LEVEL DISPERSION ---------- ---------- ---------- ---------- ---------- 1 1500 1 5.9152211 2 638 1 2 3.98458982 3 862 1 2 5.83732097 4 376 3 3 5.05192137 5 486 3 3 5.42901522