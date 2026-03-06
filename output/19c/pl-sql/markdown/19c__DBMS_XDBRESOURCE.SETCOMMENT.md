---
id: 19c__DBMS_XDBRESOURCE.SETCOMMENT
name: DBMS_XDBRESOURCE.SETCOMMENT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.SETCOMMENT

This procedure sets a comment associated with the given XDBResource.

## Syntax

```sql
DBMS_XDBRESOURCE.SETCOMMENT (
   res      IN OUT  XDBResource, 
   comment  IN      VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource | IN OUT | XDBResource |
| comment | VARCHAR2) | IN | New comment |

## Usage Notes

Syntax DBMS_XDBRESOURCE.SETCOMMENT ( res IN OUT XDBResource, comment IN VARCHAR2); Parameters Table 200-48 SETCOMMENT Procedure Parameters Parameter Description res XDBResource comment New comment