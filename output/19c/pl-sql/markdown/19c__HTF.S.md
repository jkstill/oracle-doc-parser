---
id: 19c__HTF.S
name: HTF.S
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.S

This function generates the <S> and </S> tags which direct the browser to render the text they surround in strikethrough type.

## Syntax

```sql
HTF.S (
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

This performs the same operation as STRIKE Function . Syntax HTF.S ( ctext IN VARCHAR2, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-73 S Function Parameters Parameter Description ctext The text to be rendered in strikethrough type. cattributes The other attributes to be included as-is in the tag. Examples This function generates <S cattributes>ctext</S>