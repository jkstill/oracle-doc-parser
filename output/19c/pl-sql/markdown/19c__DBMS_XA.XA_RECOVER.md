---
id: 19c__DBMS_XA.XA_RECOVER
name: DBMS_XA.XA_RECOVER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XA
tags: [dbms_xa]
source_file: DBMS_XA.html
---

# DBMS_XA.XA_RECOVER

This function obtains a list of prepared or heuristically completed transaction branches from a resource manager.

## Syntax

```sql
DBMS_XA.XA_RECOVER 
 RETURN DBMS_XA_XID_ARRAY;
```

**Returns:** `DBMS_XA_XID_ARRAY`

## Usage Notes

Syntax DBMS_XA.XA_RECOVER RETURN DBMS_XA_XID_ARRAY; Return Values See DBMS_XA_XID_ARRAY Table Type Usage Notes The flags TMSTARTSCAN , TMENDSCAN , TMNOFLAGS are not supported. The privilege SELECT ON DBA_PENDING_TRANSACTIONS must be granted to the user who needs to call XA_RECOVER .