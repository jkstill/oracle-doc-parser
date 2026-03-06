---
id: 19c__HTP.STRONG
name: HTP.STRONG
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.STRONG

This procedure generates the <STRONG> and </STRONG> tags which direct the browser to render the text they surround in bold, or however "strong" is defined.

## Syntax

```sql
HTP.STRONG(
   ctext          IN       VARCHAR2,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The text to be emphasized. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

Syntax HTP.STRONG( ctext IN VARCHAR2, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-78 STRONG Procedure Parameters Parameter Description ctext The text to be emphasized. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <STRONG cattributes > ctext </STRONG>