---
id: 19c__DBMS_XDBRESOURCE.SETCHARACTERSET
name: DBMS_XDBRESOURCE.SETCHARACTERSET
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.SETCHARACTERSET

This procedure sets the character set of the given XDBResource to a specified character set.

## Syntax

```sql
DBMS_XDBRESOURCE.SETCHARACTERSET (
   res      IN OUT  XDBResource, 
   charSet  IN      VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource | IN OUT | XDBResource |
| charset | VARCHAR2) | IN | New character set |

## Usage Notes

Syntax DBMS_XDBRESOURCE.SETCHARACTERSET ( res IN OUT XDBResource, charSet IN VARCHAR2); Parameters Table 200-47 SETCHARACTERSET Procedure Parameters Parameter Description res XDBResource charset New character set