---
id: 19c__DBMS_LIBCACHE__pkg
name: DBMS_LIBCACHE
object_type: plsql_package
oracle_version: 19c
doc_type: plsql_packages
tags: [dbms_libcache]
source_file: DBMS_LIBCACHE.html
---

# DBMS_LIBCACHE

The DBMS_LIBCACHE package consists of one subprogram that prepares the library cache on an Oracle instance by extracting SQL and PL/SQL from a remote instance and compiling this SQL locally without execution. The value of compiling the cache of an instance is to prepare the information the application requires to execute in advance of failover or switchover.