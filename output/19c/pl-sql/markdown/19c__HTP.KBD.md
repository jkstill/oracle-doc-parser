---
id: 19c__HTP.KBD
name: HTP.KBD
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.KBD

This procedure generates the <KBD> and </KBD> tags which direct the browser to render the text in monospace font.

## Syntax

```sql
HTP.KBD(
   ctext          IN       VARCHAR2,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The text to be rendered in monospace. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

This subprogram performs the same operation as the KEYBOARD Procedure . Syntax HTP.KBD( ctext IN VARCHAR2, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-52 KBD Procedure Parameters Parameter Description ctext The text to be rendered in monospace. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <KBD cattributes > ctext </KBD>