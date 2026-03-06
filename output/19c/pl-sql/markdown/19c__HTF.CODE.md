---
id: 19c__HTF.CODE
name: HTF.CODE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.CODE

This function generates the <CODE> and </CODE> tags which direct the browser to render the text in monospace font or however "code" is defined stylistically.

## Syntax

```sql
HTF.CODE (
   ctext          IN       VARCHAR2,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The text to render as code. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.CODE ( ctext IN VARCHAR2, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-17 CODE Function Parameters Parameter Description ctext The text to render as code. cattributes The other attributes to be included as-is in the tag Examples This function generates <CODE cattributes>ctext</CODE>