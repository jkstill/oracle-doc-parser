---
id: 19c__DBMS_AW_STATS.USING
name: DBMS_AW_STATS.USING
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AW_STATS
tags: [dbms_aw_stats]
source_file: DBMS_AW_STATS.html
---

# DBMS_AW_STATS.USING

Cubes and dimensions are first class data objects that support multidimensional analytics. They are stored in a container called an analytic workspace. Multidimensional objects and analytics are available with the OLAP option to Oracle Database.

## Usage Notes

Optimizer statistics are used to create execution plans for queries that join two cube views or join a cube view to a table or a view of a table. They are also used for query rewrite to cube materialized views. You need to generate the statistics only for these types of queries. Queries against a single cube do not use optimizer statistics. These queries are automatically optimized within the analytic workspace.