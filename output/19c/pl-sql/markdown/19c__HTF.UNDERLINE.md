---
id: 19c__HTF.UNDERLINE
name: HTF.UNDERLINE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.UNDERLINE

This function generates the <U> and </U> tags, which direct the browser to render the text they surround with an underline.

## Syntax

```sql
HTF.UNDERLINE(
   ctext          IN       VARCHAR2,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The text to render with an underline. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.UNDERLINE( ctext IN VARCHAR2, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-90 UNDERLINE Function Parameters Parameter Description ctext The text to render with an underline. cattributes The other attributes to be included as-is in the tag. Examples This function generates <U cattributes>ctext</U>