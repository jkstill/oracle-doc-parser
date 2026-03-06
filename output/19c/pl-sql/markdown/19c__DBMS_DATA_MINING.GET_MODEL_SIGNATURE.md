---
id: 19c__DBMS_DATA_MINING.GET_MODEL_SIGNATURE
name: DBMS_DATA_MINING.GET_MODEL_SIGNATURE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.GET_MODEL_SIGNATURE

The GET_MODEL_SIGNATURE function returns the list of columns from the build input table that were used by the build process to train the model. Starting from Oracle Database 12 c Release 2, this function is deprecated. See "Static Data Dictionary Views: ALL_ALL_TABLES to ALL_OUTLINES " in Oracle Database Reference .

## Syntax

```sql
FUNCTION get_model_signature (model_name IN VARCHAR2)
RETURN DM_Model_Signature PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| model_name | VARCHAR2) | IN | Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. |

**Returns:** `DM_Model_Signature`

## Usage Notes

Syntax FUNCTION get_model_signature (model_name IN VARCHAR2) RETURN DM_Model_Signature PIPELINED; Parameters Table 47-97 GET_MODEL_SIGNATURE Function Parameters Parameter Description model_name Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. Return Values Table 47-98 GET_MODEL_SIGNATURE Function Return Values Return Value Description DM_MODEL_SIGNATURE A set of rows of type DM_MODEL_SIGNATURE . The rows have the following columns: DM_MODEL_SIGNATURE TABLE OF SYS.DM_MODEL_SIGNATURE_ATTRIBUTE Name Type ------------------ ------------------- ATTRIBUTE_NAME VARCHAR2(130) ATTRIBUTE_TYPE VARCHAR2(106) Usage Notes This table function pipes out rows of type DM_MODEL_SIGNATURE . For information on Data Mining datatypes and piped output from table functions, see " DBMS_DATA_MINING Datatypes " . The signature names or types include only those attributes used by the build process. Examples The following example returns model settings for an example Naive Bayes model. ATTRIBUTE_NAME ATTRIBUTE_TYPE ------------------------------ ------------------ AGE NUMBER ANNUAL_INCOME NUMBER AVERAGE___ITEMS_PURCHASED NUMBER BOOKKEEPING_APPLICATION NUMBER BULK_PACK_DISKETTES NUMBER BULK_PURCH_AVE_AMT NUMBER DISABLE_COOKIES NUMBER EDUCATION VARCHAR2 FLAT_PANEL_MONITOR NUMBER GENDER VARCHAR2 HOME_THEATER_PACKAGE NUMBER HOUSEHOLD_SIZE VARCHAR2 MAILING_LIST NUMBER MARITAL_STATUS VARCHAR2 NO_DIFFERENT_KIND_ITEMS NUMBER OCCUPATION VARCHAR2 OS_DOC_SET_KANJI NUMBER PETS NUMBER PRINTER_SUPPLIES NUMBER PROMO_RESPOND NUMBER SHIPPING_ADDRESS_COUNTRY VARCHAR2 SR_CITIZEN NUMBER TOP_REASON_FOR_SHOPPING VARCHAR2 WKS_SINCE_LAST_PURCH NUMBER WORKCLASS VARCHAR2 YRS_RESIDENCE NUMBER Y_BOX_GAMES NUMBER 27 rows selected.