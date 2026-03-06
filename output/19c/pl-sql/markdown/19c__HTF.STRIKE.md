---
id: 19c__HTF.STRIKE
name: HTF.STRIKE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.STRIKE

This function generates the <STRIKE> and </STRIKE> tags which direct the browser to render the text they surround in strikethrough type.

## Syntax

```sql
STRIKE (
   ctext          IN       VARCHAR2,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The text to be rendered in strikethrough type. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

This performs the same operation as S Function . Syntax STRIKE ( ctext IN VARCHAR2, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-77 STRIKE Function Parameters Parameter Description ctext The text to be rendered in strikethrough type. cattributes The other attributes to be included as-is in the tag. Examples This function generates <STRIKE cattributes>ctext</STRIKE>