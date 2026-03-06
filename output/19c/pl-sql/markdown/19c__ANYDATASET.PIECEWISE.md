---
id: 19c__ANYDATASET.PIECEWISE
name: ANYDATASET.PIECEWISE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: ANYDATASET
tags: [anydataset]
source_file: ANYDATASET-TYPE.html
---

# ANYDATASET.PIECEWISE

This procedure sets the MODE of construction, access of the data value to be an attribute at a time (if the data value is of TYPECODE_OBJECT ).

## Syntax

```sql
MEMBER PROCEDURE PIECEWISE(
   self         IN OUT NOCOPY ANYDATASET);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| self | NOCOPY | IN OUT | The ANYDATASET being constructed. |

## Usage Notes

It sets the MODE of construction, access of the data value to be a collection element at a time (if the data value is of a collection TYPE ). Once this call has been made, subsequent SET* and GET* calls will sequentially obtain individual attributes or collection elements. Syntax MEMBER PROCEDURE PIECEWISE( self IN OUT NOCOPY ANYDATASET); Parameters Table 281-10 PIECEWISE Procedure Parameter Parameter Description self The ANYDATASET being constructed. Exceptions DBMS_TYPES.INVALID_PARAMETERS : Invalid parameters. DBMS_TYPES.INCORRECT_USAGE : On incorrect usage. Usage Notes The current data value must be of an object or collection type before this call can be made. There is no support for piece-wise construction or access of embedded object type attributes or nested collections.