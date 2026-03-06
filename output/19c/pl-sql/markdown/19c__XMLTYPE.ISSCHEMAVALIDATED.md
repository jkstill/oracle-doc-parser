---
id: 19c__XMLTYPE.ISSCHEMAVALIDATED
name: XMLTYPE.ISSCHEMAVALIDATED
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: XMLTYPE
tags: [xmltype]
source_file: XMLTYPE.html
---

# XMLTYPE.ISSCHEMAVALIDATED

This member function returns the validation status of the XMLType instance to tell if a schema-based instance has been actually validated against its schema. It returns 1 if the instance has been validated against the schema, 0 otherwise.

## Syntax

```sql
MEMBER FUNCTION isSchemaValidated
return NUMBER deterministic;
```

**Returns:** `NUMBER`

## Usage Notes

MEMBER FUNCTION isSchemaValidated return NUMBER deterministic;