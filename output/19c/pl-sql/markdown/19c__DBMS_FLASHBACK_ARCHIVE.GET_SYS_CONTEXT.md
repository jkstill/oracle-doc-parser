---
id: 19c__DBMS_FLASHBACK_ARCHIVE.GET_SYS_CONTEXT
name: DBMS_FLASHBACK_ARCHIVE.GET_SYS_CONTEXT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FLASHBACK_ARCHIVE
tags: [dbms_flashback_archive]
source_file: DBMS_FLASHBACK_ARCHIVE.html
---

# DBMS_FLASHBACK_ARCHIVE.GET_SYS_CONTEXT

This function gets the context previously selected by the SET_CONTEXT_LEVEL Procedure.

## Syntax

```sql
DBMS_FLASHBACK_ARCHIVE.GET_SYS_CONTEXT (
   xid            IN   RAW, 
   namespace      IN   VARCHAR2, 
   parameter      IN   VARCHAR2)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xid | RAW | IN | Transaction identifier is an opaque handle to a transaction obtained from the versions query |
| namespace | VARCHAR2 | IN | Namespace |
| parameter | VARCHAR2) | IN | If undefined, the subprogram returns NULL |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_FLASHBACK_ARCHIVE.GET_SYS_CONTEXT ( xid IN RAW, namespace IN VARCHAR2, parameter IN VARCHAR2) RETURN VARCHAR2; Parameters Table 73-11 GET_SYS_CONTEXT Function Parameters Parameter Description xid Transaction identifier is an opaque handle to a transaction obtained from the versions query namespace Namespace parameter If undefined, the subprogram returns NULL