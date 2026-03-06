---
id: 19c__HTF.MAPCLOSE
name: HTF.MAPCLOSE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.MAPCLOSE

This function generates the </MAP> tag which marks the end of a set of regions in a client-side image map

## Syntax

```sql
HTF.MAPCLOSE
  RETURN VARCHAR2;
```

**Returns:** `VARCHAR2`

## Usage Notes

. To mark the beginning of a set of regions in a client-side image map, use the MAPOPEN Function . Syntax HTF.MAPCLOSE RETURN VARCHAR2; Examples This function generates </MAP>