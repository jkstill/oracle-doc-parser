---
id: 19c__DBMS_DEBUG.GET_LINE_MAP
name: DBMS_DEBUG.GET_LINE_MAP
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DEBUG
tags: [dbms_debug]
source_file: DBMS_DEBUG.html
---

# DBMS_DEBUG.GET_LINE_MAP

This function finds line and entrypoint information about a program so that a debugger can determine the source lines at which it is possible to place breakpoints.

## Syntax

```sql
DBMS_DEBUG.GET_LINE_MAP (
   program                IN   program_info,
   maxline                OUT  BINARY_INTEGER,
   number_of_entry_points OUT  BINARY_INTEGER,
   linemap                OUT  RAW)
  RETURN BINARY_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| program | program_info | IN | A top-level program unit (procedure / package / function / package body, and so on). Its Namespace , Name , and Owner fields must be initialized, the remaining fields are ignored. |
| maxline | BINARY_INTEGER | OUT | The largest source code line number in 'program' |
| number_of_entry_points | BINARY_INTEGER | OUT | The number of subprograms in 'program' |
| linemap | RAW) | OUT | A bitmap representing the executable lines of 'program'. If line number N is executable, bit number N MOD 8 will be set to 1 at linemap position N / 8. The length of returned linemap is either maxline divided by 8 (plus one if maxline MOD 8 is not zero) or 32767 in the unlikely case of maxline being larger than 32767 * 8. |

**Returns:** `BINARY_INTEGER`

## Usage Notes

Syntax DBMS_DEBUG.GET_LINE_MAP ( program IN program_info, maxline OUT BINARY_INTEGER, number_of_entry_points OUT BINARY_INTEGER, linemap OUT RAW) RETURN BINARY_INTEGER; Parameters Table 57-28 GET_LINE_MAP Function Parameters Parameter Description program A top-level program unit (procedure / package / function / package body, and so on). Its Namespace , Name , and Owner fields must be initialized, the remaining fields are ignored. maxline The largest source code line number in 'program' number_of_entry_points The number of subprograms in 'program' linemap A bitmap representing the executable lines of 'program'. If line number N is executable, bit number N MOD 8 will be set to 1 at linemap position N / 8. The length of returned linemap is either maxline divided by 8 (plus one if maxline MOD 8 is not zero) or 32767 in the unlikely case of maxline being larger than 32767 * 8. Return Values Table 57-29 GET_LINE_MAP Function Return Values Return Description success A successful completion error_no_debug_info The program unit exists, but has no debug info error_bad_handle No such program unit exists