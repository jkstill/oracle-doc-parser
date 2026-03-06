---
id: 19c__DBMS_XDBRESOURCE.GETACLDOCFROMRES
name: DBMS_XDBRESOURCE.GETACLDOCFROMRES
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.GETACLDOCFROMRES

This function returns the ACL Document for the given resource as XMLType .

## Syntax

```sql
DBMS_XDBRESOURCE.GETACLDOCFROMRES (
   res   IN    XDBResource) 
 RETURN SYS.XMLTYPE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource) | IN | XDBResource |

**Returns:** `SYS.XMLTYPE`

## Usage Notes

Syntax DBMS_XDBRESOURCE.GETACLDOCFROMRES ( res IN XDBResource) RETURN SYS.XMLTYPE; Parameters Table 200-4 GETACLDOCFROMRES Function Parameters Parameter Description res XDBResource