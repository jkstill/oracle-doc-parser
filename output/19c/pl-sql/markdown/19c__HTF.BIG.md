---
id: 19c__HTF.BIG
name: HTF.BIG
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.BIG

This function generates the <BIG> and </BIG> tags which direct the browser to render the text in a bigger font.

## Syntax

```sql
HTF.BIG (
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

Syntax HTF.BIG ( ctext IN VARCHAR2, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-10 BIG Function Parameters Parameter Description ctext The text that goes between the tags. cattributes The other attributes to be included as-is in the tag. Examples This function generates <BIG cattributes>ctext</BIG>