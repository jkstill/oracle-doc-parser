---
id: 19c__HTP.SUP
name: HTP.SUP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.SUP

This procedure generates the <SUP> and </SUP> tags which direct the browser to render the text they surround as superscript.

## Syntax

```sql
HTP.SUP(
   ctext          IN       VARCHAR2,
   calign         in       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The text to render in superscript. |
| calign | VARCHAR2 | in | The value for the ALIGN attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

Syntax HTP.SUP( ctext IN VARCHAR2, calign in VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-81 SUP Procedure Parameters Parameter Description ctext The text to render in superscript. calign The value for the ALIGN attribute. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <SUP ALIGN=" calign " cattributes > ctext </SUP>