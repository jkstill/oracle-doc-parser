---
id: 19c__HTF.FONTCLOSE
name: HTF.FONTCLOSE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.FONTCLOSE

This function generates the </FONT> tag which marks the end of a section of text with the specified font characteristics.

## Syntax

```sql
HTF.FONTCLOSE
  RETURN VARCHAR2;
```

**Returns:** `VARCHAR2`

## Usage Notes

You mark the beginning of the section text by means of the FONTOPEN Function . Syntax HTF.FONTCLOSE RETURN VARCHAR2; Examples This function generates </FONT>