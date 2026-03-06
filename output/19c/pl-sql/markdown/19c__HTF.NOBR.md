---
id: 19c__HTF.NOBR
name: HTF.NOBR
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.NOBR

This function generates the <NOBR> and </NOBR> tags which turn off line-breaking in a section of text.

## Syntax

```sql
HTF.NOBR(
ctext        IN        VARCHAR2)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2) | IN | The text that is to be rendered on one line. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.NOBR( ctext IN VARCHAR2) RETURN VARCHAR2; Parameters Table 220-65 NOBR Function Parameters Parameter Description ctext The text that is to be rendered on one line. Examples This function generates <NOBR>ctext</NOBR>