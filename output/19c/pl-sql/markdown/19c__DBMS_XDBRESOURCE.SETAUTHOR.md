---
id: 19c__DBMS_XDBRESOURCE.SETAUTHOR
name: DBMS_XDBRESOURCE.SETAUTHOR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.SETAUTHOR

This procedure sets the author of the given XDBResource to the specified string.

## Syntax

```sql
DBMS_XDBRESOURCE.SETAUTHOR (
   res     IN OUT  XDBResource, 
   author  IN      VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource | IN OUT | XDBResource |
| author | VARCHAR2) | IN | Author |

## Usage Notes

Syntax DBMS_XDBRESOURCE.SETAUTHOR ( res IN OUT XDBResource, author IN VARCHAR2); Parameters Table 200-46 SETAUTHOR Procedure Parameters Parameter Description res XDBResource author Author