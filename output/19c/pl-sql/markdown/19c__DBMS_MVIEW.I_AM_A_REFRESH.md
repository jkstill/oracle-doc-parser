---
id: 19c__DBMS_MVIEW.I_AM_A_REFRESH
name: DBMS_MVIEW.I_AM_A_REFRESH
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MVIEW
tags: [dbms_mview]
source_file: DBMS_MVIEW.html
---

# DBMS_MVIEW.I_AM_A_REFRESH

This function returns the value of the I_AM_REFRESH package state.

## Syntax

```sql
DBMS_MVIEW.I_AM_A_REFRESH
   RETURN BOOLEAN;
```

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_MVIEW.I_AM_A_REFRESH RETURN BOOLEAN; Return Values A return value of true indicates that all local replication triggers for materialized views are effectively disabled in this session because each replication trigger first checks this state. A return value of false indicates that these triggers are enabled.