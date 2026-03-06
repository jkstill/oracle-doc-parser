---
id: 19c__DBMS_XMLSAVE.NEWCONTEXT
name: DBMS_XMLSAVE.NEWCONTEXT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSAVE
tags: [dbms_xmlsave]
source_file: DBMS_XMLSAVE.html
---

# DBMS_XMLSAVE.NEWCONTEXT

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

Syntax FUNCTION newContext( targetTable IN VARCHAR2) RETURN ctxType; Parameters Table 209-11 NEWCONTEXT Function Parameters Parameter IN / OUT Description targetTable (IN) The target table into which to load the XML document.