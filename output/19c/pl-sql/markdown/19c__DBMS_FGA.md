---
id: 19c__DBMS_FGA
name: DBMS_FGA
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FGA
tags: [dbms_fga]
source_file: DBMS_FGA.html
---

# DBMS_FGA

This package is available for only cost-based optimization. The rule-based optimizer may generate unnecessary audit records since audit monitoring can occur before row filtering.

## Usage Notes

For both the rule-based optimizer and the cost-based optimizer, you can query the SQL_TEXT and SQL_BINDS columns of the UNIFIED_AUDIT_TRAIL view to analyze the SQL text and corresponding bind variables that are issued.