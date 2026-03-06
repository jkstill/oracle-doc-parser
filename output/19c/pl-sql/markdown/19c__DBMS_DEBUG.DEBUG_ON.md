---
id: 19c__DBMS_DEBUG.DEBUG_ON
name: DBMS_DEBUG.DEBUG_ON
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DEBUG
tags: [dbms_debug]
source_file: DBMS_DEBUG.html
---

# DBMS_DEBUG.DEBUG_ON

This procedure marks the target session so that all PL/SQL is run in debug mode. This must be done before any debugging can take place.

## Syntax

```sql
DBMS_DEBUG.DEBUG_ON (
   no_client_side_plsql_engine BOOLEAN := TRUE,
   immediate                   BOOLEAN := FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| no_client_side_plsql_engine | BOOLEAN | IN | Should be left to its default value unless the debugging session is taking place from a client-side PL/SQL engine |
| immediate | BOOLEAN | IN | If this is TRUE , then the interpreter immediately switches itself into debug-mode, instead of continuing in regular mode for the duration of the call. |

## Usage Notes

Syntax DBMS_DEBUG.DEBUG_ON ( no_client_side_plsql_engine BOOLEAN := TRUE, immediate BOOLEAN := FALSE); Parameters Table 57-16 DEBUG_ON Procedure Parameters Parameter Description no_client_side_plsql_engine Should be left to its default value unless the debugging session is taking place from a client-side PL/SQL engine immediate If this is TRUE , then the interpreter immediately switches itself into debug-mode, instead of continuing in regular mode for the duration of the call.