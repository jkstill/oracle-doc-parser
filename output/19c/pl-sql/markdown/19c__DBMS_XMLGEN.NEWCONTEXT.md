---
id: 19c__DBMS_XMLGEN.NEWCONTEXT
name: DBMS_XMLGEN.NEWCONTEXT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLGEN
tags: [dbms_xmlgen]
source_file: DBMS_XMLGEN.html
---

# DBMS_XMLGEN.NEWCONTEXT

This function generates and returns a new context handle.

## Syntax

```sql
DBMS_XMLGEN.NEWCONTEXT ( 
      query     IN VARCHAR2) 
 RETURN ctxHandle;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| query | VARCHAR2) | IN | The query, in the form of a VARCHAR , the result of which must be converted to XML. |
| queryString |  |  | The query string in the form of a PL/SQL ref cursor, the result of which must be converted to XML. |

**Returns:** `ctxHandle`

## Usage Notes

This context handle is used in GETXML Functions and other functions to get XML back from the result. There are several version of the function. Syntax Generates a new context handle from a query: DBMS_XMLGEN.NEWCONTEXT ( query IN VARCHAR2) RETURN ctxHandle; Generates a new context handle from a query string in the form of a PL/SQL ref cursor: DBMS_XMLGEN.NEWCONTEXT ( queryString IN SYS_REFCURSOR) RETURN ctxHandle; Parameters Table 205-7 NEWCONTEXT Function Parameters Parameter Description query The query, in the form of a VARCHAR , the result of which must be converted to XML. queryString The query string in the form of a PL/SQL ref cursor, the result of which must be converted to XML.