---
id: 19c__DBMS_XMLSTORE.NEWCONTEXT
name: DBMS_XMLSTORE.NEWCONTEXT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSTORE
tags: [dbms_xmlstore]
source_file: DBMS_XMLSTORE.html
---

# DBMS_XMLSTORE.NEWCONTEXT

NEWCONTEXT creates a save context and returns the context handle.

## Syntax

```sql
FUNCTION newContext(
   targetTable IN VARCHAR2)
RETURN ctxType;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| targetTable | VARCHAR2) | IN | (IN) |

**Returns:** `ctxType`

## Usage Notes

FUNCTION newContext( targetTable IN VARCHAR2) RETURN ctxType;