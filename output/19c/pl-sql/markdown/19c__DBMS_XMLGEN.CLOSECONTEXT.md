---
id: 19c__DBMS_XMLGEN.CLOSECONTEXT
name: DBMS_XMLGEN.CLOSECONTEXT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLGEN
tags: [dbms_xmlgen]
source_file: DBMS_XMLGEN.html
---

# DBMS_XMLGEN.CLOSECONTEXT

This procedure closes a given context and releases all resources associated with it, including the SQL cursor and bind and define buffers. After this call, the handle cannot be used for a subsequent function call.

## Syntax

```sql
DBMS_XMLGEN.CLOSECONTEXT (
   ctx  IN ctxHandle);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctx | ctxHandle) | IN | The context handle to close. |

## Usage Notes

Syntax DBMS_XMLGEN.CLOSECONTEXT ( ctx IN ctxHandle); Parameters Table 205-2 CLOSECONTEXT Procedure Parameters Parameter Description ctx The context handle to close.