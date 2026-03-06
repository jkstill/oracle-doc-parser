---
id: 19c__DBMS_DEBUG.CONTINUE
name: DBMS_DEBUG.CONTINUE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DEBUG
tags: [dbms_debug]
source_file: DBMS_DEBUG.html
---

# DBMS_DEBUG.CONTINUE

This function passes the given breakflags (a mask of the events that are of interest) to Probe in the target process. It tells Probe to continue execution of the target process, and it waits until the target process runs to completion or signals an event.

## Syntax

```sql
DBMS_DEBUG.CONTINUE (
   run_info       IN OUT runtime_info,
   breakflags     IN     BINARY_INTEGER,
   info_requested IN     BINARY_INTEGER := NULL)
  RETURN BINARY_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| run_info | runtime_info | IN OUT | Information about the state of the program |
| breakflags | BINARY_INTEGER | IN | Mask of events that are of interest (see the discussion about break flags under DBMS_DEBUG Operational Notes ) |
| info_requested | BINARY_INTEGER | IN | Which information should be returned in run_info when the program stops (see the discussion of information flags under DBMS_DEBUG Operational Notes ) |

**Returns:** `BINARY_INTEGER`

## Usage Notes

If info_requested is not NULL , then calls GET_RUNTIME_INFO . Syntax DBMS_DEBUG.CONTINUE ( run_info IN OUT runtime_info, breakflags IN BINARY_INTEGER, info_requested IN BINARY_INTEGER := NULL) RETURN BINARY_INTEGER; Parameters Table 57-14 CONTINUE Function Parameters Parameter Description run_info Information about the state of the program breakflags Mask of events that are of interest (see the discussion about break flags under DBMS_DEBUG Operational Notes ) info_requested Which information should be returned in run_info when the program stops (see the discussion of information flags under DBMS_DEBUG Operational Notes ) Return Values Table 57-15 CONTINUE Function Return Values Return Description success error_timeout Timed out before the program started running error_communication Other communication error