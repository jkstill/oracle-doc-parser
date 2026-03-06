---
id: 19c__HTF.TABLECAPTION
name: HTF.TABLECAPTION
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.TABLECAPTION

This function generates the <CAPTION> and </CAPTION> tags which place a caption in an HTML table.

## Syntax

```sql
HTF.TABLECAPTION(
   ccaption       IN       VARCHAR2,
   calign         in       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext |  |  | The text for the caption. |
| calign | VARCHAR2 | in | The value for the ALIGN attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.TABLECAPTION( ccaption IN VARCHAR2, calign in VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-82 TABLECAPTION Function Parameters Parameter Description ctext The text for the caption. calign The value for the ALIGN attribute. cattributes The other attributes to be included as-is in the tag. Examples This function generates <CAPTION ALIGN="calign" cattributes>ccaption</CAPTION>