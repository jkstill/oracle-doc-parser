---
id: 19c__DBMS_LOGSTDBY_CONTEXT__pkg
name: DBMS_LOGSTDBY_CONTEXT
object_type: plsql_package
oracle_version: 19c
doc_type: plsql_packages
tags: [dbms_logstdby_context]
source_file: DBMS_LOGSTDBY_CONTEXT.html
---

# DBMS_LOGSTDBY_CONTEXT

As of Oracle Database 12 c release 1 (12.1), SQL Apply processes have access to a context namespace called LSBY_APPLY_CONTEXT . You can use the procedures provided in the DBMS_LOGSTDBY_CONTEXT package to set and retrieve various parameters associated with LSBY_APPLY_CONTEXT . This is useful when writing skip procedures that are registered with SQL Apply using the DBMS_LOGSTBDY.SKIP and DBMS_LOGSTDBY.SKIP_ERROR procedures.