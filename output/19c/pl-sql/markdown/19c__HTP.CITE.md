---
id: 19c__HTP.CITE
name: HTP.CITE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.CITE

This procedure generates the <CITE> and </CITE> tags which direct the browser to render the text as a citation.

## Syntax

```sql
HTP.CITE (
   ctext          IN       VARCHAR2,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The text to render as citation. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

Syntax HTP.CITE ( ctext IN VARCHAR2, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-16 CITE Procedure Parameters Parameter Description ctext The text to render as citation. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <CITE cattributes > ctext </CITE>