---
id: 19c__XMLTYPE.ISFRAGMENT
name: XMLTYPE.ISFRAGMENT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: XMLTYPE
tags: [xmltype]
source_file: XMLTYPE.html
---

# XMLTYPE.ISFRAGMENT

ISFRAGMENT determines if the XMLType instance corresponds to a well-formed document, or a fragment. It returns 1 or 0 indicating if the XMLType instance contains a fragment or a well-formed document.

## Syntax

```sql
MEMBER FUNCTION isFragment()
RETURN number deterministic;
```

**Returns:** `number`

## Usage Notes

MEMBER FUNCTION isFragment() RETURN number deterministic;