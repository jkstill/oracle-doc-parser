---
id: 19c__DBMS_DEBUG
name: DBMS_DEBUG
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DEBUG
tags: [dbms_debug]
source_file: DBMS_DEBUG.html
---

# DBMS_DEBUG

The DBMS_DEBUG package defines RECORD types and TABLE types.

## Syntax

```sql
TYPE breakpoint_info IS RECORD (
   name        VARCHAR2(30),
   owner       VARCHAR2(30),
   dblink      VARCHAR2(30),
   line#       BINARY_INTEGER,
   libunittype BINARY_INTEGER,
   status      BINARY_INTEGER);
```

## Usage Notes

RECORD Types BREAKPOINT_INFO Record Type PROGRAM_INFO Record Type RUNTIME_INFO Record Type TABLE Types BACKTRACE_TABLE Table Type BREAKPOINT_TABLE Table Type INDEX_TABLE Table Type VC2_TABLE Table Type Syntax TYPE breakpoint_info IS RECORD ( name VARCHAR2(30), owner VARCHAR2(30), dblink VARCHAR2(30), line# BINARY_INTEGER, libunittype BINARY_INTEGER, status BINARY_INTEGER); Fields Table 57-9 BREAKPOINT_INFO Fields Field Description name Name of the program unit owner Owner of the program unit dblink Database link, if remote line# Line number libunittype NULL , unless this is a nested procedure or function status See Constants for values of breakpoint_status_* This is used for stack backtraces and for setting and examining breakpoints. The read-only fields are currently ignored by Probe for breakpoint operations. They are set by Probe only for stack backtraces.