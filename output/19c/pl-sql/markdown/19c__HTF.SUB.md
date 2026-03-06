---
id: 19c__HTF.SUB
name: HTF.SUB
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.SUB

This function generates the <SUB> and </SUB> tags which direct the browser to render the text they surround as subscript.

## Syntax

```sql
HTF.SUB(
   ctext          IN       VARCHAR2,
   calign         in       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The text to render in subscript. |
| calign | VARCHAR2 | in | The value for the ALIGN attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.SUB( ctext IN VARCHAR2, calign in VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-80 SUB Function Parameters Parameter Description ctext The text to render in subscript. calign The value for the ALIGN attribute. cattributes The other attributes to be included as-is in the tag. Examples This function generates <SUB ALIGN="calign" cattributes>ctext</SUB>