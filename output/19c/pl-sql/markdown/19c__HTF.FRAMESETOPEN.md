---
id: 19c__HTF.FRAMESETOPEN
name: HTF.FRAMESETOPEN
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.FRAMESETOPEN

This function generates the <FRAMESET> tag which define a frameset section.

## Syntax

```sql
HTF.FRAMESETOPEN(
   crows          IN       VARCHAR2   DEFAULT NULL,
   ccols          IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| crows | VARCHAR2 | IN | The value for the ROWS attribute. |
| ccols | VARCHAR2 | IN | The value for the COLS attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

You mark the end of a frameset section by means of the FRAMESETCLOSE Function . Syntax HTF.FRAMESETOPEN( crows IN VARCHAR2 DEFAULT NULL, ccols IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-47 FRAMESETOPEN Function Parameters Parameter Description crows The value for the ROWS attribute. ccols The value for the COLS attribute. cattributes The other attributes to be included as-is in the tag. Examples This function generates <FRAMESET ROWS="crows" COLS="ccols" cattributes>