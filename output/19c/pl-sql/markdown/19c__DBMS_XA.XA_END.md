---
id: 19c__DBMS_XA.XA_END
name: DBMS_XA.XA_END
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XA
tags: [dbms_xa]
source_file: DBMS_XA.html
---

# DBMS_XA.XA_END

This function disassociates the current session from the transaction branch specified by xid .

## Syntax

```sql
DBMS_XA.XA_END (
   xid   IN  DBMS_XA_XID,
   flag  IN  PLS_INTEGER)
RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xid | DBMS_XA_XID | IN | See DBMS_XA_XID Object Type |
| flag | PLS_INTEGER) | IN | See Table 193-1 . |

**Returns:** `PLS_INTEGER`

## Usage Notes

A transaction manager calls XA_END when a thread of control finishes, or needs to suspend work on, a transaction branch. This occurs when the application completes a portion of its work, either partially or in its entirety (for example, before blocking on some event in order to let other threads of control work on the branch). When XA_END successfully returns, the calling thread of control is no longer actively associated with the branch but the branch still exists Syntax DBMS_XA.XA_END ( xid IN DBMS_XA_XID, flag IN PLS_INTEGER) RETURN PLS_INTEGER; Parameters Table 193-6 XA_END Function Parameters Parameter Description xid See DBMS_XA_XID Object Type flag See Table 193-1 . Return Values See Table 193-2 . Possible return values in error are XAER_RMERR , XAER_RMFAILED , XAER_NOTA , XAER_INVAL , XAER_PROTO , or XA_RB *. Usage Notes TMSUCCESS or TMSUSPEND may be specified in flag, and the transaction branch is disassociated with the current session in detached state if the return value is XA_OK . TMFAIL is not supported. XA_END may be called with either TMSUCCESS or TMSUSPEND to disassociate the transaction branch identified by xid from the current session. XA_OK is returned if XA_END succeeds. An application must check the return value and handle error cases. Only when XA_OK is returned, the application should proceed for other normal operations. Executing a ROLLBACK statement without calling XA_END first will rollback the changes made by the current transaction. However, the transaction context is still associated with the current session until XA_END is called. Executing a COMMIT statement without calling XA_END first will result in ORA - 02089 : COMMIT is not allowed in a subordinate session. Executing a COMMIT or a ROLLBACK statement after XA_END has no effect on the transaction identified by xid , since this transaction is no longer associated with the current session.