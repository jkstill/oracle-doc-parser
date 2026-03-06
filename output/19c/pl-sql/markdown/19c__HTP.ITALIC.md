---
id: 19c__HTP.ITALIC
name: HTP.ITALIC
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.ITALIC

This procedure generates the <I> and </I> tags which direct the browser to render the text in italics.

## Syntax

```sql
HTP.ITALIC(
   ctext          IN       VARCHAR2,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The text to be rendered in italics. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

Syntax HTP.ITALIC( ctext IN VARCHAR2, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-51 ITALIC Procedure Parameters Parameter Description ctext The text to be rendered in italics. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <I cattributes > ctext </I>