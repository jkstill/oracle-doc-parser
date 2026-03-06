---
id: 19c__DBMS_XA.XA_SETTIMEOUT
name: DBMS_XA.XA_SETTIMEOUT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XA
tags: [dbms_xa]
source_file: DBMS_XA.html
---

# DBMS_XA.XA_SETTIMEOUT

This function sets the transaction timeout in seconds for the current session.

## Syntax

```sql
DBMS_XA.XA_SETTIMEOUT (
   seconds  IN  PLS_INTEGER)
RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| seconds | PLS_INTEGER) | IN | The timeout value indicates the maximum time in seconds that a transaction branch may be disassociated from the session before the system automatically aborts the transaction. The default value is 60 seconds. |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax DBMS_XA.XA_SETTIMEOUT ( seconds IN PLS_INTEGER) RETURN PLS_INTEGER; Parameters Table 193-10 XA_SETTIMEOUT Function Parameters Parameter Description seconds The timeout value indicates the maximum time in seconds that a transaction branch may be disassociated from the session before the system automatically aborts the transaction. The default value is 60 seconds. Return Values See Table 193-2 . Possible return values are XA_OK , XAER_RMERR , XAER_RMFAIL , or XAER_INVAL . Usage Notes Only if return value is XA_OK , is the timeout value successfully set.