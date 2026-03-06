---
id: 19c__HTP.MENULISTCLOSE
name: HTP.MENULISTCLOSE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.MENULISTCLOSE

This procedure generates the </MENU> tag which ends a list that presents one line for each item.

## Syntax

```sql
HTP.MENULISTCLOSE;
```

## Usage Notes

To begin a list of this kind, use the MENULISTOPEN Procedure . The items in the list appear more compact than an unordered list. The LISTITEM Procedure defines the list items in a menu list. Syntax HTP.MENULISTCLOSE; Examples This procedure generates </MENU>