---
id: 19c__HTF.FORMSELECTCLOSE
name: HTF.FORMSELECTCLOSE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.FORMSELECTCLOSE

This function generates the </SELECT> tag which marks the end of a Select form element.

## Syntax

```sql
HTF.FORMSELECTCLOSE
  RETURN VARCHAR2;
```

**Returns:** `VARCHAR2`

## Usage Notes

A Select form element is a listbox where the user selects one or more values. You mark the beginning of Select form element by means of the FORMSELECTOPEN Function .The values are inserted using FORMSELECTOPTION Function . Syntax HTF.FORMSELECTCLOSE RETURN VARCHAR2; Examples This function generates </SELECT> as shown under Examples of the FORMSELECTOPEN Function .