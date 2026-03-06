---
id: 19c__ALL_MINING_MODEL_VIEWS
name: ALL_MINING_MODEL_VIEWS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_MINING_MODEL_VIEWS.html
---

# ALL_MINING_MODEL_VIEWS

ALL_MINING_MODEL_VIEWS provides a description of all the model views accessible to the user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the model view |
| MODEL_NAME | VARCHAR2(128) | Name of the model to which model views belongs |
| VIEW_NAME | VARCHAR2(128) | Name of the model view |
| VIEW_TYPE | VARCHAR2(128) | Type of the model view |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_MINING_MODEL_VIEWS provides a description of all the model views in the database. USER_MINING_MODEL_VIEWS provides a description of the user's own model views. This view does not display the OWNER column. See Also: " ALL_MINING_MODEL_VIEWS " in Oracle Data Mining User’s Guide See Also: " ALL_MINING_MODEL_VIEWS " in Oracle Data Mining User’s Guide