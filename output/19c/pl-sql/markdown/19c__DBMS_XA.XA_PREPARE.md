---
id: 19c__DBMS_XA.XA_PREPARE
name: DBMS_XA.XA_PREPARE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XA
tags: [dbms_xa]
source_file: DBMS_XA.html
---

# DBMS_XA.XA_PREPARE

This function prepares the transaction branch specified in xid for committing the transaction subsequently if possible.

## Syntax

```sql
DBMS_XA.XA_PREPARE (
   xid   IN  DBMS_XA_XID)
RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xid | DBMS_XA_XID) | IN | See DBMS_XA_XID Object Type |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax DBMS_XA.XA_PREPARE ( xid IN DBMS_XA_XID) RETURN PLS_INTEGER; Parameters Table 193-8 XA_PREPARE Function Parameters Parameter Description xid See DBMS_XA_XID Object Type Return Values See Table 193-2 . Possible return codes include: XA_OK , XA_RDONLY , XA_RB *, XAER_RMERR , XAER_RMFAIL , XAER_NOTA , XAER_INVAL , or XAER_PROTO . Usage Notes If a user needs to prepare a transaction branch that is created by other users, FORCE ANY TRANSACTION must be granted to the user. An application must keep track of all the branches of one global transaction, and prepare each transaction branch. Only if all branches of the global transaction have been prepared successfully and XA_PREPARE has returned XA_OK , the application may proceed to call XA_COMMIT .