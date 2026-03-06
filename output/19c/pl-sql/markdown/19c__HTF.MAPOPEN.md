---
id: 19c__HTF.MAPOPEN
name: HTF.MAPOPEN
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.MAPOPEN

This function generates the <MAP> tag which mark the beginning of a set of regions in a client-side image map.

## Syntax

```sql
HTF.MAPOPEN(
   cname          IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cname | VARCHAR2 | IN | The value for the NAME attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

To mark the end of a set of regions in a client-side image map, use the MAPCLOSE Function . Syntax HTF.MAPOPEN( cname IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-62 MAPOPEN Function Parameters Parameter Description cname The value for the NAME attribute. cattributes The other attributes to be included as-is in the tag. Examples This function generates <MAP NAME="cname" cattributes>