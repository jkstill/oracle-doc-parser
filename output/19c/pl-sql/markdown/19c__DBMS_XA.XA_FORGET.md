---
id: 19c__DBMS_XA.XA_FORGET
name: DBMS_XA.XA_FORGET
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XA
tags: [dbms_xa]
source_file: DBMS_XA.html
---

# DBMS_XA.XA_FORGET

This function informs the resource manager to forget about a heuristically committed or rolled back transaction branch.

## Syntax

```sql
DBMS_XA.XA_FORGET (
   xid       IN  DBMS_XA_XID)
RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xid | DBMS_XA_XID) | IN | See DBMS_XA_XID Object Type |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax DBMS_XA.XA_FORGET ( xid IN DBMS_XA_XID) RETURN PLS_INTEGER; Parameters Table 193-7 XA_FORGET Function Parameters Parameter Description xid See DBMS_XA_XID Object Type Return Values See Table 193-2 . Possible return values are XA_OK , XAER_RMERR , XAER_RMFAIL , XAER_NOTA , XAER_INVAL , or XAER_PROTO .