---
id: 19c__DBA_ROLLING_PARAMETERS
name: DBA_ROLLING_PARAMETERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: configuration
tags: [dba]
source_file: DBA_ROLLING_PARAMETERS.html
---

# DBA_ROLLING_PARAMETERS

DBA_ROLLING_PARAMETERS lists the available parameters of the DBMS_ROLLING PL/SQL package.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SCOPE | VARCHAR2(128) | Database unique name associated with a parameter |
| TYPE | VARCHAR2(7) | Type of parameter |
| NAME | VARCHAR2(32) | Name of the parameter |
| DESCRIPTION | VARCHAR2(256) | Description of the parameter |
| CURVAL | VARCHAR2(256) | Current value of the parameter |
| LSTVAL | VARCHAR2(256) | Prior value of the parameter |
| DEFVAL | VARCHAR2(256) | Default value of the parameter |
| MINVAL | NUMBER | Minimum value of the parameter |
| MAXVAL | NUMBER | Maximum value of the parameter |

## Usage Notes

See Also: Oracle Data Guard Concepts and Administration for more information about rolling operations. Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_ROLLING package See Also: Oracle Data Guard Concepts and Administration for more information about rolling operations. Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_ROLLING package