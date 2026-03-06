---
id: 19c__HTP.MAPOPEN
name: HTP.MAPOPEN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.MAPOPEN

This procedure generates the <MAP> tag which mark the beginning of a set of regions in a client-side image map.

## Syntax

```sql
HTP.MAPOPEN(
   cname          IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cname | VARCHAR2 | IN | The value for the NAME attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

To mark the end of a set of regions in a client-side image map, use the MAPCLOSE Procedure . Syntax HTP.MAPOPEN( cname IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-60 MAPOPEN Procedure Parameters Parameter Description cname The value for the NAME attribute. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <MAP NAME=" cname " cattributes >