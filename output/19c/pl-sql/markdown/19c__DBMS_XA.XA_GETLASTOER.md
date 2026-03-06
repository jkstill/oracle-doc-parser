---
id: 19c__DBMS_XA.XA_GETLASTOER
name: DBMS_XA.XA_GETLASTOER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XA
tags: [dbms_xa]
source_file: DBMS_XA.html
---

# DBMS_XA.XA_GETLASTOER

This function obtains the last Oracle error code, in case of failure of previous XA calls.

## Syntax

```sql
DBMS_XA.XA_GETLASTOER  
 RETURN PLS_INTEGER;
```

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax DBMS_XA.XA_GETLASTOER RETURN PLS_INTEGER; Return Values The return value carries the last Oracle error code.