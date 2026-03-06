---
id: 19c__HTP.DIRLISTCLOSE
name: HTP.DIRLISTCLOSE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.DIRLISTCLOSE

This procedure generates the </DIR> tag which ends a directory list section. You start a directory list section with the DIRLISTOPEN Procedure.

## Syntax

```sql
HTP.DIRLISTCLOSE;
```

## Usage Notes

Syntax HTP.DIRLISTCLOSE; Usage Notes A directory list presents a list of items that contains up to 20 characters. Items in this list are typically arranged in columns, 24 characters wide. Insert the <LI> tag directly or invoke the LISTITEM Procedure so that the <LI> tag appears directly after the </DIR> tag to define the items as a list. Examples This procedure generates </DIR>