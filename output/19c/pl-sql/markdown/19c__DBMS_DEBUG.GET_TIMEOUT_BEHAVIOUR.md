---
id: 19c__DBMS_DEBUG.GET_TIMEOUT_BEHAVIOUR
name: DBMS_DEBUG.GET_TIMEOUT_BEHAVIOUR
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DEBUG
tags: [dbms_debug]
source_file: DBMS_DEBUG.html
---

# DBMS_DEBUG.GET_TIMEOUT_BEHAVIOUR

This procedure returns the current timeout behavior. This call is made in the target session.

## Syntax

```sql
DBMS_DEBUG.GET_TIMEOUT_BEHAVIOUR
 RETURN BINARY_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| oer |  |  | The OER (a 4-byte positive number) |

**Returns:** `BINARY_INTEGER`

## Usage Notes

Syntax DBMS_DEBUG.GET_TIMEOUT_BEHAVIOUR RETURN BINARY_INTEGER; Parameters Table 57-31 GET_TIMEOUT_BEHAVIOUR Function Parameters Parameter Description oer The OER (a 4-byte positive number) Return Values Table 57-32 GET_TIMEOUT_BEHAVIOUR Function Return Values Return Description success A successful completion Information Flags info_getOerInfo CONSTANT PLS_INTEGER:= 32; Usage Notes Less functionality is supported on OER breakpoints than on code breakpoints. In particular, note that: No "breakpoint number" is returned - the number of the OER is used instead. Thus it is impossible to set duplicate breakpoints on a given OER (it is a no-op). It is not possible to disable an OER breakpoint (although clients are free to simulate this by deleting it). OER breakpoints are deleted using delete_oer_breakpoint.