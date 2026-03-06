---
id: 19c__ANYDATASET.GETINSTANCE
name: ANYDATASET.GETINSTANCE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: ANYDATASET
tags: [anydataset]
source_file: ANYDATASET-TYPE.html
---

# ANYDATASET.GETINSTANCE

This function gets the next instance in an ANYDATASET . Only sequential access to the instances in an ANYDATASET is allowed.

## Syntax

```sql
MEMBER FUNCTION GETINSTANCE(
   self           IN OUT NOCOPY ANYDATASET)
   RETURN         PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| self | NOCOPY | IN OUT | The ANYDATASET being accessed. |

**Returns:** `PLS_INTEGER`

## Usage Notes

After this function has been called, the GET* functions can be invoked on the ANYDATASET to access the current instance. If PIECEWISE is called before doing the GET* calls, the individual attributes (or collection elements) can be accessed. It is an error to invoke this function before the ANYDATASET is fully created. Syntax MEMBER FUNCTION GETINSTANCE( self IN OUT NOCOPY ANYDATASET) RETURN PLS_INTEGER; Parameters Table 281-7 GETINSTANCE Function Parameter Parameter Description self The ANYDATASET being accessed. Return Values DBMS_TYPES.SUCCESS or DBMS_TYPES.NO_DATA DBMS_TYPES.NO_DATA signifies the end of the ANYDATASET (all instances have been accessed). Usage Notes This function should be called even before accessing the first instance.