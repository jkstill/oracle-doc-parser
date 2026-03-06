---
id: 19c__XMLTYPE.GETCLOBVAL
name: XMLTYPE.GETCLOBVAL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: XMLTYPE
tags: [xmltype]
source_file: XMLTYPE.html
---

# XMLTYPE.GETCLOBVAL

This member function returns a CLOB containing the serialized XML representation. If the CLOB returned is temporary, it must be freed after use. The CLOBs returned by this function are read-only .

## Syntax

```sql
MEMBER FUNCTION getClobVal()
RETURN clob deterministic;
```

**Returns:** `clob`

## Usage Notes

MEMBER FUNCTION getClobVal() RETURN clob deterministic;