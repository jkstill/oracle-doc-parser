---
id: 19c__HTF.MENULISTCLOSE
name: HTF.MENULISTCLOSE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.MENULISTCLOSE

This function generates the </MENU> tag which ends a list that presents one line for each item.

## Syntax

```sql
HTF.MENULISTCLOSE
  RETURN VARCHAR2;
```

**Returns:** `VARCHAR2`

## Usage Notes

To begin a list of this kind, use the MENULISTOPEN Function . The items in the list appear more compact than an unordered list. The LISTITEM Function defines the list items in a menu list. Syntax HTF.MENULISTCLOSE RETURN VARCHAR2; Examples This function generates </MENU>