---
id: 19c__DBMS_METADATA.RULES
name: DBMS_METADATA.RULES
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_METADATA
tags: [dbms_metadata]
source_file: DBMS_METADATA.html
---

# DBMS_METADATA.RULES

In an Oracle Shared Server (OSS) environment, the DBMS_METADATA package must disable session migration and connection pooling.

## Usage Notes

This results in any shared server process that is serving a session running the package to effectively become a default, dedicated server for the life of the session. You should ensure that sufficient shared servers are configured when the package is used and that the number of servers is not artificially limited by too small a value for the MAX_SHARED_SERVERS initialization parameter.