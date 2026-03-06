---
id: 19c__HTP.S
name: HTP.S
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.S

This procedure generates the <S> and </S> tags which direct the browser to render the text they surround in strikethrough type.

## Syntax

```sql
HTP.S (
   ctext          IN       VARCHAR2,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The text to be rendered in strikethrough type. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

This performs the same operation as STRIKE Procedure . Syntax HTP.S ( ctext IN VARCHAR2, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-73 S Procedure Parameters Parameter Description ctext The text to be rendered in strikethrough type. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <S cattributes > ctext </S>