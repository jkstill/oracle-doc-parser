---
id: 19c__HTF.DIV
name: HTF.DIV
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.DIV

This function generates the <DIV> tag which creates document divisions.

## Syntax

```sql
HTF.DIV (
   calign         IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| calign | VARCHAR2 | IN | The value for the ALIGN attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.DIV ( calign IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-20 DIV Function Parameters Parameter Description calign The value for the ALIGN attribute. cattributes The other attributes to be included as-is in the tag. Examples This function generates <DIV ALIGN="calign" cattributes>