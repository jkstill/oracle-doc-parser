---
id: 19c__HTP.DLISTCLOSE
name: HTP.DLISTCLOSE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.DLISTCLOSE

This procedure generates the </DL> tag which ends a definition list. You start a definition list by means of the DLISTOPEN Procedure.

## Syntax

```sql
HTP.DLISTCLOSE;
```

## Usage Notes

Syntax HTP.DLISTCLOSE; Usage Notes A definition list looks like a glossary: it contains terms and definitions. Terms are inserted using the DLISTTERM Procedure and definitions are inserted using the DLISTDEF Procedure . Examples This procedure generates </DL>