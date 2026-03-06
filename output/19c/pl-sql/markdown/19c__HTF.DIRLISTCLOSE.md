---
id: 19c__HTF.DIRLISTCLOSE
name: HTF.DIRLISTCLOSE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.DIRLISTCLOSE

This function generates the </DIR> tag which ends a directory list section. You start a directory list section with the DIRLISTOPEN Function.

## Syntax

```sql
HTF.DIRLISTCLOSE
  RETURN VARCHAR2;
```

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.DIRLISTCLOSE RETURN VARCHAR2; Usage Notes A directory list presents a list of items that contains up to 20 characters. Items in this list are typically arranged in columns, 24 characters wide. Insert the <LI> tag directly or invoke the LISTITEM Function so that the <LI> tag appears directly after the </DIR> tag to define the items as a list. Examples This function generates </DIR>