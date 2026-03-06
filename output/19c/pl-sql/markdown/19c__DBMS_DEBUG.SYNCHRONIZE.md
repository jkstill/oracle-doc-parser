---
id: 19c__DBMS_DEBUG.SYNCHRONIZE
name: DBMS_DEBUG.SYNCHRONIZE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DEBUG
tags: [dbms_debug]
source_file: DBMS_DEBUG.html
---

# DBMS_DEBUG.SYNCHRONIZE

This function waits until the target program signals an event. If info_requested is not NULL , then it calls GET_RUNTIME_INFO .

## Syntax

```sql
DBMS_DEBUG.SYNCHRONIZE (
   run_info       OUT  runtime_info,
   info_requested IN   BINARY_INTEGER := NULL)
  RETURN BINARY_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| run_info | runtime_info | OUT | Structure in which to write information about the program. By default, this includes information about what program is running and at which line execution has paused. |
| info_requested | BINARY_INTEGER | IN | Optional bit-field in which to request information other than the default (which is info_getStackDepth + info_getLineInfo ). 0 means that no information is requested at all (see DBMS_DEBUG Operational Notes for more about information flags). |

**Returns:** `BINARY_INTEGER`

## Usage Notes

Syntax DBMS_DEBUG.SYNCHRONIZE ( run_info OUT runtime_info, info_requested IN BINARY_INTEGER := NULL) RETURN BINARY_INTEGER; Parameters Table 57-54 SYNCHRONIZE Function Parameters Parameter Description run_info Structure in which to write information about the program. By default, this includes information about what program is running and at which line execution has paused. info_requested Optional bit-field in which to request information other than the default (which is info_getStackDepth + info_getLineInfo ). 0 means that no information is requested at all (see DBMS_DEBUG Operational Notes for more about information flags). Return Values Table 57-55 SYNCHRONIZE Function Return Values Return Description success A successful completion error_timeout Timed out before the program started execution error_communication Other communication error