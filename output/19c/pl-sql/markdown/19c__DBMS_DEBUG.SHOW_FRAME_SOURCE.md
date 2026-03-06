---
id: 19c__DBMS_DEBUG.SHOW_FRAME_SOURCE
name: DBMS_DEBUG.SHOW_FRAME_SOURCE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DEBUG
tags: [dbms_debug]
source_file: DBMS_DEBUG.html
---

# DBMS_DEBUG.SHOW_FRAME_SOURCE

The procedure gets the source code. There are two overloaded SHOW_SOURCE procedures.

## Syntax

```sql
DBMS_DEBUG.SHOW_FRAME_SOURCE (
   first_line  IN            BINARY_INTEGER,
   last_line   IN            BINARY_INTEGER,
   source      IN OUT NOCOPY vc2_table,
   frame_num   IN            BINARY_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| first_line | BINARY_INTEGER | IN | Line number of first line to fetch (PL/SQL programs always start at line 1 and have no holes) |
| last_line | BINARY_INTEGER | IN | Line number of last line to fetch. No lines are fetched past the end of the program. |
| source | NOCOPY | IN OUT | The resulting table, which may be indexed by line# |
| frame_num | BINARY_INTEGER) | IN | 1-based frame number |

## Usage Notes

Syntax DBMS_DEBUG.SHOW_FRAME_SOURCE ( first_line IN BINARY_INTEGER, last_line IN BINARY_INTEGER, source IN OUT NOCOPY vc2_table, frame_num IN BINARY_INTEGER); Parameters Table 57-52 SHOW_FRAME_SOURCE Procedure Parameters Parameter Description first_line Line number of first line to fetch (PL/SQL programs always start at line 1 and have no holes) last_line Line number of last line to fetch. No lines are fetched past the end of the program. source The resulting table, which may be indexed by line# frame_num 1-based frame number Usage Notes You use this function only when backtrace shows an anonymous unit is executing at a given frame position and you need to view the source in order to set a breakpoint. If frame number is top of the stack and it's an anonymous block then SHOW_SOURCE can also be used. If it's a stored PL/SQL package/function/procedure then use SQL as described in the Usage Notes to SHOW_SOURCE Procedures .