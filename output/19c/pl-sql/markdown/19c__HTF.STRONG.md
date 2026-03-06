---
id: 19c__HTF.STRONG
name: HTF.STRONG
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.STRONG

This function generates the <STRONG> and </STRONG> tags which direct the browser to render the text they surround in bold, or however "strong" is defined.

## Syntax

```sql
HTF.STRONG(
   ctext          IN       VARCHAR2,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The text to be emphasized. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.STRONG( ctext IN VARCHAR2, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-78 STRONG Function Parameters Parameter Description ctext The text to be emphasized. cattributes The other attributes to be included as-is in the tag. Examples This function generates <STRONG cattributes>ctext</STRONG>