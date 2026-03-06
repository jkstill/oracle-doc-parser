---
id: 19c__DBA_ILMPARAMETERS
name: DBA_ILMPARAMETERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: configuration
tags: [dba]
source_file: DBA_ILMPARAMETERS.html
---

# DBA_ILMPARAMETERS

DBA_ILMPARAMETERS can be queried to provide information on the Automatic Data Optimization parameters in the database and their values.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAME | VARCHAR2(128) | Name of the Automatic Data Optimization environment parameter. The value is one of the constants defined in the DBMS_ILM_ADMIN package. |
| VALUE | NUMBER | Value of the parameter |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: Automatic Data Optimization is supported in Oracle Database 12 c Release 2 multitenant environments. Note: Automatic Data Optimization is supported in Oracle Database 12 c Release 2 multitenant environments. See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the API interface for implementing Automatic Data Optimization strategies Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_ILM_ADMIN package See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the API interface for implementing Automatic Data Optimization strategies Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_ILM_ADMIN package