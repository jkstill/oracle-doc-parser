---
id: 19c__HTP.PLAINTEXT
name: HTP.PLAINTEXT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.PLAINTEXT

This procedure generates the <PLAINTEXT> and </PLAINTEXT> tags which direct the browser to render the text they surround in fixed-width type.

## Syntax

```sql
HTP.PLAINTEXT(
   ctext          IN       VARCHAR2,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The text to be rendered in fixed-width font. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

Syntax HTP.PLAINTEXT( ctext IN VARCHAR2, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-67 PLAINTEXT Procedure Parameters Parameter Description ctext The text to be rendered in fixed-width font. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <PLAINTEXT cattributes > ctext </PLAINTEXT>