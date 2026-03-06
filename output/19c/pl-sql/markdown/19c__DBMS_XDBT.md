---
id: 19c__DBMS_XDBT
name: DBMS_XDBT
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBT
tags: [dbms_xdbt]
source_file: DBMS_XDBT.html
---

# DBMS_XDBT

Configuration settings, or package variables, are available to customize the DBMS_XDBT package.

## Usage Notes

The DBMS_XDBT package can be customized by using a PL/SQL procedure or an anonymous block to set the relevant package variables, configuration settings, and then execute the procedures. A more general approach would be to introduce the appropriate customizations by modifying this package in place, or as a copy. The system must be configured to use job queues, and the jobs can be viewed through the USER_JOBS catalog views.