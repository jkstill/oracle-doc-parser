---
id: 19c__HTP.UNDERLINE
name: HTP.UNDERLINE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.UNDERLINE

This procedure generates the <U> and </U> tags, which direct the browser to render the text they surround with an underline.

## Syntax

```sql
HTP.UNDERLINE(
   ctext          IN       VARCHAR2,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The text to render with an underline. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

Syntax HTP.UNDERLINE( ctext IN VARCHAR2, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-90 UNDERLINE Procedure Parameters Parameter Description ctext The text to render with an underline. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <U cattributes > ctext </U>