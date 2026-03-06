---
id: 19c__XMLTYPE.GETNAMESPACE
name: XMLTYPE.GETNAMESPACE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: XMLTYPE
tags: [xmltype]
source_file: XMLTYPE.html
---

# XMLTYPE.GETNAMESPACE

GETNAMESPACE is a member function. It returns the namespace of the top level element in the instance. It returns NULL if the input is a fragment or is a non-schema based instance.

## Syntax

```sql
MEMBER FUNCTION getNamespace
return varchar2 deterministic;
```

**Returns:** `varchar2`

## Usage Notes

MEMBER FUNCTION getNamespace return varchar2 deterministic;