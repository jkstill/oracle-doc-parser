---
id: 19c__DBA_LOGSTDBY_PLSQL_SUPPORT
name: DBA_LOGSTDBY_PLSQL_SUPPORT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dba]
source_file: DBA_LOGSTDBY_PLSQL_SUPPORT.html
---

# DBA_LOGSTDBY_PLSQL_SUPPORT

DBA_LOGSTDBY_PLSQL_SUPPORT shows the PL/SQL packages that are only supported during rolling operations.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner name of the package |
| PKG_NAME | VARCHAR2(128) | Package name of the user invokable procedure |
| SUPPORT_LEVEL | VARCHAR2(12) | Logical standby PL/SQL support level for the package: ALWAYS - PL/SQL replication is always supported for this package, whether it is called inside or outside of DBMS_ROLLING DBMS_ROLLING : PL/SQL replication is supported only when the procedure is called inside DBMS_ROLLING |

## Usage Notes

Note: In a CDB, this view shows data when queried in the root or a PDB. See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_ROLLING package Note: In a CDB, this view shows data when queried in the root or a PDB. See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_ROLLING package