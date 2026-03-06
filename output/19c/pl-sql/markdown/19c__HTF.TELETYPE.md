---
id: 19c__HTF.TELETYPE
name: HTF.TELETYPE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.TELETYPE

This function generates the <TT> and </TT> tags which direct the browser to render the text they surround in a fixed width typewriter font, for example, the courier font.

## Syntax

```sql
HTF.TELETYPE(
   ctext          IN       VARCHAR2,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The text to render in a fixed width typewriter font. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.TELETYPE( ctext IN VARCHAR2, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-87 TELETYPE Function Parameters Parameter Description ctext The text to render in a fixed width typewriter font. cattributes The other attributes to be included as-is in the tag. Examples This function generates <TT cattributes>ctext</TT>