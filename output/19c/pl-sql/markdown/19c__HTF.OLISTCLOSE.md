---
id: 19c__HTF.OLISTCLOSE
name: HTF.OLISTCLOSE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.OLISTCLOSE

This function generates the </OL> tag which defines the end of an ordered list. An ordered list presents a list of numbered items.

## Syntax

```sql
HTF.OLISTCLOSE
  RETURN VARCHAR2;
```

**Returns:** `VARCHAR2`

## Usage Notes

To mark the beginning of a list of this kind, use the OLISTOPEN Function . Numbered items are added using LISTITEM Function . Syntax HTF.OLISTCLOSE RETURN VARCHAR2; Examples This function generates </OL>