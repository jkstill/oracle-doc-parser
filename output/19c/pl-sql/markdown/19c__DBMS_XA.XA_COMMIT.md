---
id: 19c__DBMS_XA.XA_COMMIT
name: DBMS_XA.XA_COMMIT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XA
tags: [dbms_xa]
source_file: DBMS_XA.html
---

# DBMS_XA.XA_COMMIT

This function commits the global transaction specified by xid .

## Syntax

```sql
DBMS_XA.XA_COMMIT (
   xid       IN  DBMS_XA_XID,
   onePhase  IN  BOOLEAN)
RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xid | DBMS_XA_XID | IN | See DBMS_XA_XID Object Type |
| onePhase | BOOLEAN) | IN | If TRUE , apply single phase commit |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax DBMS_XA.XA_COMMIT ( xid IN DBMS_XA_XID, onePhase IN BOOLEAN) RETURN PLS_INTEGER; Parameters Table 193-5 XA_COMMIT Function Parameters Parameter Description xid See DBMS_XA_XID Object Type onePhase If TRUE , apply single phase commit Return Values See Table 193-2 . Possible return values indicating error are: XAER_RMERR , XAER_RMFAIL , XAER_NOTA , XAER_INVAL , or XAER_PROTO . Other possible return values include: XA_OK , XA_RB *, XA_HEURHAZ , XA_HEURCOM , XA_HEURRB , and XA_HEURMIX . Usage Notes An application must not call COMMIT , but instead must call XA_COMMIT to commit the global transaction specified by xid . If a user needs to commit a transaction branch that is created by other users, FORCE ANY TRANSACTION must be granted to the user. If onePhase is TRUE , the resource manager should use a one-phase commit protocol to commit the work done on behalf of xid . Otherwise, only if all branches of the global transaction have been prepared successfully and the preceding XA_PREPARE call has returned XA_OK , should XA_COMMIT be called. The application must make a separate XA_COMMIT call for each of the transaction branches of the global transaction for which XA_PREPARE has returned XA_OK . If the resource manager did not commit the transaction and the parameter onePhase is set to TRUE , the resource manager may return one of the XA_RB * code. Upon return, the resource manager has rolled back the branch's work and has released all held resources.