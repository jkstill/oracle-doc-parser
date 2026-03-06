---
id: 19c__DBMS_MGWMSG.NVARRAY_FIND_NAME_TYPE
name: DBMS_MGWMSG.NVARRAY_FIND_NAME_TYPE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWMSG
tags: [dbms_mgwmsg]
source_file: DBMS_MGWMSG.html
---

# DBMS_MGWMSG.NVARRAY_FIND_NAME_TYPE

This function searches a name-value array for an element with the name and value type you specify.

## Syntax

```sql
DBMS_MGWMSG.NVARRAY_FIND_NAME_TYPE (
   p_array    IN SYS.MGW_NAME_VALUE_ARRAY_T,
   p_name     IN VARCHAR2,
   p_type     IN BINARY_INTEGER
   p_compare  IN BINARY_INTEGER DEFAULT CASE_SENSITIVE )
RETURN BINARY_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p_array | SYS.MGW_NAME_VALUE_ARRAY_T | IN | The name-value array to search |
| p_name | VARCHAR2 | IN | The name to find |
| p_type | BINARY_INTEGER | IN | The value type. Refer to the value type constants in Table 111-1 . |
| p_compare | BINARY_INTEGER | IN | Name comparison method. Values are CASE_SENSITIVE and CASE_INSENSITIVE . |

**Returns:** `BINARY_INTEGER`

## Usage Notes

Syntax DBMS_MGWMSG.NVARRAY_FIND_NAME_TYPE ( p_array IN SYS.MGW_NAME_VALUE_ARRAY_T, p_name IN VARCHAR2, p_type IN BINARY_INTEGER p_compare IN BINARY_INTEGER DEFAULT CASE_SENSITIVE ) RETURN BINARY_INTEGER; Parameters Table 111-25 NVARRAY_FIND_NAME_TYPE Function Parameters Parameter Description p_array The name-value array to search p_name The name to find p_type The value type. Refer to the value type constants in Table 111-1 . p_compare Name comparison method. Values are CASE_SENSITIVE and CASE_INSENSITIVE . Return Values Returns a positive integer that is the array index of the matching element, zero ( 0) if the specified name is not found, or negative one (-1) if the specified name is found but a type mismatch exists.