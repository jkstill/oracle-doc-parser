---
id: 19c__HTP.BOLD
name: HTP.BOLD
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.BOLD

This procedure generates the <B> and </B> tags which direct the browser to display the text in boldface.

## Syntax

```sql
HTP.BOLD (
   ctext          IN       VARCHAR2,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The text that goes between the tags. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

Syntax HTP.BOLD ( ctext IN VARCHAR2, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-13 BOLD Procedure Parameters Parameter Description ctext The text that goes between the tags. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <B cattributes > ctext </B>