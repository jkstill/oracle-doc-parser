---
id: 19c__HTF.DFN
name: HTF.DFN
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.DFN

This function generates the <DFN> and </DFN> tags which direct the browser to mark the text in italics or however "definition" is described stylistically.

## Syntax

```sql
HTF.DFN (
   ctext          IN       VARCHAR2)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2) | IN | The text to render in italics. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.DFN ( ctext IN VARCHAR2) RETURN VARCHAR2; Parameters Table 220-19 DFN Function Parameters Parameter Description ctext The text to render in italics. Examples This function generates <DFN>ctext</DFN>