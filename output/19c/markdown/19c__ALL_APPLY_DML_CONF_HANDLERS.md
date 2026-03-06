---
id: 19c__ALL_APPLY_DML_CONF_HANDLERS
name: ALL_APPLY_DML_CONF_HANDLERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_APPLY_DML_CONF_HANDLERS.html
---

# ALL_APPLY_DML_CONF_HANDLERS

ALL_APPLY_DML_CONF_HANDLERS provides details about DML conflict handlers on objects visible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| APPLY_NAME | VARCHAR2(128) | Name of the apply process |
| OBJECT_OWNER | VARCHAR2(128) | Owner of the target object |
| OBJECT_NAME | VARCHAR2(128) | Name of the target object |
| SOURCE_OBJECT_OWNER | VARCHAR2(128) | Source database owner of the object |
| SOURCE_OBJECT_NAME | VARCHAR2(128) | Source database name of the object |
| COMMAND_TYPE | VARCHAR2(6) | Type of the DML operation: INSERT , UPDATE , or DELETE |
| CONFLICT_TYPE | VARCHAR2(11) | Type of conflict: ROW EXISTS ROW MISSING |
| METHOD_NAME | VARCHAR2(9) | Method used for resolving the error, depending on the conflict type: OVERWRITE RECORD IGNORE MAXIMUM MINIMUM DELTA |
| CONFLICT_HANDLER_NAME | VARCHAR2(128) | Name of the conflict handler |
| RESOLUTION_COLUMN | VARCHAR2(128) | Name of the column used to resolve the conflict for MAXIMUM , MINIMUM , and DELTA |
| SET_BY | VARCHAR2(10) | Entity that set up the handler: USER GOLDENGATE |

## Usage Notes

Related View DBA_APPLY_DML_CONF_HANDLERS provides details about DML conflict handlers. See Also: " DBA_APPLY_DML_CONF_HANDLERS " See Also: " DBA_APPLY_DML_CONF_HANDLERS "