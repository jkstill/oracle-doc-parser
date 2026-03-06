---
id: 19c__HTP.SMALL
name: HTP.SMALL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.SMALL

This procedure generates the <SMALL> and </SMALL> tags, which direct the browser to render the text they surround using a small font.

## Syntax

```sql
HTP.SMALL (
   ctext          IN       VARCHAR2,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The text to be rendered in small font. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

Syntax HTP.SMALL ( ctext IN VARCHAR2, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-76 SMALL Procedure Parameters Parameter Description ctext The text to be rendered in small font. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <SMALL cattributes > ctext </SMALL>