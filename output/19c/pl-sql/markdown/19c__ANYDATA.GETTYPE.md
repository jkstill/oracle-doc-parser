---
id: 19c__ANYDATA.GETTYPE
name: ANYDATA.GETTYPE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: ANYDATA
tags: [anydata]
source_file: ANYDATA-TYPE.html
---

# ANYDATA.GETTYPE

This function gets the typecode of the ANYDATA .

## Syntax

```sql
MEMBER FUNCTION GETTYPE(
   self          IN ANYDATA,
   typ           OUT NOCOPY AnyType)
   RETURN        PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| self | ANYDATA | IN | An ANYDATA . |
| typ | NOCOPY | OUT | The AnyType corresponding to the ANYDATA . May be NULL if it does not represent a user-defined type. |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax MEMBER FUNCTION GETTYPE( self IN ANYDATA, typ OUT NOCOPY AnyType) RETURN PLS_INTEGER; Parameters Table 280-5 GETTYPE Function Parameter Parameter Description self An ANYDATA . typ The AnyType corresponding to the ANYDATA . May be NULL if it does not represent a user-defined type. Return Values The typecode corresponding to the type of the ANYDATA .