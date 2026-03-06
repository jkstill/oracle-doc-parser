---
id: 19c__ALL_MINING_MODEL_ATTRIBUTES
name: ALL_MINING_MODEL_ATTRIBUTES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_MINING_MODEL_ATTRIBUTES.html
---

# ALL_MINING_MODEL_ATTRIBUTES

Mining models are schema objects created by Oracle Data Mining.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the mining model |
| MODEL_NAME | VARCHAR2(128) | Name of the mining model |
| ATTRIBUTE_NAME | VARCHAR2(128) | Name of the attribute |
| ATTRIBUTE_TYPE | VARCHAR2(11) | Logical type of the attribute. The type is identified during the model build or apply process: NUMERICAL : Numeric data CATEGORICAL : Character data TEXT : Unstructured text data PARTITION : The input signature column is used for the partitioning key MIXED : The input signature column takes on more than one attribute type. This is due to user-defined embedded transformations that allow an input column to be transformed into multiple independent mining attributes, including mining attributes of different types. |
| DATA_TYPE | VARCHAR2(106) | Data type of the attribute |
| DATA_LENGTH | NUMBER | Length of the data type |
| DATA_PRECISION | NUMBER | Precision of a fixed point number. Precision, which is the total number of significant decimal digits, is represented as p in the data type NUMBER(p,s) . |
| DATA_SCALE | NUMBER | Scale of a fixed point number. Scale, which is the number of digits from the decimal to the least significant digit, is represented as s in the data type NUMBER(p,s) . |
| USAGE_TYPE | VARCHAR2(8) | Indicates whether the attribute was used to construct the model ( ACTIVE ) or not ( INACTIVE ). Some attributes may be eliminated by transformations or algorithmic processing. The *_MINING_MODEL_ATTRIBUTES view only lists the attributes used by the model, therefore the value of this column is always ACTIVE . |
| TARGET | VARCHAR2(3) | Indicates whether the attribute is the target of a predictive model ( YES ) or not ( NO ). The target describes the result that is produced when the model is applied. |
| ATTRIBUTE_SPEC | VARCHAR2(4000) | One or more keywords that identify special treatment for the attribute during model build. Values are: FORCE_IN : (GLM only) When feature selection is enabled, forces the inclusion of the attribute in the model build. Feature selection is disabled by default. If the model is not using GLM with feature selection enabled, this value is ignored. NOPREP : When ADP is on, prevents automatic transformation of the attribute. If ADP is OFF , this value is ignored. TEXT : Causes the attribute to be treated as unstructured text data. The TEXT value supports three subsettings: POLICY_NAME , MAX_FEATURES , TOKEN_TYPE , and MIN_DOCUMENTS . Subsettings are specified as name:value pairs within parentheses. For example: (POLICY_NAME:mypolicy) (MAX_FEATURES:2000)(TOKEN_TYPE:THEME) . See Oracle Data Mining User’s Guide for details. NULL : The ATTRIBUTE_SPEC for this attribute is NULL . ATTRIBUTE_SPEC is a parameter to the PL/SQL procedure DBMS_DATA_MINING_TRANSFORM.SET_TRANSFORM . See Oracle Database PL/SQL Packages and Types Reference for details. |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_MINING_MODEL_ATTRIBUTES describes the attributes of all mining models in the database. USER_MINING_MODEL_ATTRIBUTES describes the attributes of the mining models owned by the current user. This view does not display the OWNER column. See Also: Oracle Data Mining User’s Guide for more information about the attributes of machine learning models See Also: Oracle Data Mining User’s Guide for more information about the attributes of machine learning models