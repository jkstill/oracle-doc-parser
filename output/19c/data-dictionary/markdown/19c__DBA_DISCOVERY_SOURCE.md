---
id: 19c__DBA_DISCOVERY_SOURCE
name: DBA_DISCOVERY_SOURCE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_DISCOVERY_SOURCE.html
---

# DBA_DISCOVERY_SOURCE

DBA_DISCOVERY_SOURCE describes sensitive data discovery import information.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SOURCE_NAME | VARCHAR2(128) | The name of the discovery source. In the case of Application Data Model (ADM), this is the ADM instance name. |
| SOURCE_TYPE | VARCHAR2(6) | The type of the source: ADM : import from ADM CUSTOM : custom import DB : discovered within the database |
| CTIME | TIMESTAMP(6) | The last time sensitive data was imported from this source |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: Oracle Database Security Guide for more information about transparent sensitive data protection See Also: Oracle Database Security Guide for more information about transparent sensitive data protection