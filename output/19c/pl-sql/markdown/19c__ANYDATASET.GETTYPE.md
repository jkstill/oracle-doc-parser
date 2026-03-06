---
id: 19c__ANYDATASET.GETTYPE
name: ANYDATASET.GETTYPE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: ANYDATASET
tags: [anydataset]
source_file: ANYDATASET-TYPE.html
---

# ANYDATASET.GETTYPE

This function gets the AnyType describing the type of the data instances in an ANYDATASET .

## Syntax

```sql
MEMBER FUNCTION GETTYPE(
   self           IN ANYDATASET,
   typ            OUT NOCOPY AnyType)
   RETURN         PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| self | ANYDATASET | IN | The ANYDATASET . |
| typ | NOCOPY | OUT | The ANYTYPE corresponding to the AnyData. May be NULL if it does not represent a user-defined function. |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax MEMBER FUNCTION GETTYPE( self IN ANYDATASET, typ OUT NOCOPY AnyType) RETURN PLS_INTEGER; Parameters Table 281-8 GETTYPE Function Parameter Parameter Description self The ANYDATASET . typ The ANYTYPE corresponding to the AnyData. May be NULL if it does not represent a user-defined function. Return Values The typecode corresponding to the type of the ANYDATA .