---
id: 19c__DBMS_SESSION.LIST_CONTEXT
name: DBMS_SESSION.LIST_CONTEXT
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SESSION
tags: [dbms_session]
source_file: DBMS_SESSION.html
---

# DBMS_SESSION.LIST_CONTEXT

This procedure returns a list of active namespaces and contexts for the current session.

## Syntax

```sql
TYPE AppCtxRecTyp IS RECORD ( 
   namespace VARCHAR2(30), 
   attribute VARCHAR2(30),
   value     VARCHAR2(256)); 

TYPE AppCtxTabTyp IS TABLE OF AppCtxRecTyp INDEX BY BINARY_INTEGER; 

DBMS_SESSION.LIST_CONTEXT ( 
   list OUT AppCtxTabTyp, 
   size OUT NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| list | AppCtxTabTyp | OUT | Buffer to store a list of application context set in the current session |

## Usage Notes

Syntax TYPE AppCtxRecTyp IS RECORD ( namespace VARCHAR2(30), attribute VARCHAR2(30), value VARCHAR2(256)); TYPE AppCtxTabTyp IS TABLE OF AppCtxRecTyp INDEX BY BINARY_INTEGER; DBMS_SESSION.LIST_CONTEXT ( list OUT AppCtxTabTyp, size OUT NUMBER); Parameters Table 154-12 LIST_CONTEXT Procedure Parameters Parameter Description list Buffer to store a list of application context set in the current session Return Values Table 154-13 LIST_CONTEXT Procedure Return Values Return Description list A list of (namespace, attribute, values) set in current session size Returns the number of entries in the buffer returned Usage Notes The context information in the list appears as a series of < namespace > < attribute > < value >. Because list is a table type variable, its size is dynamically adjusted to the size of returned list.