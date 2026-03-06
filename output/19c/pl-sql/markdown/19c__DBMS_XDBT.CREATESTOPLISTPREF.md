---
id: 19c__DBMS_XDBT.CREATESTOPLISTPREF
name: DBMS_XDBT.CREATESTOPLISTPREF
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBT
tags: [dbms_xdbt]
source_file: DBMS_XDBT.html
---

# DBMS_XDBT.CREATESTOPLISTPREF

This procedure creates a stoplist for the CONTEXT index on the XML DB hierarchy.

## Syntax

```sql
DBMS_XDBT.CREATESTOPLISTPREF;
```

## Usage Notes

Syntax DBMS_XDBT.CREATESTOPLISTPREF; Usage Notes The name of the stoplist can be modified; see the StoplistPref configuration setting. Numbers are not indexed. The StopWords array is a configurable list of stopwords. These are meant to be stopwords in addition to the set of stopwords in CTXSYS.DEFAULT_STOPLIST.