---
id: 19c__DBMS_DATA_MINING.IMPORT_SERMODEL
name: DBMS_DATA_MINING.IMPORT_SERMODEL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.IMPORT_SERMODEL

This procedure imports the serialized format of the model back into a database.

## Syntax

```sql
DBMS_DATA_MINING.IMPORT_SERMODEL (
      model_data     IN BLOB,
      model_name     IN VARCHAR2,);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| model_data | BLOB | IN | Provides model data in BLOB format. |
| model_name | VARCHAR2 | IN | Name of the mining model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. |

## Usage Notes

The import routine takes the serialized content in the BLOB and the name of the model to be created with the content. This import does not create model views or tables that are needed for querying model details. The import procedure only provides the ability to score the model. Syntax DBMS_DATA_MINING.IMPORT_SERMODEL ( model_data IN BLOB, model_name IN VARCHAR2,); Parameters Table 47-109 IMPORT_SERMODEL Procedure Parameters Parameter Description model_data Provides model data in BLOB format. model_name Name of the mining model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. Examples The following statement imports the serialized format of the models. declare v_blob blob; BEGIN dbms_lob.createtemporary(v_blob, FALSE); -- fill in v_blob from somewhere (e.g., bfile, etc.) dbms_data_mining.import_sermodel(v_blob, 'MY_MODEL'); dbms_lob.freetemporary(v_blob); END; / See Also: Oracle Data Mining User's Guide for more information about exporting and importing mining models