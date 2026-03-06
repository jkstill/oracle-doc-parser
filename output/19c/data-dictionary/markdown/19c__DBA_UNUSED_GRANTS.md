---
id: 19c__DBA_UNUSED_GRANTS
name: DBA_UNUSED_GRANTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [dba]
source_file: DBA_UNUSED_GRANTS.html
---

# DBA_UNUSED_GRANTS

DBA_UNUSED_GRANTS shows all the grants that are not used during the privilege capture.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CAPTURE | VARCHAR2(128) | Name of the privilege analysis policy |
| RUN_NAME | VARCHAR2(128) | Name of the run of the privilege analysis policy |
| GRANTEE | VARCHAR2(128) | Name of the user who is granted with the privilege or role |
| ROLENAME | VARCHAR2(128) | Name of the role that is granted to the grantee |
| SYS_PRIV | VARCHAR2(40) | Name of the system privilege that is granted to the grantee |
| OBJ_PRIV | VARCHAR2(40) | Name of the object privilege that is granted to the grantee |
| USER_PRIV | VARCHAR2(25) | Name of the user privilege that is granted to the grantee |
| OBJECT_OWNER | VARCHAR2(128) | Name of the owner of the object for which the object privilege is granted |
| OBJECT_NAME | VARCHAR2(128) | Name of the object for which the object privilege is granted |
| OBJECT_TYPE | VARCHAR2(23) | Type of the object for which the object privilege is granted |
| COLUMN_NAME | VARCHAR2(128) | Name of the column in the table for which the object privilege is granted |
| OPTION$ | NUMBER | Whether the grant option of the privilege is granted |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: Oracle Database Security Guide for more information about privilege analysis See Also: Oracle Database Security Guide for more information about privilege analysis