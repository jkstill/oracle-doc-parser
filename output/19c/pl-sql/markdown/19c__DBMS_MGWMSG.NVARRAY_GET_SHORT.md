---
id: 19c__DBMS_MGWMSG.NVARRAY_GET_SHORT
name: DBMS_MGWMSG.NVARRAY_GET_SHORT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWMSG
tags: [dbms_mgwmsg]
source_file: DBMS_MGWMSG.html
---

# DBMS_MGWMSG.NVARRAY_GET_SHORT

This function gets the value of the name-value array element that you specify in p_name and with the SHORT_VALUE value type .

## Syntax

```sql
DBMS_MGWMSG.NVARRAY_GET_SHORT (
   p_array    IN SYS.MGW_NAME_VALUE_ARRAY_T,
   p_name     IN VARCHAR2,
   p_compare  IN BINARY_INTEGER DEFAULT CASE_SENSITIVE )
RETURN INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p_array | SYS.MGW_NAME_VALUE_ARRAY_T | IN | The name-value array |
| p_name | VARCHAR2 | IN | The value name |
| p_compare | BINARY_INTEGER | IN | Name comparison method. Values are CASE_SENSITIVE and CASE_INSENSITIVE . |

**Returns:** `INTEGER`

## Usage Notes

Syntax DBMS_MGWMSG.NVARRAY_GET_SHORT ( p_array IN SYS.MGW_NAME_VALUE_ARRAY_T, p_name IN VARCHAR2, p_compare IN BINARY_INTEGER DEFAULT CASE_SENSITIVE ) RETURN INTEGER; Parameters Table 111-35 NVARRAY_GET_SHORT Function Parameters Parameter Description p_array The name-value array p_name The value name p_compare Name comparison method. Values are CASE_SENSITIVE and CASE_INSENSITIVE . Return Values Returns the value, or NULL if either the specified name is not found or a type mismatch exists.