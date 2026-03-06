---
id: 19c__XMLTYPE.GETNUMBERVAL
name: XMLTYPE.GETNUMBERVAL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: XMLTYPE
tags: [xmltype]
source_file: XMLTYPE.html
---

# XMLTYPE.GETNUMBERVAL

This is a member function. It returns a numeric value, formatted from the text value pointed to by the XMLType instance. The XMLType must point to a valid text node that contains a numerical value.

## Syntax

```sql
MEMBER FUNCTION getNumberVal()
RETURN number deterministic;
```

**Returns:** `number`

## Usage Notes

The options are described in the following table. MEMBER FUNCTION getNumberVal() RETURN number deterministic;