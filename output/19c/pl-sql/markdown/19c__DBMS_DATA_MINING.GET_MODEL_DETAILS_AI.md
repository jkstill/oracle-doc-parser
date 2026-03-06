---
id: 19c__DBMS_DATA_MINING.GET_MODEL_DETAILS_AI
name: DBMS_DATA_MINING.GET_MODEL_DETAILS_AI
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.GET_MODEL_DETAILS_AI

The GET_MODEL_DETAILS_AI function returns a set of rows that provide the details of an Attribute Importance model. Starting from Oracle Database 12 c Release 2, this function is deprecated. See "Model Detail Views" in Oracle Data Mining User’s Guide .

## Syntax

```sql
DBMS_DATA_MINING.get_model_details_ai(
      model_name IN VARCHAR2,
      partition_name IN VARCHAR2 DEFAULT NULL)
  RETURN dm_ranked_attributes pipelined;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| model_name | VARCHAR2 | IN | Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. |
| partition_name | VARCHAR2 | IN | Specifies a partition in a partitioned model. |

**Returns:** `dm_ranked_attributes`

## Usage Notes

Syntax DBMS_DATA_MINING.get_model_details_ai( model_name IN VARCHAR2, partition_name IN VARCHAR2 DEFAULT NULL) RETURN dm_ranked_attributes pipelined; Parameters Table 47-77 GET_MODEL_DETAILS_AI Function Parameters Parameter Description model_name Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. partition_name Specifies a partition in a partitioned model. Return Values Table 47-78 GET_MODEL_DETAILS_AI Function Return Values Return Value Description DM_RANKED_ATTRIBUTES A set of rows of type DM_RANKED_ATTRIBUTE . The rows have the following columns: (attribute_name VARCHAR2(4000, attribute_subname VARCHAR2(4000), importance_value NUMBER, rank NUMBER(38)) Examples The following example returns model details for the Attribute Importance model AI_SH_sample , which was created by the sample program dmaidemo.sql . For information about the sample programs, see Oracle Data Mining User's Guide . SELECT attribute_name, importance_value, rank FROM TABLE(DBMS_DATA_MINING.GET_MODEL_DETAILS_AI('AI_SH_sample')) ORDER BY RANK; ATTRIBUTE_NAME IMPORTANCE_VALUE RANK ---------------------------------------- ---------------- ---------- HOUSEHOLD_SIZE .151685183 1 CUST_MARITAL_STATUS .145294546 2 YRS_RESIDENCE .07838928 3 AGE .075027496 4 Y_BOX_GAMES .063039952 5 EDUCATION .059605314 6 HOME_THEATER_PACKAGE .056458722 7 OCCUPATION .054652937 8 CUST_GENDER .035264741 9 BOOKKEEPING_APPLICATION .019204751 10 PRINTER_SUPPLIES 0 11 OS_DOC_SET_KANJI -.00050013 12 FLAT_PANEL_MONITOR -.00509564 13 BULK_PACK_DISKETTES -.00540822 14 COUNTRY_NAME -.01201116 15 CUST_INCOME_LEVEL -.03951311 16