---
id: 19c__HTF.SMALL
name: HTF.SMALL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.SMALL

This function generates the <SMALL> and </SMALL> tags, which direct the browser to render the text they surround using a small font.

## Syntax

```sql
HTF.SMALL (
   ctext          IN       VARCHAR2,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The text to be rendered in small font. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.SMALL ( ctext IN VARCHAR2, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-76 SMALL Function Parameters Parameter Description ctext The text to be rendered in small font. cattributes The other attributes to be included as-is in the tag. Examples This function generates <SMALL cattributes>ctext</SMALL>