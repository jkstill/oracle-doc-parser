---
id: 19c__HTP.BIG
name: HTP.BIG
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.BIG

This procedure generates the <BIG> and </BIG> tags which direct the browser to render the text in a bigger font.

## Syntax

```sql
HTP.BIG (
   ctext          IN       VARCHAR2,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The the text that goes between the tags. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

Syntax HTP.BIG ( ctext IN VARCHAR2, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-10 BIG Procedure Parameters Parameter Description ctext The the text that goes between the tags. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <BIG cattributes > ctext </BIG>