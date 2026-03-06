---
id: 19c__HTP.CODE
name: HTP.CODE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.CODE

This procedure generates the <CODE> and </CODE> tags which direct the browser to render the text in monospace font or however "code" is defined stylistically.

## Syntax

```sql
HTP.CODE (
   ctext          IN       VARCHAR2,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The text to render as code. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag |

## Usage Notes

Syntax HTP.CODE ( ctext IN VARCHAR2, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-17 CODE Procedure Parameters Parameter Description ctext The text to render as code. cattributes The other attributes to be included as-is in the tag Examples This procedure generates <CODE cattributes > ctext </CODE>