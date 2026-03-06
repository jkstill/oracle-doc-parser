---
id: 19c__HTF.BOLD
name: HTF.BOLD
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.BOLD

This function generates the <B> and </B> tags which direct the browser to display the text in boldface.

## Syntax

```sql
HTF.BOLD (
   ctext          IN       VARCHAR2,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The text that goes between the tags. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.BOLD ( ctext IN VARCHAR2, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-13 BOLD Function Parameters Parameter Description ctext The text that goes between the tags. cattributes The other attributes to be included as-is in the tag. Examples This function generates <B cattributes>ctext</B>