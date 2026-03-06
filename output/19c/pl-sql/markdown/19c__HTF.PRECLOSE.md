---
id: 19c__HTF.PRECLOSE
name: HTF.PRECLOSE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.PRECLOSE

This function generates the </PRE> tag which marks the end of a section of preformatted text in the body of the HTML page.

## Syntax

```sql
HTF.PRECLOSE
  RETURN VARCHAR2;
```

**Returns:** `VARCHAR2`

## Usage Notes

To mark the beginning of a section of preformatted text in the body of the HTML page, use the PREOPEN Function . Syntax HTF.PRECLOSE RETURN VARCHAR2; Examples This function generates </PRE>