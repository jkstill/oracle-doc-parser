---
id: 19c__HTF.SUP
name: HTF.SUP
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.SUP

This function generates the <SUP> and </SUP> tags which direct the browser to render the text they surround as superscript.

## Syntax

```sql
HTF.SUP(
   ctext          IN       VARCHAR2,
   calign         in       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The text to render in superscript. |
| calign | VARCHAR2 | in | The value for the ALIGN attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.SUP( ctext IN VARCHAR2, calign in VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-81 SUP Function Parameters Parameter Description ctext The text to render in superscript. calign The value for the ALIGN attribute. cattributes The other attributes to be included as-is in the tag. Examples This function generates <SUP ALIGN="calign" cattributes>ctext</SUP>