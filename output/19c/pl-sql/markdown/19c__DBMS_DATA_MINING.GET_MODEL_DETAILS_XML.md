---
id: 19c__DBMS_DATA_MINING.GET_MODEL_DETAILS_XML
name: DBMS_DATA_MINING.GET_MODEL_DETAILS_XML
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.GET_MODEL_DETAILS_XML

This function returns an XML object that provides the details of a Decision Tree model.

## Syntax

```sql
DBMS_DATA_MINING.get_model_details_xml(
      model_name IN VARCHAR2,
      partition_name IN VARCHAR2 DEFAULT NULL)
  RETURN XMLType;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| model_name | VARCHAR2 | IN | Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. |
| partition_name | VARCHAR2 | IN | Specifies a partition in a partitioned model. |

**Returns:** `XMLType`

## Usage Notes

Syntax DBMS_DATA_MINING.get_model_details_xml( model_name IN VARCHAR2, partition_name IN VARCHAR2 DEFAULT NULL) RETURN XMLType; Parameters Table 47-103 GET_MODEL_DETAILS_XML Function Parameters Parameter Description model_name Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. partition_name Specifies a partition in a partitioned model. Return Values Table 47-104 GET_MODEL_DETAILS_XML Function Return Value Return Value Description XMLTYPE The XML definition for the Decision Tree model. See "XMLTYPE" for details. The XML definition conforms to the Data Mining Group Predictive Model Markup Language ( PMML) version 2.1 specification. The specification is available at https://dmg.org . If a nested attribute is used as a splitter, the attribute will appear in the XML document as field="'<column_name>'.<subname>", as opposed to the non-nested attributes which appear in the document as field="<column_name>". Note: The column names are surrounded by single quotes and a period separates the column_name from the subname. The rest of the document style remains unchanged. Note: The column names are surrounded by single quotes and a period separates the column_name from the subname. Usage Notes Special characters that cannot be displayed by Oracle XML are converted to '#'.