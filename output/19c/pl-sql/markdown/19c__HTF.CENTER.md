---
id: 19c__HTF.CENTER
name: HTF.CENTER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.CENTER

This function generates the <CENTER> and </CENTER> tags which center a section of text within a Web page.

## Syntax

```sql
HTF.CENTER (
   ctext          IN       VARCHAR2)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2) | IN | The text that goes between the tags. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.CENTER ( ctext IN VARCHAR2) RETURN VARCHAR2; Parameters Table 220-15 CENTER Parameters Parameter Description ctext The text that goes between the tags. Examples This function generates <CENTER>ctext</CENTER>