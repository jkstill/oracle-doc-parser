---
id: 19c__DBMS_XEVENT.GETPARAMETER
name: DBMS_XEVENT.GETPARAMETER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XEVENT
tags: [dbms_xevent]
source_file: DBMS_XEVENT.html
---

# DBMS_XEVENT.GETPARAMETER

This function returns the value of a request or session-specific parameter. The definition of the key parameter can be found in RFC 2616 (HTTP/1.1). They will be mapped to equivalent SQL session parameters (if any).

## Syntax

```sql
DBMS_XEVENT.GETPARAMETER (
    ev   IN   XDBRepositoryEvent,
    key  IN   VARCHAR2) 
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ev | XDBRepositoryEvent | IN | Event of XDBRepositoryEvent type |
| key | VARCHAR2) | IN | Supported parameters: ACCEPT ACCEPT-LANGUAGE ACCEPT-CHARSET ACCEPT_ENCODING |

**Returns:** `VARCHAR2`

## Usage Notes

See Also: XDBRepositoryEvent Type Subprograms for other subprograms in this group See Also: XDBRepositoryEvent Type Subprograms for other subprograms in this group Syntax DBMS_XEVENT.GETPARAMETER ( ev IN XDBRepositoryEvent, key IN VARCHAR2) RETURN VARCHAR2; Parameters Table 203-28 GETPARAMETER Function Parameters Parameter Description ev Event of XDBRepositoryEvent type key Supported parameters: ACCEPT ACCEPT-LANGUAGE ACCEPT-CHARSET ACCEPT_ENCODING