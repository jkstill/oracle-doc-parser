---
id: 19c__DBMS_DEBUG.ATTACH_SESSION
name: DBMS_DEBUG.ATTACH_SESSION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DEBUG
tags: [dbms_debug]
source_file: DBMS_DEBUG.html
---

# DBMS_DEBUG.ATTACH_SESSION

This procedure notifies the debug session about the target program.

## Syntax

```sql
DBMS_DEBUG.ATTACH_SESSION (
   debug_session_id  IN VARCHAR2,
   diagnostics       IN BINARY_INTEGER := 0);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| debug_session_id | VARCHAR2 | IN | Debug ID from a call to INITIALIZE in target session |
| diagnostics | BINARY_INTEGER | IN | Generate diagnostic output if nonzero |

## Usage Notes

Syntax DBMS_DEBUG.ATTACH_SESSION ( debug_session_id IN VARCHAR2, diagnostics IN BINARY_INTEGER := 0); Parameters Table 57-13 ATTACH_SESSION Procedure Parameters Parameter Description debug_session_id Debug ID from a call to INITIALIZE in target session diagnostics Generate diagnostic output if nonzero