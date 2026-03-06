---
id: 19c__DBA_LOGSTDBY_UNSUPPORTED
name: DBA_LOGSTDBY_UNSUPPORTED
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dba]
source_file: DBA_LOGSTDBY_UNSUPPORTED.html
---

# DBA_LOGSTDBY_UNSUPPORTED

DBA_LOGSTDBY_UNSUPPORTED displays the schemas, tables, and columns in those tables that contain unsupported data types.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the unsupported table |
| TABLE_NAME | VARCHAR2(128) | Name of the unsupported table |
| COLUMN_NAME | VARCHAR2(128) | Name of the unsupported column |
| ATTRIBUTES | VARCHAR2(39) | When possible, displays the reason why the table is not supported by SQL Apply. The ATTRIBUTES column may be NULL if the table structure itself is not supported by SQL Apply (for example, the table is system-partitioned), or when the structure of the table is supported but certain columns in the table have an unsupported datatype. |
| DATA_TYPE | VARCHAR2(32) | Datatype of the unsupported column |

## Usage Notes

Note: A rolling upgrade performed using the DBMS_ROLLING PL/SQL package supports more object types than a manual rolling upgrade performed using transient logical standby databases. See Also: " DBA_ROLLING_UNSUPPORTED " for more information about determining unsupported data types for a rolling upgrade using the DBMS_ROLLING package Oracle Data Guard Concepts and Administration for more information about rolling operations Oracle Data Guard Concepts and Administration for more information about unsupported tables for rolling upgrade operations Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_ROLLING package Note: A rolling upgrade performed using the DBMS_ROLLING PL/SQL package supports more object types than a manual rolling upgrade performed using transient logical standby databases. See Also: " DBA_ROLLING_UNSUPPORTED " for more information about determining unsupported data types for a rolling upgrade using the DBMS_ROLLING package Oracle Data Guard Concepts and Administration for more information about rolling operations Oracle Data Guard Concepts and Administration for more information about unsupported tables for rolling upgrade operations Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_ROLLING package