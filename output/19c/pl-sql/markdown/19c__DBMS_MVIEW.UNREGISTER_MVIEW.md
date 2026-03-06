---
id: 19c__DBMS_MVIEW.UNREGISTER_MVIEW
name: DBMS_MVIEW.UNREGISTER_MVIEW
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MVIEW
tags: [dbms_mview]
source_file: DBMS_MVIEW.html
---

# DBMS_MVIEW.UNREGISTER_MVIEW

This procedure enables the administration of individual materialized views. It is invoked at a master site or master materialized view site to unregister a materialized view.

## Syntax

```sql
DBMS_MVIEW.UNREGISTER_MVIEW (
   mviewowner      IN   VARCHAR2,
   mviewname       IN   VARCHAR2,
   mviewsite       IN   VARCHAR2);
```

## Usage Notes

Syntax DBMS_MVIEW.UNREGISTER_MVIEW ( mviewowner IN VARCHAR2, mviewname IN VARCHAR2, mviewsite IN VARCHAR2); Parameters Table 113-14 UNREGISTER_MVIEW Procedure Parameters Parameters Description mviewowner Owner of the materialized view mviewname Name of the materialized view mviewsite Name of the materialized view site