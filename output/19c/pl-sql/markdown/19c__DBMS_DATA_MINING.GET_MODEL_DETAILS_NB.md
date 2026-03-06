---
id: 19c__DBMS_DATA_MINING.GET_MODEL_DETAILS_NB
name: DBMS_DATA_MINING.GET_MODEL_DETAILS_NB
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.GET_MODEL_DETAILS_NB

The GET_MODEL_DETAILS_NB function returns a set of rows that provide the details of a Naive Bayes model. Starting from Oracle Database 12 c Release 2, this function is deprecated. See "Model Detail Views" in Oracle Data Mining User’s Guide .

## Syntax

```sql
DBMS_DATA_MINING.get_model_details_nb(
      model_name IN VARCHAR2,
      partition_name IN VARCHAR2 DEFAULT NULL)
  RETURN DM_NB_Details PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| model_name | VARCHAR2 | IN | Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. |
| partition_name | VARCHAR2 | IN | Specifies a partition in a partitioned model |

**Returns:** `DM_NB_Details`

## Usage Notes

Syntax DBMS_DATA_MINING.get_model_details_nb( model_name IN VARCHAR2, partition_name IN VARCHAR2 DEFAULT NULL) RETURN DM_NB_Details PIPELINED; Parameters Table 47-90 GET_MODEL_DETAILS_NB Function Parameters Parameter Description model_name Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. partition_name Specifies a partition in a partitioned model Return Values Table 47-91 GET_MODEL_DETAILS_NB Function Return Values Return Value Description DM_NB_DETAILS A set of rows of type DM_NB_DETAIL . The rows have the following columns: (target_attribute_name VARCHAR2(30), target_attribute_str_value VARCHAR2(4000), target_attribute_num_value NUMBER, prior_probability NUMBER, conditionals DM_CONDITIONALS) The conditionals column of DM_NB_DETAIL returns a nested table of type DM_CONDITIONALS . The rows, of type DM_CONDITIONAL , have the following columns: (attribute_name VARCHAR2(4000), attribute_subname VARCHAR2(4000), attribute_str_value VARCHAR2(4000), attribute_num_value NUMBER, conditional_probability NUMBER) Usage Notes The table function pipes out rows of type DM_NB_DETAILS . For information on Data Mining datatypes and piped output from table functions, see " Datatypes " . When the value is NULL for a partitioned model, an exception is thrown. When the value is not null, it must contain the desired partition name. Examples The following query is from the sample program dmnbdemo.sql . It returns model details about the model NB_SH_Clas_sample . For information about the sample programs, see Oracle Data Mining User's Guide . The query creates labels from the bin boundary tables that were used to bin the training data. It replaces the attribute values with the labels. For numeric bins, the labels are ( lower_boundary , upper_boundary ] ; for categorical bins, the label matches the value it represents. (This method of categorical label representation will only work for cases where one value corresponds to one bin.) The target was not binned. WITH bin_label_view AS ( SELECT col, bin, (DECODE(bin,'1','[','(') || lv || ',' || val || ']') label FROM (SELECT col, bin, LAST_VALUE(val) OVER ( PARTITION BY col ORDER BY val ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING) lv, val FROM nb_sh_sample_num) UNION ALL SELECT col, bin, val label FROM nb_sh_sample_cat ), model_details AS ( SELECT T.target_attribute_name tname, NVL(TO_CHAR(T.target_attribute_num_value,T.target_attribute_str_value)) tval, C.attribute_name pname, NVL(L.label, NVL(C.attribute_str_value, C.attribute_num_value)) pval, T.prior_probability priorp, C.conditional_probability condp FROM TABLE(DBMS_DATA_MINING.GET_MODEL_DETAILS_NB('NB_SH_Clas_sample')) T, TABLE(T.conditionals) C, bin_label_view L WHERE C.attribute_name = L.col (+) AND (NVL(C.attribute_str_value,C.attribute_num_value) = L.bin(+)) ORDER BY 1,2,3,4,5,6 ) SELECT tname, tval, pname, pval, priorp, condp FROM model_details WHERE ROWNUM < 11; TNAME TVAL PNAME PVAL PRIORP CONDP -------------- ---- ------------------------- ------------- ------- ------- AFFINITY_CARD 0 AGE (24,30] .6500 .1714 AFFINITY_CARD 0 AGE (30,35] .6500 .1509 AFFINITY_CARD 0 AGE (35,40] .6500 .1125 AFFINITY_CARD 0 AGE (40,46] .6500 .1134 AFFINITY_CARD 0 AGE (46,53] .6500 .1071 AFFINITY_CARD 0 AGE (53,90] .6500 .1312 AFFINITY_CARD 0 AGE [17,24] .6500 .2134 AFFINITY_CARD 0 BOOKKEEPING_APPLICATION 0 .6500 .1500 AFFINITY_CARD 0 BOOKKEEPING_APPLICATION 1 .6500 .8500 AFFINITY_CARD 0 BULK_PACK_DISKETTES 0 .6500 .3670