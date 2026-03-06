---
id: 19c__DBMS_DATA_MINING.EXPORT_SERMODEL
name: DBMS_DATA_MINING.EXPORT_SERMODEL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.EXPORT_SERMODEL

This procedure exports the model in a serialized format so that they can be moved to another platform for scoring.

## Syntax

```sql
DBMS_DATA_MINING.EXPORT_SERMODEL (
      model_data     IN OUT NOCOPY BLOB,
      model_name     IN VARCHAR2,
      partition_name IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| model_data | NOCOPY | IN OUT | Provides serialized model data. |
| model_name | VARCHAR2 | IN | Name of the mining model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. |
| partition_name | VARCHAR2 | IN | Name of the partition that must be exported. |

## Usage Notes

When exporting a model in serialized format, the user must pass in an empty BLOB locator and specify the model name to be exported. If the model is partitioned, the user can optionally select an individual partition to export, otherwise all partitions are exported. The returned BLOB contains the content that can be deployed. Syntax DBMS_DATA_MINING.EXPORT_SERMODEL ( model_data IN OUT NOCOPY BLOB, model_name IN VARCHAR2, partition_name IN VARCHAR2 DEFAULT NULL); Parameters Table 47-69 EXPORT_SERMODEL Procedure Parameters Parameter Description model_data Provides serialized model data. model_name Name of the mining model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. partition_name Name of the partition that must be exported. Examples The following statement exports all the models in a serialized format. DECLARE v_blob blob; BEGIN dbms_lob.createtemporary(v_blob, FALSE); dbms_data_mining.export_sermodel(v_blob, 'MY_MODEL'); -- save v_blob somewhere (e.g., bfile, etc.) dbms_lob.freetemporary(v_blob); END; / See Also: Oracle Data Mining User's Guide for more information about exporting and importing mining models See Also: Oracle Data Mining User's Guide for more information about exporting and importing mining models