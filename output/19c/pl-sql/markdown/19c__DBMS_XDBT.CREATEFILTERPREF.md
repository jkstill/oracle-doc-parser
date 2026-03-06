---
id: 19c__DBMS_XDBT.CREATEFILTERPREF
name: DBMS_XDBT.CREATEFILTERPREF
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBT
tags: [dbms_xdbt]
source_file: DBMS_XDBT.html
---

# DBMS_XDBT.CREATEFILTERPREF

This procedure creates a NULL filter preference for the CONTEXT index on the XML DB hierarchy.

## Syntax

```sql
DBMS_XDBT.CREATEFILTERPREF;
```

## Usage Notes

Syntax DBMS_XDBT.CREATEFILTERPREF; Usage Notes The name of the filter preference can be modified; see FilterPref configuration setting. The USER datastore procedure filters the incoming document; see CREATEDATASTOREPREF Procedure for more details.