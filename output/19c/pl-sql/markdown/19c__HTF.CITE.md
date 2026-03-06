---
id: 19c__HTF.CITE
name: HTF.CITE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.CITE

This function generates the <CITE> and </CITE> tags which direct the browser to render the text as a citation.

## Syntax

```sql
HTF.CITE (
   ctext          IN       VARCHAR2,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The text to render as citation. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.CITE ( ctext IN VARCHAR2, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-16 CITE Function Parameters Parameter Description ctext The text to render as citation. cattributes The other attributes to be included as-is in the tag. Examples This function generates <CITE cattributes>ctext</CITE>