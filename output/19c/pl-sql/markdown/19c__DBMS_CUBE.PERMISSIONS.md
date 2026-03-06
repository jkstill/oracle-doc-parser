---
id: 19c__DBMS_CUBE.PERMISSIONS
name: DBMS_CUBE.PERMISSIONS
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE
tags: [dbms_cube]
source_file: DBMS_CUBE.html
---

# DBMS_CUBE.PERMISSIONS

Certain permissions are required to manage and query cube materialized views.

## Usage Notes

To create cube materialized views, you must have these privileges: CREATE [ANY] MATERIALIZED VIEW privilege CREATE [ANY] DIMENSION privilege ADVISOR privilege To access cube materialized views from another schema using query rewrite, you must have these privileges: GLOBAL QUERY REWRITE privilege SELECT or READ privilege on the relational source tables SELECT or READ privilege on the analytic workspace ( AW$ name ) that supports the cube materialized view SELECT or READ privilege on the cube SELECT or READ privilege on the dimensions of the cube Note that you need SELECT or READ privileges on the database objects that support the cube materialized views, but not on the cube materialized views.