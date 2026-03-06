---
id: 19c__ALL_CUBE_DIM_MODELS
name: ALL_CUBE_DIM_MODELS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_CUBE_DIM_MODELS.html
---

# ALL_CUBE_DIM_MODELS

ALL_CUBE_DIM_MODELS describes the models for the OLAP dimensions accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the cube dimension |
| DIMENSION_NAME | VARCHAR2(128) | Name of a cube dimension |
| MODEL_NAME | VARCHAR2(128) | Name of a model for the cube dimension |
| MODEL_ID | NUMBER | ID of the model |
| DESCRIPTION | NVARCHAR2(300) | Description of the model in the session language |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_CUBE_DIM_MODELS describes the models for all OLAP dimensions in the database. USER_CUBE_DIM_MODELS describes the models for the OLAP dimensions owned by the current user. This view does not display the OWNER column. See Also: " DBA_CUBE_DIM_MODELS " " USER_CUBE_DIM_MODELS " See Also: " DBA_CUBE_DIM_MODELS " " USER_CUBE_DIM_MODELS "