---
id: 19c__HTF.KEYBOARD
name: HTF.KEYBOARD
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.KEYBOARD

This function generates the <KBD> and </KBD> tags, which direct the browser to render the text in monospace font.

## Syntax

```sql
HTF.KEYBOARD(
   ctext          IN       VARCHAR2,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The text to be rendered in monospace. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

This subprogram performs the same operation as the KBD Function . Syntax HTF.KEYBOARD( ctext IN VARCHAR2, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-55 KEYBOARD Function Parameters Parameter Description ctext The text to be rendered in monospace. cattributes The other attributes to be included as-is in the tag. Examples This function generates <KBD cattributes>ctext</KBD>