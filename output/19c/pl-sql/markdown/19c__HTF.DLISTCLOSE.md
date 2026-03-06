---
id: 19c__HTF.DLISTCLOSE
name: HTF.DLISTCLOSE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.DLISTCLOSE

This function generates the </DL> tag which ends a definition list. You start a definition list by means of the DLISTOPEN Function.

## Syntax

```sql
HTF.DLISTCLOSE
  RETURN VARCHAR2;
```

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.DLISTCLOSE RETURN VARCHAR2; Usage Notes A definition list looks like a glossary: it contains terms and definitions. Terms are inserted using the DLISTTERM Function and definitions are inserted using the DLISTDEF Function . Examples This function generates </DL>