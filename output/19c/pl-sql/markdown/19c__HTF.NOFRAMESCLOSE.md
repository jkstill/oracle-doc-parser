---
id: 19c__HTF.NOFRAMESCLOSE
name: HTF.NOFRAMESCLOSE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.NOFRAMESCLOSE

This function generates the </NOFRAMES> tag which marks the end of a no-frames section.

## Syntax

```sql
HTF.NOFRAMESCLOSE
  RETURN VARCHAR2;
```

**Returns:** `VARCHAR2`

## Usage Notes

To mark the beginning of a no-frames section, use the FRAMESETOPEN Function . See also FRAME Function , FRAMESETOPEN Function and FRAMESETCLOSE Function . Syntax HTF.NOFRAMESCLOSE RETURN VARCHAR2; Examples This function generates </NOFRAMES>