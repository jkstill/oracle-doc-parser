---
id: 19c__ALL_MINING_MODEL_SETTINGS
name: ALL_MINING_MODEL_SETTINGS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_MINING_MODEL_SETTINGS.html
---

# ALL_MINING_MODEL_SETTINGS

ALL_MINING_MODEL_SETTINGS describes the settings of the mining models accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the mining model |
| MODEL_NAME | VARCHAR2(128) | Name of the mining model |
| SETTING_NAME | VARCHAR2(30) | Name of the setting |
| SETTING_VALUE | VARCHAR2(4000) | Value of the setting |
| SETTING_TYPE | VARCHAR2(7) | Indicates whether the default value ( DEFAULT ) or a user-specified value ( INPUT ) is used by the model |

## Usage Notes

Mining models are schema objects created by Oracle Data Mining. Related Views DBA_MINING_MODEL_SETTINGS describes the settings of all mining models in the database. USER_MINING_MODEL_SETTINGS describes the settings of the mining models owned by the current user. This view does not display the OWNER column. See Also: Oracle Database PL/SQL Packages and Types Reference for descriptions of model settings See Also: Oracle Database PL/SQL Packages and Types Reference for descriptions of model settings