---
id: 19c__DBMS_XDBRESOURCE.SETCONTENTTYPE
name: DBMS_XDBRESOURCE.SETCONTENTTYPE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.SETCONTENTTYPE

This procedure sets the content-type of the given XDBResource.

## Syntax

```sql
DBMS_XDBRESOURCE.SETCONTENTTYPE (
   res         IN OUT  XDBResource, 
   conttype    IN      VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource | IN OUT | XDBResource |
| conttype | VARCHAR2) | IN | New content-type |

## Usage Notes

Syntax DBMS_XDBRESOURCE.SETCONTENTTYPE ( res IN OUT XDBResource, conttype IN VARCHAR2); Parameters Table 200-50 SETCONTENTTYPE Procedure Parameters Parameter Description res XDBResource conttype New content-type