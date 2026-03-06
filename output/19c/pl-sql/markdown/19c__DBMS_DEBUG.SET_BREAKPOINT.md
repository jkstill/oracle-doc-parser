---
id: 19c__DBMS_DEBUG.SET_BREAKPOINT
name: DBMS_DEBUG.SET_BREAKPOINT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DEBUG
tags: [dbms_debug]
source_file: DBMS_DEBUG.html
---

# DBMS_DEBUG.SET_BREAKPOINT

This function sets a breakpoint in a program unit, which persists for the current session.

## Syntax

```sql
DBMS_DEBUG.SET_BREAKPOINT (
   program     IN  program_info,
   line#       IN  BINARY_INTEGER,
   breakpoint# OUT BINARY_INTEGER,
   fuzzy       IN  BINARY_INTEGER := 0,
   iterations  IN  BINARY_INTEGER := 0)
  RETURN BINARY_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| program | program_info | IN | Information about the program unit in which the breakpoint is to be set. (In version 2.1 and later, the namespace, name, owner, and dblink may be set to NULL , in which case the breakpoint is placed in the currently-running program unit.) |
| line# | BINARY_INTEGER | IN | Line at which the breakpoint is to be set |
| breakpoint# | BINARY_INTEGER | OUT | On successful completion, contains the unique breakpoint number by which to refer to the breakpoint |
| fuzzy | BINARY_INTEGER | IN | Only applicable if there is no executable code at the specified line: 0 means return error_illegal_line 1 means search forward for an adjacent line at which to place the breakpoint -1 means search backward for an adjacent line at which to place the breakpoint |
| iterations | BINARY_INTEGER | IN | Number of times to wait before signalling this breakpoint |

**Returns:** `BINARY_INTEGER`

## Usage Notes

Syntax Execution pauses if the target program reaches the breakpoint. DBMS_DEBUG.SET_BREAKPOINT ( program IN program_info, line# IN BINARY_INTEGER, breakpoint# OUT BINARY_INTEGER, fuzzy IN BINARY_INTEGER := 0, iterations IN BINARY_INTEGER := 0) RETURN BINARY_INTEGER; Parameters Table 57-43 SET_BREAKPOINT Function Parameters Parameter Description program Information about the program unit in which the breakpoint is to be set. (In version 2.1 and later, the namespace, name, owner, and dblink may be set to NULL , in which case the breakpoint is placed in the currently-running program unit.) line# Line at which the breakpoint is to be set breakpoint# On successful completion, contains the unique breakpoint number by which to refer to the breakpoint fuzzy Only applicable if there is no executable code at the specified line: 0 means return error_illegal_line 1 means search forward for an adjacent line at which to place the breakpoint -1 means search backward for an adjacent line at which to place the breakpoint iterations Number of times to wait before signalling this breakpoint Return Values Note: The fuzzy and iterations parameters are not yet implemented Table 57-44 SET_BREAKPOINT Function Return Values Return Description success A successful completion error_illegal_line Cannot set a breakpoint at that line error_bad_handle No such program unit exists Note: The fuzzy and iterations parameters are not yet implemented