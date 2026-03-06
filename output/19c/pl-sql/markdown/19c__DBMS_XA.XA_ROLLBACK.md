---
id: 19c__DBMS_XA.XA_ROLLBACK
name: DBMS_XA.XA_ROLLBACK
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XA
tags: [dbms_xa]
source_file: DBMS_XA.html
---

# DBMS_XA.XA_ROLLBACK

This function informs the resource manager to roll back work done on behalf of a transaction branch.

## Syntax

```sql
DBMS_XA.XA_ROLLBACK (
   xid       IN  DBMS_XA_XID)
 RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xid | DBMS_XA_XID) | IN | See DBMS_XA_XID Object Type |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax DBMS_XA.XA_ROLLBACK ( xid IN DBMS_XA_XID) RETURN PLS_INTEGER; Parameters Table 193-9 XA_ROLLBACK Function Parameters Parameter Description xid See DBMS_XA_XID Object Type Return Values See Table 193-2 . Possible return values are: XA_OK , XA_RB *, XA_HEURHAZ , XA_HEURCOM , XA_HEURRB , or XA_HEURMIX . Usage Notes If a user needs to rollback a transaction branch that created by other users, the privilege FORCE ANY TRANSACTION must be granted to the user.