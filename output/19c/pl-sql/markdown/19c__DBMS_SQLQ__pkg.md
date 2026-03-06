---
id: 19c__DBMS_SQLQ__pkg
name: DBMS_SQLQ
object_type: plsql_package
oracle_version: 19c
doc_type: plsql_packages
tags: [dbms_sqlq]
source_file: DBMS_SQLQ.html
---

# DBMS_SQLQ

The DBMS_SQLQ package provides the interface for configuring quarantine thresholds for execution plans of SQL statements. If any of the Resource Manager thresholds is equal to or less than the quarantine threshold specified in a SQL statement's quarantine configuration, then the SQL statement is not allowed to run, if it uses the execution plan specified in its quarantine configuration.