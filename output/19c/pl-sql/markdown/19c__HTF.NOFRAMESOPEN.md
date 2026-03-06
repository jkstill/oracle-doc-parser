---
id: 19c__HTF.NOFRAMESOPEN
name: HTF.NOFRAMESOPEN
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.NOFRAMESOPEN

This function generates the <NOFRAMES> tag which mark the beginning of a no-frames section.

## Syntax

```sql
HTF.NOFRAMESOPEN
  RETURN VARCHAR2;
```

**Returns:** `VARCHAR2`

## Usage Notes

To mark the end of a no-frames section, use the FRAMESETCLOSE Function . See also FRAME Function , FRAMESETOPEN Function and FRAMESETCLOSE Function . Syntax HTF.NOFRAMESOPEN RETURN VARCHAR2; Examples This function generates <NOFRAMES>