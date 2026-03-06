---
id: 19c__HTP.DIRLISTOPEN
name: HTP.DIRLISTOPEN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.DIRLISTOPEN

This procedure generates the <DIR> which starts a directory list section. You end a directory list section with the DIRLISTCLOSE Procedure.

## Syntax

```sql
HTP.DIRLISTOPEN;
```

## Usage Notes

Syntax HTP.DIRLISTOPEN; Usage Notes A directory list presents a list of items that contains up to 20 characters. Items in this list are typically arranged in columns, 24 characters wide. Insert the <LI> tag directly or invoke the LISTITEM Procedure so that the <LI> tag appears directly after the </DIR> tag to define the items as a list. Examples This procedure generates <DIR>