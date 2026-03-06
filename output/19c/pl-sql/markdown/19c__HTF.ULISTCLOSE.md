---
id: 19c__HTF.ULISTCLOSE
name: HTF.ULISTCLOSE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.ULISTCLOSE

This function generates the </UL> tag which marks the end of an unordered list. An unordered list presents items with bullets.

## Syntax

```sql
HTF.ULISTCLOSE
  RETURN VARCHAR2;
```

**Returns:** `VARCHAR2`

## Usage Notes

To mark the beginning of an unordered list, use the ULISTOPEN Function . Add list items with LISTITEM Function . Syntax HTF.ULISTCLOSE RETURN VARCHAR2; Examples This function generates </UL>