---
id: 19c__ANYDATA.GETTYPENAME
name: ANYDATA.GETTYPENAME
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: ANYDATA
tags: [anydata]
source_file: ANYDATA-TYPE.html
---

# ANYDATA.GETTYPENAME

This function gets the fully qualified type name for the ANYDATA .

## Syntax

```sql
MEMBER FUNCTION GETTYPENAME(
   self         IN ANYDATA)
   RETURN       VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| self | ANYDATA) | IN | An ANYDATA . |

**Returns:** `VARCHAR2`

## Usage Notes

If the ANYDATA is based on a built-in type, this function will return NUMBER and other relevant information. If it is based on a user defined type, this function will return schema_name . type_name , for example, SCOTT.FOO. If it is based on a transient anonymous type, this function will return NULL. Syntax MEMBER FUNCTION GETTYPENAME( self IN ANYDATA) RETURN VARCHAR2; Parameters Table 280-6 GETTYPENAME Function Parameter Parameter Description self An ANYDATA . Return Values Type name of the ANYDATA .