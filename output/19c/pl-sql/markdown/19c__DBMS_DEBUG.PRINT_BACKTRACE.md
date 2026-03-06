---
id: 19c__DBMS_DEBUG.PRINT_BACKTRACE
name: DBMS_DEBUG.PRINT_BACKTRACE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DEBUG
tags: [dbms_debug]
source_file: DBMS_DEBUG.html
---

# DBMS_DEBUG.PRINT_BACKTRACE

This procedure prints a backtrace listing of the current execution stack. This should only be called if a program is currently running.

## Syntax

```sql
DBMS_DEBUG.PRINT_BACKTRACE (
  listing IN OUT VARCHAR2); 

DBMS_DEBUG.PRINT_BACKTRACE (
  backtrace OUT backtrace_table);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| listing | VARCHAR2) | IN OUT | A formatted character buffer with embedded newlines |
| backtrace | backtrace_table) | OUT | 1-based indexed table of backtrace entries. The currently-running procedure is the last entry in the table (that is, the frame numbering is the same as that used by GET_VALUE ). Entry 1 is the oldest procedure on the stack. |

## Usage Notes

There are two overloaded PRINT_BACKTRACE procedures. Syntax DBMS_DEBUG.PRINT_BACKTRACE ( listing IN OUT VARCHAR2); DBMS_DEBUG.PRINT_BACKTRACE ( backtrace OUT backtrace_table); Parameters Table 57-38 PRINT_BACKTRACE Procedure Parameters Parameter Description listing A formatted character buffer with embedded newlines backtrace 1-based indexed table of backtrace entries. The currently-running procedure is the last entry in the table (that is, the frame numbering is the same as that used by GET_VALUE ). Entry 1 is the oldest procedure on the stack.