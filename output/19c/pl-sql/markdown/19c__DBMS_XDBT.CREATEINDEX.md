---
id: 19c__DBMS_XDBT.CREATEINDEX
name: DBMS_XDBT.CREATEINDEX
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBT
tags: [dbms_xdbt]
source_file: DBMS_XDBT.html
---

# DBMS_XDBT.CREATEINDEX

This procedure creates the CONTEXT index on the XML DB hierarchy.

## Syntax

```sql
DBMS_XDBT.CREATEINDEX;
```

## Usage Notes

Syntax DBMS_XDBT.CREATEINDEX; Usage Notes The name of the index can be changed; see the IndexName configuration setting. Set the LogFile configuration parameter to enable ROWID logging during index creation. Set the IndexMemory configuration parameter to determine the amount of memory that index creation, and later SYNCs, will use.