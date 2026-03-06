---
id: 19c__XMLTYPE.GETSCHEMAURL
name: XMLTYPE.GETSCHEMAURL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: XMLTYPE
tags: [xmltype]
source_file: XMLTYPE.html
---

# XMLTYPE.GETSCHEMAURL

This member function returns the XML Schema URL corresponding to the XMLType instance, if the XMLType instance is a schema-based document. Otherwise, it returns NULL .

## Syntax

```sql
MEMBER FUNCTION getSchemaURL
return varchar2 deterministic;
```

**Returns:** `varchar2`

## Usage Notes

MEMBER FUNCTION getSchemaURL return varchar2 deterministic;