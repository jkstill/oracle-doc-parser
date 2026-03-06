---
id: 19c__HTF.FRAMESETCLOSE
name: HTF.FRAMESETCLOSE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.FRAMESETCLOSE

This function generates the </FRAMESET> tag which ends a frameset section.

## Syntax

```sql
HTF.FRAMESETCLOSE
  RETURN VARCHAR2;
```

**Returns:** `VARCHAR2`

## Usage Notes

You mark the beginning of a frameset section by means of the FRAMESETOPEN Function . Syntax HTF.FRAMESETCLOSE RETURN VARCHAR2; Examples This function generates </FRAMESET>