---
id: 19c__DBMS_DEBUG.SHOW_BREAKPOINTS
name: DBMS_DEBUG.SHOW_BREAKPOINTS
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DEBUG
tags: [dbms_debug]
source_file: DBMS_DEBUG.html
---

# DBMS_DEBUG.SHOW_BREAKPOINTS

There are two overloaded procedures that return a listing of the current breakpoints. There are three overloaded SHOW_BREAKPOINTS procedures.

## Syntax

```sql
DBMS_DEBUG.SHOW_BREAKPOINTS (
   listing    IN OUT VARCHAR2);

DBMS_DEBUG.SHOW_BREAKPOINTS (
   listing    OUT breakpoint_table);

DBMS_DEBUG.SHOW_BREAKPOINTS (
   code_breakpoints  OUT breakpoint_table, 
   oer_breakpoints   OUT oer_table);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| listing | VARCHAR2) | IN OUT | A formatted buffer (including newlines) of the breakpoints. Indexed table of breakpoint entries. The breakpoint number is indicated by the index into the table. Breakpoint numbers start at 1 and are reused when deleted. |
| code_breakpoints | breakpoint_table | OUT | The indexed table of breakpoint entries, indexed by breakpoint number |
| oer_breakpoints | oer_table) | OUT | The indexed table of OER breakpoints, indexed by OER |

## Usage Notes

Syntax DBMS_DEBUG.SHOW_BREAKPOINTS ( listing IN OUT VARCHAR2); DBMS_DEBUG.SHOW_BREAKPOINTS ( listing OUT breakpoint_table); DBMS_DEBUG.SHOW_BREAKPOINTS ( code_breakpoints OUT breakpoint_table, oer_breakpoints OUT oer_table); Parameters Table 57-51 SHOW_BREAKPOINTS Procedure Parameters Parameter Description listing A formatted buffer (including newlines) of the breakpoints. Indexed table of breakpoint entries. The breakpoint number is indicated by the index into the table. Breakpoint numbers start at 1 and are reused when deleted. code_breakpoints The indexed table of breakpoint entries, indexed by breakpoint number oer_breakpoints The indexed table of OER breakpoints, indexed by OER