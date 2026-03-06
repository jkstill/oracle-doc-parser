---
id: 19c__ANYDATASET.GETTYPENAME
name: ANYDATASET.GETTYPENAME
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: ANYDATASET
tags: [anydataset]
source_file: ANYDATASET-TYPE.html
---

# ANYDATASET.GETTYPENAME

This procedure gets the fully qualified type name for the ANYDATASET .

## Syntax

```sql
MEMBER FUNCTION GETTYPENAME(
   self           IN ANYDATASET)
   RETURN         VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| self | ANYDATASET) | IN | The ANYDATASET being constructed. |

**Returns:** `VARCHAR2`

## Usage Notes

If the ANYDATASET is based on a built-in, this function will return NUMBER and associated information. If it is based on a user defined type, this function will return schema_name . type_name . for example, SCOTT.FOO. If it is based on a transient anonymous type, this function will return NULL . Syntax MEMBER FUNCTION GETTYPENAME( self IN ANYDATASET) RETURN VARCHAR2; Parameter Table 281-9 GETTYPENAME Function Parameter Parameter Description self The ANYDATASET being constructed. Return Values Type name of the ANYDATASET .