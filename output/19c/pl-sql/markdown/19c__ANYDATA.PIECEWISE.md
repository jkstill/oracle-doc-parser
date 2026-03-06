---
id: 19c__ANYDATA.PIECEWISE
name: ANYDATA.PIECEWISE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: ANYDATA
tags: [anydata]
source_file: ANYDATA-TYPE.html
---

# ANYDATA.PIECEWISE

This procedure sets the MODE of access of the current data value to be an attribute at a time (if the data value is of TYPECODE_OBJECT ).

## Syntax

```sql
MEMBER PROCEDURE PIECEWISE(
   self         IN OUT NOCOPY ANYDATA);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| self | NOCOPY | IN OUT | The current data value. |

## Usage Notes

It sets the MODE of access of the data value to be a collection element at a time (if the data value is of collection type). Once this call has been made, subsequent calls to SET* and GET* will sequentially obtain individual attributes or collection elements. Syntax MEMBER PROCEDURE PIECEWISE( self IN OUT NOCOPY ANYDATA); Parameters Table 280-7 PIECEWISE Procedure Parameters Parameter Description self The current data value. Exceptions DBMS_TYPES.INVALID_PARAMETERS DBMS_TYPES.INCORRECT_USAGE : On incorrect usage. Usage Notes The current data value must be of an OBJECT or COLLECTION type before this call can be made. Piece-wise construction and access of nested attributes that are of object or collection types is not supported.