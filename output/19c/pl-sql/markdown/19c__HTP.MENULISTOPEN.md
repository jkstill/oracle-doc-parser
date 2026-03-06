---
id: 19c__HTP.MENULISTOPEN
name: HTP.MENULISTOPEN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.MENULISTOPEN

This procedure generates the <MENU> tag which begins a list that presents one line for each item.

## Syntax

```sql
HTP.MENULISTOPEN;
```

## Usage Notes

To end a list of this kind, use the MENULISTCLOSE Procedure .The items in the list appear more compact than an unordered list. The LISTITEM Procedure defines the list items in a menu list. Syntax HTP.MENULISTOPEN; Examples This procedure generates <MENU>