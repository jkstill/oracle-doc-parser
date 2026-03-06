---
id: 19c__DBMS_DATA_MINING.GET_MODEL_DETAILS_NMF
name: DBMS_DATA_MINING.GET_MODEL_DETAILS_NMF
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.GET_MODEL_DETAILS_NMF

The GET_MODEL_DETAILS_NMF function returns a set of rows that provide the details of a Non-Negative Matrix Factorization model. Starting from Oracle Database 12 c Release 2, this function is deprecated. See "Model Detail Views" in Oracle Data Mining User’s Guide .

## Syntax

```sql
DBMS_DATA_MINING.get_model_details_nmf(
      model_name IN VARCHAR2,
      partition_name VARCHAR2 DEFAULT NULL)
   RETURN DM_NMF_Feature_Set PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| model_name | VARCHAR2 | IN | Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. |
| partition_name | VARCHAR2 | IN | Specifies a partition in a partitioned model |

**Returns:** `DM_NMF_Feature_Set`

## Usage Notes

Syntax DBMS_DATA_MINING.get_model_details_nmf( model_name IN VARCHAR2, partition_name VARCHAR2 DEFAULT NULL) RETURN DM_NMF_Feature_Set PIPELINED; Parameters Table 47-92 GET_MODEL_DETAILS_NMF Function Parameters Parameter Description model_name Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. partition_name Specifies a partition in a partitioned model Return Values Table 47-93 GET_MODEL_DETAILS_NMF Function Return Values Return Value Description DM_NMF_FEATURE_SET A set of rows of DM_NMF_FEATURE . The rows have the following columns: (feature_id NUMBER, mapped_feature_id VARCHAR2(4000), attribute_set DM_NMF_ATTRIBUTE_SET) The attribute_set column of DM_NMF_FEATURE returns a nested table of type DM_NMF_ATTRIBUTE_SET . The rows, of type DM_NMF_ATTRIBUTE , have the following columns: (attribute_name VARCHAR2(4000), attribute_subname VARCHAR2(4000), attribute_value VARCHAR2(4000), coefficient NUMBER) Usage Notes The table function pipes out rows of type DM_NMF_FEATURE_SET . For information on Data Mining datatypes and piped output from table functions, see " Datatypes " . When the value is NULL for a partitioned model, an exception is thrown. When the value is not null, it must contain the desired partition name. Examples The following example returns model details for the feature extraction model NMF_SH_Sample , which was created by the sample program dmnmdemo.sql . For information about the sample programs, see Oracle Data Mining User's Guide . SELECT * FROM ( SELECT F.feature_id, A.attribute_name, A.attribute_value, A.coefficient FROM TABLE(DBMS_DATA_MINING.GET_MODEL_DETAILS_NMF('NMF_SH_Sample')) F, TABLE(F.attribute_set) A ORDER BY feature_id,attribute_name,attribute_value ) WHERE ROWNUM < 11; FEATURE_ID ATTRIBUTE_NAME ATTRIBUTE_VALUE COEFFICIENT --------- ----------------------- ---------------- ------------------- 1 AFFINITY_CARD .051208078859308 1 AGE .0390513260041573 1 BOOKKEEPING_APPLICATION .0512734004239326 1 BULK_PACK_DISKETTES .232471260895683 1 COUNTRY_NAME Argentina .00766817464479959 1 COUNTRY_NAME Australia .000157637881096675 1 COUNTRY_NAME Brazil .0031409632415604 1 COUNTRY_NAME Canada .00144213099311427 1 COUNTRY_NAME China .000102279310968754 1 COUNTRY_NAME Denmark .000242424084307513