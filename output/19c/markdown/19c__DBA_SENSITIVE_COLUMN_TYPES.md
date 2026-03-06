---
id: 19c__DBA_SENSITIVE_COLUMN_TYPES
name: DBA_SENSITIVE_COLUMN_TYPES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [dba]
source_file: DBA_SENSITIVE_COLUMN_TYPES.html
---

# DBA_SENSITIVE_COLUMN_TYPES

DBA_SENSITIVE_COLUMN_TYPES describes sensitive column types in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAME | VARCHAR2(128) | The name of the sensitive column type |
| USER_COMMENT | VARCHAR2(4000) | User comment on the sensitive column type |
| SOURCE_NAME | VARCHAR2(128) | The name of the discovery source for the sensitive column type |
| SOURCE_TYPE | VARCHAR2(3) | The type of the discovery source: ADM : import from ADM DB : added within the database |

## Usage Notes

See Also: Oracle Database Security Guide for more information about transparent sensitive data protection See Also: Oracle Database Security Guide for more information about transparent sensitive data protection