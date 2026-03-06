---
id: 19c__DBMS_PCLXUTIL__pkg
name: DBMS_PCLXUTIL
object_type: plsql_package
oracle_version: 19c
doc_type: plsql_packages
tags: [dbms_pclxutil]
source_file: DBMS_PCLXUTIL.html
---

# DBMS_PCLXUTIL

The DBMS_PCLXUTIL package provides intra-partition parallelism for creating partition-wise local indexes. DBMS_PCLXUTIL circumvents the limitation that, for local index creation, the degree of parallelism is restricted to the number of partitions as only one parallel execution server process for each partition is used.