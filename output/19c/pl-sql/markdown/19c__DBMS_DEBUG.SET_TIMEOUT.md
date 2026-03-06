---
id: 19c__DBMS_DEBUG.SET_TIMEOUT
name: DBMS_DEBUG.SET_TIMEOUT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DEBUG
tags: [dbms_debug]
source_file: DBMS_DEBUG.html
---

# DBMS_DEBUG.SET_TIMEOUT

This function sets the timeout value and returns the new timeout value.

## Syntax

```sql
DBMS_DEBUG.SET_TIMEOUT (
   timeout BINARY_INTEGER) 
  RETURN BINARY_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| timeout | BINARY_INTEGER) | IN | The timeout to use for communication between the target and debug sessions |

**Returns:** `BINARY_INTEGER`

## Usage Notes

Syntax DBMS_DEBUG.SET_TIMEOUT ( timeout BINARY_INTEGER) RETURN BINARY_INTEGER; Parameters Table 57-47 SET_TIMEOUT Function Parameters Parameter Description timeout The timeout to use for communication between the target and debug sessions