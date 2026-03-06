---
id: 19c__DBMS_DATA_MINING.REMOVE_COST_MATRIX
name: DBMS_DATA_MINING.REMOVE_COST_MATRIX
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.REMOVE_COST_MATRIX

The REMOVE_COST_MATRIX procedure removes the default scoring matrix from a classification model.

## Syntax

```sql
DBMS_DATA_MINING.REMOVE_COST_MATRIX (
      model_name   IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| model_name | VARCHAR2) | IN | Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, your own schema is used. |

## Usage Notes

See Also: " ADD_COST_MATRIX Procedure " " REMOVE_COST_MATRIX Procedure " See Also: " ADD_COST_MATRIX Procedure " " REMOVE_COST_MATRIX Procedure " Syntax DBMS_DATA_MINING.REMOVE_COST_MATRIX ( model_name IN VARCHAR2); Parameters Table 47-112 Remove_Cost_Matrix Procedure Parameters Parameter Description model_name Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, your own schema is used. Usage Notes If the model is not in your schema, then REMOVE_COST_MATRIX requires the ALTER ANY MINING MODEL system privilege or the ALTER object privilege for the mining model.