---
id: 19c__DBMS_XDBRESOURCE.SETDISPLAYNAME
name: DBMS_XDBRESOURCE.SETDISPLAYNAME
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.SETDISPLAYNAME

This procedure sets the display name of the given XDBResource.

## Syntax

```sql
DBMS_XDBRESOURCE.SETDISPLAYNAME (
   res      IN OUT  XDBResource, 
   name     IN      VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource | IN OUT | XDBResource |
| name | VARCHAR2) | IN | New display name |

## Usage Notes

Syntax DBMS_XDBRESOURCE.SETDISPLAYNAME ( res IN OUT XDBResource, name IN VARCHAR2); Parameters Table 200-52 SETDISPLAYNAME Procedure Parameters Parameter Description res XDBResource name New display name