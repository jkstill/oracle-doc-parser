---
id: 19c__ALL_WARNING_SETTINGS
name: ALL_WARNING_SETTINGS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_WARNING_SETTINGS.html
---

# ALL_WARNING_SETTINGS

ALL_WARNING_SETTINGS displays information about the warning parameter settings for the objects accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the object |
| OBJECT_NAME | VARCHAR2(128) | Name of the object |
| OBJECT_ID | NUMBER | Object number of the object |
| OBJECT_TYPE | VARCHAR2(12) | Type of the object: PROCEDURE FUNCTION PACKAGE PACKAGE BODY TRIGGER TYPE TYPE BODY |
| WARNING | VARCHAR2(40) | Warning number or category: INFORMATIONAL PERFORMANCE SEVERE ALL |
| SETTING | VARCHAR2(7) | Value of the warning setting: DISABLE ENABLE ERROR |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_WARNING_SETTINGS displays information about the warning parameter settings for all objects in the database. USER_WARNING_SETTINGS displays information about the warning parameter settings for the objects owned by the current user. This view does not display the OWNER column. See Also: " DBA_WARNING_SETTINGS " " USER_WARNING_SETTINGS " See Also: " DBA_WARNING_SETTINGS " " USER_WARNING_SETTINGS "