---
id: 19c__DBA_PRIV_CAPTURES
name: DBA_PRIV_CAPTURES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [dba]
source_file: DBA_PRIV_CAPTURES.html
---

# DBA_PRIV_CAPTURES

DBA_PRIV_CAPTURES lists the privilege analysis policies in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAME | VARCHAR2(128) | Name of the privilege analysis policy |
| DESCRIPTION | VARCHAR2(1024) | Description of the privilege analysis |
| TYPE | VARCHAR2(16) | Type of the privilege analysis policy. Possible values: G_DATABASE : Database wide privilege analysis G_ROLE : Role privilege analysis G_CONTEXT : Context privilege analysis G_ROLE_AND_CONTEXT : Role and context privilege analysis |
| ENABLED | VARCHAR2(1) | Enabling status of the privilege analysis |
| ROLES | ROLE_ID_LIST | List of roles whose privileges to analyze if the privilege analysis type is G_ROLE or G_ROLE_AND_CONTEXT |
| CONTEXT | VARCHAR2(4000) | Context condition if the privilege analysis type is G_CONTEXT or G_ROLE_AND_CONTEXT |
| RUN_NAME | VARCHAR2(128) | Displays run name information for each run |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: Oracle Database Security Guide for more information about privilege analysis See Also: Oracle Database Security Guide for more information about privilege analysis