---
id: 19c__DBMS_MVIEW.PURGE_DIRECT_LOAD_LOG
name: DBMS_MVIEW.PURGE_DIRECT_LOAD_LOG
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MVIEW
tags: [dbms_mview]
source_file: DBMS_MVIEW.html
---

# DBMS_MVIEW.PURGE_DIRECT_LOAD_LOG

This procedure removes entries from the direct loader log after they are no longer needed for any known materialized view. This procedure usually is used in environments using Oracle's data warehousing technology.

## Syntax

```sql
DBMS_MVIEW.PURGE_DIRECT_LOAD_LOG();
```

## Usage Notes

Syntax DBMS_MVIEW.PURGE_DIRECT_LOAD_LOG();