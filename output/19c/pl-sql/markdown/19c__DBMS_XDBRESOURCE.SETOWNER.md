---
id: 19c__DBMS_XDBRESOURCE.SETOWNER
name: DBMS_XDBRESOURCE.SETOWNER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.SETOWNER

This procedure sets the owner of the given XDBResource.

## Syntax

```sql
DBMS_XDBRESOURCE.SETOWNER (
   res      IN OUT  XDBResource, 
   owner    IN      VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource | IN OUT | XDBResource |
| owner | VARCHAR2) | IN | New owner |

## Usage Notes

Syntax DBMS_XDBRESOURCE.SETOWNER ( res IN OUT XDBResource, owner IN VARCHAR2); Parameters Table 200-54 SETOWNER Procedure Parameters Parameter Description res XDBResource owner New owner Usage Notes The user must have the XDBADMIN privilege to call this subprogram.