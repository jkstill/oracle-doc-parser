---
id: 19c__DBA_SENSITIVE_DATA
name: DBA_SENSITIVE_DATA
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_SENSITIVE_DATA.html
---

# DBA_SENSITIVE_DATA

DBA_SENSITIVE_DATA describes the sensitive columns in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SENSITIVE# | NUMBER | Dictionary ID for the sensitive data |
| SCHEMA_NAME | VARCHAR2(128) | The schema containing the sensitive data |
| TABLE_NAME | VARCHAR2(128) | The table containing the sensitive data |
| COLUMN_NAME | VARCHAR2(128) | The name of the column identified as sensitive |
| SENSITIVE_TYPE | VARCHAR2(128) | The sensitive column type of the data |
| SOURCE_NAME | VARCHAR2(128) | The name of the discovery source for the sensitive data |
| USER_COMMENT | VARCHAR2(4000) | User comment on the sensitive data |
| TS | TIMESTAMP(6) | The time when the data was identified as sensitive in the database |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: Oracle Database Security Guide for more information about transparent sensitive data protection See Also: Oracle Database Security Guide for more information about transparent sensitive data protection