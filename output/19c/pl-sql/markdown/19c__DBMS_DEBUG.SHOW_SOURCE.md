---
id: 19c__DBMS_DEBUG.SHOW_SOURCE
name: DBMS_DEBUG.SHOW_SOURCE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DEBUG
tags: [dbms_debug]
source_file: DBMS_DEBUG.html
---

# DBMS_DEBUG.SHOW_SOURCE

The procedure gets the source code. There are two overloaded SHOW_SOURCE procedures.

## Syntax

```sql
DBMS_DEBUG.SHOW_SOURCE (
   first_line  IN   BINARY_INTEGER,
   last_line   IN   BINARY_INTEGER,
   source      OUT  vc2_table);

DBMS_DEBUG.SHOW_SOURCE (
   first_line   IN     BINARY_INTEGER,
   last_line    IN     BINARY_INTEGER,
   window       IN     BINARY_INTEGER,
   print_arrow  IN     BINARY_INTEGER,
   buffer       IN OUT VARCHAR2,
   buflen       IN     BINARY_INTEGER,
   pieces       OUT    BINARY_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| first_line | BINARY_INTEGER | IN | Line number of first line to fetch (PL/SQL programs always start at line 1 and have no holes) |
| last_line | BINARY_INTEGER | IN | Line number of last line to fetch. No lines are fetched past the end of the program. |
| source | vc2_table) | OUT | The resulting table, which may be indexed by line# |
| window | BINARY_INTEGER | IN | 'Window' of lines (the number of lines around the current source line) |
| print_arrow | BINARY_INTEGER | IN | Nonzero means to print an arrow before the current line |
| buffer | VARCHAR2 | IN OUT | Buffer in which to place the source listing |
| buflen | BINARY_INTEGER | IN | Length of buffer |
| pieces | BINARY_INTEGER) | OUT | Set to nonzero if not all the source could be placed into the given buffer |

## Usage Notes

Syntax DBMS_DEBUG.SHOW_SOURCE ( first_line IN BINARY_INTEGER, last_line IN BINARY_INTEGER, source OUT vc2_table); DBMS_DEBUG.SHOW_SOURCE ( first_line IN BINARY_INTEGER, last_line IN BINARY_INTEGER, window IN BINARY_INTEGER, print_arrow IN BINARY_INTEGER, buffer IN OUT VARCHAR2, buflen IN BINARY_INTEGER, pieces OUT BINARY_INTEGER); Parameters Table 57-53 SHOW_SOURCE Procedure Parameters Parameter Description first_line Line number of first line to fetch (PL/SQL programs always start at line 1 and have no holes) last_line Line number of last line to fetch. No lines are fetched past the end of the program. source The resulting table, which may be indexed by line# window 'Window' of lines (the number of lines around the current source line) print_arrow Nonzero means to print an arrow before the current line buffer Buffer in which to place the source listing buflen Length of buffer pieces Set to nonzero if not all the source could be placed into the given buffer Return Values An indexed table of source-lines. The source lines are stored starting at first_line . If any error occurs, then the table is empty. Usage Notes The best way to get the source code (for a program that is being run) is to use SQL. For example: DECLARE info DBMS_DEBUG.runtime_info; BEGIN -- call DBMS_DEBUG.SYNCHRONIZE, CONTINUE, -- or GET_RUNTIME_INFO to fill in 'info' SELECT text INTO <buffer> FROM all_source WHERE owner = info.Program.Owner AND name = info.Program.Name AND line = info.Line#; END; However, this does not work for nonpersistent programs (for example, anonymous blocks and trigger invocation blocks). For nonpersistent programs, call SHOW_SOURCE . There are two flavors: one returns an indexed table of source lines, and the other returns a packed (and formatted) buffer. The second overloading of SHOW_SOURCE returns the source in a formatted buffer, complete with line-numbers. It is faster than the indexed table version, but it does not guarantee to fetch all the source. If the source does not fit in bufferlength ( buflen ), then additional pieces can be retrieved using the GET_MORE_SOURCE procedure ( pieces returns the number of additional pieces that need to be retrieved).