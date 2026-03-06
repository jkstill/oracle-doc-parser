---
id: 19c__DBMS_XA.XA_START
name: DBMS_XA.XA_START
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XA
tags: [dbms_xa]
source_file: DBMS_XA.html
---

# DBMS_XA.XA_START

This function associates the current session with a transaction branch specified by the xid .

## Syntax

```sql
DBMS_XA.XA_START (
   xid   IN  DBMS_XA_XID,    flag  IN  PLS_INTEGER)  RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xid | DBMS_XA_XID | IN | See DBMS_XA_XID Object Type |
| flag | PLS_INTEGER) | IN | See Table 193-1 . |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax DBMS_XA.XA_START ( xid IN DBMS_XA_XID, flag IN PLS_INTEGER) RETURN PLS_INTEGER; Parameters Table 193-11 XA_START Function Parameters Parameter Description xid See DBMS_XA_XID Object Type flag See Table 193-1 . Return Values See Table 193-2 Usage Notes If TMJOIN or TMRESUME is specified in flag, the start is for joining an existing transaction branch identified by the xid . TMJOIN flag should be used when the transaction is detached with TMSUCCESS flag. TMRESUME should be used when the transaction branch is detached with TMSUSPEND flag. XA_START may be called with either flag to join an existing transaction branch. If TMNOFLAGS is specified in flag, and neither TMJOIN nor TMRESUME is specified, a new transaction branch is to be started. If the transaction branch specified in xid already exists, XA_START returns an XAER_DUPID error code. Possible return values in error include: XAER_RMERR , XAER_RMFAIL , XAER_DUPID , XAER_OUTSIDE , XAER_NOTA , XAER_INVAL , and XAER_PROTO . XA_OK is returned if XA_START succeeds. An application must check the return value and handle error cases. Only when XA_OK is returned, the PL/SQL application should proceed for other normal operations. Transaction stacking is not supported. If there is an active transaction associated with the current session, may not be called to start or join another transaction. XAER_PROTO will be returned if XA_START is called with an active global transaction branch associated with the session. XAER_OUTSIDE will be returned if XA_START is called with a local transaction associated with the current session.