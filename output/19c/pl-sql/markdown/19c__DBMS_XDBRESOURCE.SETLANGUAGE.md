---
id: 19c__DBMS_XDBRESOURCE.SETLANGUAGE
name: DBMS_XDBRESOURCE.SETLANGUAGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.SETLANGUAGE

This procedure sets the language of the given XDBResource .

## Syntax

```sql
DBMS_XDBRESOURCE.SETLANGUAGE (
   res      IN OUT  XDBResource, 
   ACLPath  IN      VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource | IN OUT | XDBResource |
| ACLPath | VARCHAR2) | IN | New path |

## Usage Notes

Syntax DBMS_XDBRESOURCE.SETLANGUAGE ( res IN OUT XDBResource, ACLPath IN VARCHAR2); Parameters Table 200-53 SETLANGUAGE Procedure Parameters Parameter Description res XDBResource ACLPath New path