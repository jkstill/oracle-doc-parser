---
id: 19c__HTP.FORMSELECTCLOSE
name: HTP.FORMSELECTCLOSE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.FORMSELECTCLOSE

This procedure generates the </SELECT> tag which marks the end of a Select form element.

## Syntax

```sql
HTP.FORMSELECTCLOSE;
```

## Usage Notes

A Select form element is a listbox where the user selects one or more values. You mark the beginning of Select form element by means of the FORMSELECTOPEN Procedure .The values are inserted using FORMSELECTOPTION Procedure . Syntax HTP.FORMSELECTCLOSE; Examples This procedure generates </SELECT> as shown under Examples of the FORMSELECTOPEN Procedure .