---
id: 19c__HTF.ITALIC
name: HTF.ITALIC
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.ITALIC

This function generates the <I> and </I> tags which direct the browser to render the text in italics.

## Syntax

```sql
HTF.ITALIC(
   ctext          IN       VARCHAR2,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The text to be rendered in italics. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.ITALIC( ctext IN VARCHAR2, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-53 ITALIC Function Parameters Parameter Description ctext The text to be rendered in italics. cattributes The other attributes to be included as-is in the tag. Examples This function generates <I cattributes>ctext</I>