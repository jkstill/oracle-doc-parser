---
id: 19c__DBMS_DBCOMP__pkg
name: DBMS_DBCOMP
object_type: plsql_package
oracle_version: 19c
doc_type: plsql_packages
tags: [dbms_dbcomp]
source_file: DBMS_DBCOMP.html
---

# DBMS_DBCOMP

The DBMS_DBCOMP package performs block comparison to detect lost writes or database inconsistencies between a primary database and one or more physical standby databases. It contains one procedure, DBCOMP , which can be executed at any time. (It does not require that the DB_LOST_WRITE_PROTECT initialization parameter be enabled.)