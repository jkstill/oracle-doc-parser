---
id: 19c__ANYDATASET.GETCOUNT
name: ANYDATASET.GETCOUNT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: ANYDATASET
tags: [anydataset]
source_file: ANYDATASET-TYPE.html
---

# ANYDATASET.GETCOUNT

This function gets the number of data instances in an ANYDATASET .

## Syntax

```sql
MEMBER FUNCTION GetCount(
   self        IN ANYDATASET) 
   RETURN      PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| self | ANYDATASET) | IN | The ANYDATASET being accessed. |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax MEMBER FUNCTION GetCount( self IN ANYDATASET) RETURN PLS_INTEGER; Parameter Table 281-6 GETCOUNT Function Parameter Parameter Description self The ANYDATASET being accessed. Return Values The number of data instances.