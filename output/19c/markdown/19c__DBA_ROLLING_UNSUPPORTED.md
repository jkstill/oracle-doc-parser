---
id: 19c__DBA_ROLLING_UNSUPPORTED
name: DBA_ROLLING_UNSUPPORTED
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_ROLLING_UNSUPPORTED.html
---

# DBA_ROLLING_UNSUPPORTED

DBA_ROLLING_UNSUPPORTED displays the schemas, tables, and columns in those tables that contain unsupported data types for a rolling upgrade operation for a logical standby database using the DBMS_ROLLING PL/SQL package.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Schema name of the unsupported column |
| TABLE_NAME | VARCHAR2(128) | Name of the table that the unsupported column belongs to |
| COLUMN_NAME | VARCHAR2(128) | Name of the unsupported column |
| ATTRIBUTES | VARCHAR2(39) | If not a data type issue, displays the reason why the table is unsupported |
| DATA_TYPE | VARCHAR2(106) | Data type of the unsupported column |

## Usage Notes

Use this view before you perform a rolling upgrade using DBMS_ROLLING to determine what is unsupported. The data pertains to the container in which the view is queried. Note: A rolling upgrade using DBMS_ROLLING supports more object types than a manual rolling upgrade using transient logical standby databases See Also: " DBA_LOGSTDBY_UNSUPPORTED " for more information about determining unsupported data types for a manual rolling upgrade operation using transient logical standby databases Oracle Data Guard Concepts and Administration for more information about rolling operations Oracle Data Guard Concepts and Administration for more information about unsupported tables for rolling upgrade operations Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_ROLLING package Note: A rolling upgrade using DBMS_ROLLING supports more object types than a manual rolling upgrade using transient logical standby databases See Also: " DBA_LOGSTDBY_UNSUPPORTED " for more information about determining unsupported data types for a manual rolling upgrade operation using transient logical standby databases Oracle Data Guard Concepts and Administration for more information about rolling operations Oracle Data Guard Concepts and Administration for more information about unsupported tables for rolling upgrade operations Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_ROLLING package