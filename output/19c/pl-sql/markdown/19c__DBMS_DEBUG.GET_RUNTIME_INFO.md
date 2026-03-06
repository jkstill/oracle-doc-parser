---
id: 19c__DBMS_DEBUG.GET_RUNTIME_INFO
name: DBMS_DEBUG.GET_RUNTIME_INFO
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DEBUG
tags: [dbms_debug]
source_file: DBMS_DEBUG.html
---

# DBMS_DEBUG.GET_RUNTIME_INFO

This function returns information about the current program. It is only needed if the info_requested parameter to SYNCHRONIZE or CONTINUE was set to 0 .

## Syntax

```sql
DBMS_DEBUG.GET_RUNTIME_INFO (
   info_requested  IN  BINARY_INTEGER,
   run_info        OUT runtime_info)
  RETURN BINARY_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| info_requested | BINARY_INTEGER | IN | Which information should be returned in run_info when the program stops (see DBMS_DEBUG Operational Notes for information about information flags) |
| run_info | runtime_info) | OUT | Information about the state of the program |

**Returns:** `BINARY_INTEGER`

## Usage Notes

Note: This is currently only used by client-side PL/SQL. Note: This is currently only used by client-side PL/SQL. Syntax DBMS_DEBUG.GET_RUNTIME_INFO ( info_requested IN BINARY_INTEGER, run_info OUT runtime_info) RETURN BINARY_INTEGER; Parameters Table 57-30 GET_RUNTIME_INFO Function Parameters Parameter Description info_requested Which information should be returned in run_info when the program stops (see DBMS_DEBUG Operational Notes for information about information flags) run_info Information about the state of the program