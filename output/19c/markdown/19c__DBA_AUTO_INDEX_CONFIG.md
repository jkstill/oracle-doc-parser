---
id: 19c__DBA_AUTO_INDEX_CONFIG
name: DBA_AUTO_INDEX_CONFIG
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: index
tags: [dba]
source_file: DBA_AUTO_INDEX_CONFIG.html
---

# DBA_AUTO_INDEX_CONFIG

DBA_AUTO_INDEX_CONFIG displays the current configuration parameter settings for automatic indexing.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PARAMETER_NAME | VARCHAR2(128) | Name of the configuration parameter |
| PARAMETER_VALUE | VARCHAR2(4000) | Value of the configuration parameter |
| LAST_MODIFIED | TIMESTAMP(6) | Time at which the parameter value was last modified |
| MODIFIED_BY | VARCHAR2(128) | User who last modified the parameter value |

## Usage Notes

You can set automatic indexing configuration parameters by using the DBMS_AUTO_INDEX.CONFIGURE procedure. Note: This view is available starting with Oracle Database release 19c, version 19.1. See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_AUTO_INDEX.CONFIGURE procedure Note: This view is available starting with Oracle Database release 19c, version 19.1. See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_AUTO_INDEX.CONFIGURE procedure